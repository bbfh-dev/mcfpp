from mcfpp.lang import Criteria
from mcfpp.lib.nbt import NBT
from mcfpp.lib.tree import Node
from mcfpp.utils import override
from .base import BaseModule


def has_custom_name(criteria: tuple | Criteria):
    return type(criteria) is tuple and len(criteria) > 1


class Score(BaseModule):
    builtin = True

    @override
    async def build(self):
        root = Node("(namespace)")
        root.add_branch("functions/load")
        for name, criteria in self.cls_variables().items():
            display_name = ""
            if has_custom_name(criteria):
                display_name = NBT.string(criteria[1])
                criteria = criteria[0]
            root.as_branch("functions/load").file.add_head(
                f"scoreboard objectives add {self.prefix}.{name} {criteria.value} {display_name}",
            )
        return root
