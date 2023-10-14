import re
from copy import copy
from enum import Enum

from mcfpp.lib.nbt import NBT
from mcfpp.utils import get_var
from .structs import Point


class DisplayEntity:
    def __init__(
        self,
        name: str,
        material: str | Enum,
        pos: Point = None,
        rot: Point = None,
        scale: Point = None,
        brightness: dict = None,
        properties: dict = None,
        width: float = None,
        height: float = None,
    ):
        self.name = name
        self.material = material
        self.pos: Point = get_var(pos, Point(0))
        self.rot: Point = get_var(rot, Point(0))
        self.scale: Point = get_var(scale, Point(1))
        self.brightness = get_var(brightness, {})
        self.properties = get_var(properties, {})
        self.width = get_var(width, 1.0)
        self.height = get_var(height, 1.0)

    @property
    def material_id(self):
        if issubclass(self.material.__class__, Enum):
            return self.material.value
        return self.material

    @property
    def material_type(self):
        if issubclass(self.material.__class__, Enum):
            return re.sub(r"__.*", "", self.material.name).lower()
        return "generic"

    @property
    def partial_nbt(self):
        return {}

    @property
    def nbt(self) -> dict:
        return {
            **self.partial_nbt,
            **self.brightness,
            "Tags": [
                "+<namespace>",
                f"--{self.material_type}",
                "--new",
            ],
            "width": self.width,
            "height": self.height,
            "transformation": {
                "left_rotation": self.rot.left_rotation,
                "right_rotation": self.rot.right_rotation,
                "translation": self.pos.as_vec(),
                "scale": self.scale.as_vec(),
            },
        }

    def move(self, new_pos: Point):
        """
        Creates a new copy of the unit
        with a different position
        :return: Modified copy
        """
        buffered = self.pos
        self.pos = new_pos
        new_unit = copy(self)
        self.pos = buffered
        return new_unit


class Block(DisplayEntity):
    @property
    def partial_nbt(self):
        return {
            "id": "block_display",
            "block_state": {"Name": self.material_id, "Properties": self.properties},
        }


class Item(DisplayEntity):
    @property
    def partial_nbt(self):
        return {
            "id": "item_display",
            "item": {
                "id": self.material_id,
                "Count": NBT.byte(1),
                "tag": self.properties,
            },
        }


class Text(DisplayEntity):
    @property
    def partial_nbt(self):
        return {
            "id": "text_display",
            "text": NBT.string(self.material_id()),
            **self.properties,
        }
