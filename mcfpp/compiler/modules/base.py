from mcfpp.lang import Scoreboard
from mcfpp.lib.tree import File, Node
from mcfpp.utils import is_builtin, is_method, is_variable


class BaseModule:
    builtin = True

    class Source:
        def __init__(self):
            self._file = File([])

        def __add__(self, other):
            if type(other) is str:
                self._file.add(other)
            if type(other) is tuple:
                self._file.add(" ".join(map(lambda x: str(x), other)))
            return self

        def __repr__(self):
            return self._file.code

        def op(self, score: Scoreboard, operations: Scoreboard):
            pass

        def run_if(self, condition: str, lines: list[str]):
            pass

    @classmethod
    def cls_variables(cls):
        return {
            k: v
            for k, v in cls.__dict__.items()
            if is_variable(v) and not is_builtin(k)
        }

    @classmethod
    def cls_methods(cls):
        return {
            k: v for k, v in cls.__dict__.items() if is_method(v) and not is_builtin(k)
        }

    @classmethod
    def cls_location(cls, /, until):
        return ".".join([i.__name__ for i in cls.traverse(until=until)])

    @property
    def variables(self):
        return self.cls_variables()

    @property
    def methods(self):
        return self.cls_methods()

    @property
    def dir(self):
        return self.__class__.__dict__.get("dir", "<namespace>")

    @classmethod
    def traverse(cls, /, until: type):
        result: list[type] = []
        for c in cls.mro():
            if c is until:
                result.reverse()
                return result
            result.append(c)
        return []

    def __init__(self, prefix: str):
        self.tree = Node(self.dir)
        self.prefix = prefix

    async def build(self):
        """Build the module tree"""
