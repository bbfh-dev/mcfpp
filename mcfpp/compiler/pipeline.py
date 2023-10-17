import asyncio
import re

from beet import Context, Function

import mcfpp.std.delayed_load as delayed_load
import mcfpp.std.registry as registry
from mcfpp.lib.tree import Node, alias
from .modules import BaseModule
from .preprocessor import Preprocessor


class Pipeline:
    def __init__(self, ctx: Context, prefix: str):
        self.ctx = ctx
        self.prefix = prefix
        self._modules: list[type[BaseModule]] = []
        self._config: dict[str, bool] = {}
        self.trees: list[Node] = []

    def _set_property(self, key: str, value: bool):
        if self._config.get(key) is None:
            self._config[key] = value

    def configure(
        self,
        /,
        delay_load=True,
        garbage_collection=True,
        tick_schedule=True,
        add_header=True,
        prettier_code=True,
    ):
        self._set_property("garbage_collection", garbage_collection)
        self._set_property("tick_schedule", tick_schedule)
        self._set_property("delay_load", delay_load)
        self._set_property("add_header", add_header)
        self._set_property("prettier_code", prettier_code)
        return self

    def add(self, *modules: type[BaseModule]):
        self._modules.extend(modules)
        return self

    def _has_module(self, name: str):
        for module in self._modules:
            if type(module) is not type:
                continue
            if module.cls_parent().__name__ == name:
                return True
        return False

    def _merge_trees(self, tree: Node):
        skip = False
        for self_tree in self.trees:
            if self_tree.name == tree.name:
                self_tree.merge(tree)
                skip = True
                break
        if not skip:
            self.trees.append(tree)
        return self

    async def _build(self):
        tasks = []
        for module in map(
            lambda x: x(self.prefix, fn_has_module=self._has_module), self._modules
        ):
            tasks.append(asyncio.create_task(module.build()))
        for tree in await asyncio.gather(*tasks):
            self._merge_trees(tree)
        for tree in self.trees:
            for node in tree.walk():
                node.name = alias(self.ctx, tree.extra, node)
            for branch in tree.branches:
                node = tree.as_branch(re.sub(r"\w+:", "", branch))
                if ":functions" in branch:
                    self.ctx.data.functions[branch] = Function(
                        Preprocessor(node, self.ctx, self._config).process().code,
                        tags=node.file.tags,
                    )

    def _include_std(self):
        if self._config.get("delay_load"):
            self.add(*delayed_load.__modules__)
        self.add(*registry.__modules__)

    def run(self, /, zipped: bool = False):
        self.ctx.data.zipped = zipped
        self.ctx.assets.zipped = zipped
        self.configure()  # Default config
        self._include_std()
        asyncio.run(self._build())
