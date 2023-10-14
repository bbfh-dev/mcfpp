from .display import DisplayEntity
from .structs import Axis, Point


def fill(unit: DisplayEntity, point1: Point, point2: Point, distance: float = 1.0):
    """
    'Fills' the area using the provided unit.
    Inclusive in both boundaries.
    :return: Array of units in the specified area
    """
    result = []
    for x in range(abs(round(point2.x - point1.x)) + 1):
        for z in range(abs(round(point2.z - point1.z)) + 1):
            for y in range(abs(round(point2.y - point1.y)) + 1):
                result.append(
                    unit.move(
                        Point(
                            min(point1.x + x * distance, point2.x),
                            min(point1.z + z * distance, point2.z),
                            min(point1.y + y * distance, point2.y),
                        )
                    )
                )
    return result


def mirror(*units: DisplayEntity, axis: Axis, offset: Point) -> list[DisplayEntity]:
    """
    Mirrors units along an axis.
    :return: Both original and mirrored units
    """

    def mirror_attr(attr: Point):
        """
        Used to ensure no code repetition in the future
        in-case there will be a need for mirroring other attributes (preferably)
        """
        return Point(
            attr.x * -1 + offset.x if axis is Axis.X else attr.x,
            attr.z * -1 + offset.z if axis is Axis.Z else attr.z,
            attr.y * -1 + offset.y if axis is Axis.Y else attr.y,
        )

    return [
        *units,
        *[unit.move(mirror_attr(unit.pos)) for unit in units],
    ]


def offset(*units: DisplayEntity, _offset: Point):
    """
    Offset units by a certain amount
    """
    return [
        unit.move(
            Point(
                unit.pos.x + _offset.x,
                unit.pos.y + _offset.y,
                unit.pos.z + _offset.z,
            )
        )
        for unit in units
    ]
