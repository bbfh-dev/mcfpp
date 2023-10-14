import os


class File:
    def __init__(self, body: list[str]):
        self._head: list[str] = []
        self._body: list[str] = body
        self._tail: list[str] = []
        self.tags: list[str] = []

    @property
    def lines(self):
        return [*self._head, *self._body, *self._tail]

    @property
    def code(self):
        return os.linesep.join(self.lines)

    def add(self, *lines: str):
        self._body.extend(lines)
        return self

    def add_tail(self, *lines: str):
        self._tail.extend(lines)
        return self

    def add_head(self, *lines: str):
        self._head.extend(lines)
        return self

    def set(self, *lines: str):
        self._body = list(lines)
        return self

    def set_tail(self, *lines: str):
        self._tail = list(lines)
        return self

    def set_head(self, *lines: str):
        self._head = list(lines)
        return self

    def extend(self, file: "File"):
        self._head.extend(file._head)
        self._body.extend(file._body)
        self._tail.extend(file._tail)
