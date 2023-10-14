from typing import Callable

from beet import Context


class BaseRunner:
    def __init__(self, ctx: Context, lines: list[str]):
        self.ctx = ctx
        self.lines = lines

    def iterate(self, fn: Callable):
        for idx, line in enumerate(self.lines):
            self.lines[idx] = fn(line)

    def run(self):
        return self
