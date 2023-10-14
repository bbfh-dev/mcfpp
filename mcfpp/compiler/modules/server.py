from mcfpp.lib.tree import Node
from mcfpp.utils import override
from .base import BaseModule


class Server(BaseModule):
    @override
    async def build(self):
        return Node("(namespace)")
