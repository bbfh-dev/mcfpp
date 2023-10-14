import os

from mcfpp.utils import get_var
from .file import File

sep = "/"


class Node:
    def __init__(self, name: str, parent: "Node" = None, body: list[str] = None):
        self.name = name
        self.parent = parent
        self.children: list["Node"] = []
        self.file = File(get_var(body, []))

    @property
    def depth(self):
        if self.parent is None:
            return 0
        return self.parent.depth + 1

    @property
    def location(self):
        """
        Get the resource location as `root:path/to/node`
        """
        if self.parent is None:
            return self.name
        tree = self.traverse("name")
        return f"{tree[0]}:{sep.join(tree[1:])}"

    @property
    def branches(self) -> list[str]:
        return [leaf.location for leaf in self.leaves()]

    def traverse(self, attr: str) -> list[str]:
        """
        Recursively get the attribute of the node
        and all of its parents' attributes
        """
        if self.parent is None:
            return [getattr(self, attr)]
        return [*self.parent.traverse(attr), getattr(self, attr)]

    def walk(self) -> list["Node"]:
        """
        Recursively walk the node tree
        """
        if len(self.children) == 0:
            return [self]
        result = []
        for child in self.children:
            result.extend(child.walk())
        return [*result, self]

    def leaves(self) -> list["Node"]:
        """
        Recursively walk the node tree
        """
        if len(self.children) == 0:
            return [self]
        result = []
        for child in self.children:
            result.extend(child.leaves())
        return result

    def set_parent(self, node: "Node"):
        self.parent = node
        return self

    def merge(self, *trees: "Node"):
        for tree in trees:
            for node in tree.children:
                self.children.append(node.set_parent(self))
        return self

    def add(self, node: "Node"):
        for child in self.children:
            if child.name == node.name:
                child.file.extend(node.file)
                return self
        node.parent = self
        self.children.append(node)
        return node

    def add_branch(self, path: str):
        pivot = self
        for name in path.split("/"):
            pivot = pivot.add(Node(name))
        return self

    def as_branch(self, path: str):
        pivot = self
        for name in path.replace(":", "/").split("/"):
            pivot = pivot.get_child(name)
        return pivot

    def get_child(self, name: str):
        for child in self.children:
            if child.name == name:
                return child
        return None

    def __repr__(self):
        suffix = f" — [{len(self.file.lines)} Lines]" if self.file.lines else ""
        return f"{self.name}{suffix}" + os.linesep.join(
            [""] + [f"{' ' * (self.depth * 2)}└ {node}" for node in self.children]
        )
