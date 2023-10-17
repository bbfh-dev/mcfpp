import re

from beet import Context

from .node import Node


def alias(ctx: Context, extra: dict[str, str], node: Node):
    name = re.sub(r"[()]", "", node.name)
    aliases = {
        "namespace": ctx.project_id,
        "module": extra.get("parent").lower(),
        "class": extra.get("this").lower(),
        "this": node.location,
    }
    if name in aliases.keys():
        return aliases.get(name)
    return name
