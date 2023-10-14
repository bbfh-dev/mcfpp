import re

from mcfpp.utils import override
from .base import BaseRunner


def format_selector_arguments(line: str):
    matches: list[re.Match] = [i for i in re.finditer(r"(@\w+)\[([^]]+).", line)]
    for match in matches:
        replacement = [
            re.sub(r" *= *", "=", i.strip()) for i in match.group(2).split(",")
        ]
        line = line.replace(
            match.group(), "{}[{}]".format(match.group(1), ", ".join(replacement))
        )
    return line


class Prettier(BaseRunner):
    @override
    def run(self):
        self.iterate(lambda line: line.strip())
        self.iterate(format_selector_arguments)
        return self
