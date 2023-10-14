from typing import Callable


def override(fn: Callable):
    """Placeholder for 3.12 override() decorator"""

    def call(*args, **kwargs):
        return fn(*args, **kwargs)

    return call
