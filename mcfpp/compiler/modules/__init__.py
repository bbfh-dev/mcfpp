from .base import BaseModule
from .entity import Entity
from .player import Player
from .score import Score
from .server import Server


class Empty(Server):
    pass


def requires(*modules: type[BaseModule]):
    """
    Class decorator that prevents a module from being compiled
    if the modules specified in it are not used in the pipeline.

    Useful to ensure no unused code is produced.
    """

    def wrap(cls):
        def call(*args, **kwargs):
            for module in modules:
                if not kwargs.get("fn_has_module")(module.__name__):
                    return Empty(*args, **kwargs)
            return cls(*args, **kwargs)

        return call

    return wrap
