import os

from beet import Context
from mcfpp.lib.tree import Node
from mcfpp.utils import is_empty

from .runners import BaseRunner, Prettier


class Preprocessor:
    def __init__(self, tree: Node, ctx: Context, config: dict[str, bool]):
        self.file = tree.file
        self.ctx = ctx
        self.config = config
        self._runners: list[type[BaseRunner]] = []
        self._lines: list[str] = []

    @property
    def code(self):
        return os.linesep.join(self._lines)

    def add(self, runner: type[BaseRunner]):
        self._runners.append(runner)

    def run(self):
        for Runner in self._runners:
            self._lines = Runner(self.ctx, self._lines).run().lines
        return self

    def post(self):
        if self.config.get("add_header"):
            self._lines.insert(0, "# Generated using MCFunction++")
        if not is_empty(self.file.lines[-1]):
            self._lines.append("")

    def process(self):
        self._lines = self.file.lines
        if not is_empty(self._lines):
            if self.config.get("prettier_code"):
                self.add(Prettier)
            self.run()
            self.post()
        return self
