from mcfpp.utils import override, path
from .base import BaseModule


class Server(BaseModule):
    builtin = True

    @override
    async def build(self):
        for name, fn in self.methods.items():
            namespace, paths = self.file(name).split(":")[0], path(
                "functions", self.file(name).split(":")[1]
            )
            self.tree.name = namespace
            self.tree.add_branch(paths)
            # self.tree.as_branch(paths).file.add("say Hi")
        return self.tree
