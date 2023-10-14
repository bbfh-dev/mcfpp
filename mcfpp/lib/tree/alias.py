from beet import Context

from .node import Node


def alias(ctx: Context, node: Node):
    aliases = {
        "(namespace)": ctx.project_id,
        "(~)": ctx.project_id,
        "(this)": node.location,
        "(.)": node.location,
    }
    if node.name in aliases.keys():
        return aliases.get(node.name)
    return node.name
