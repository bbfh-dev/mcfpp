from typing import Callable


class Event:
    @classmethod
    def function(cls, *function_tags: str):
        def decorate(fn: Callable):
            def call(*args, **kwargs):
                print(args, kwargs)
                return fn(*args, **kwargs)

            return call

        return decorate

    @classmethod
    def advancement(cls, criteria: dict):
        pass

    @classmethod
    def on_load(cls, execute: str = None):
        pass

    @classmethod
    def on_tick(cls, execute: str = None):
        pass
