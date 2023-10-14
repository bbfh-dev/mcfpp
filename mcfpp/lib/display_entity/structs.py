from enum import Enum

from mcfpp.utils import get_var, vec2quat

VEC = tuple[float, float, float]
QUAT = tuple[float, float, float, float]


class Point:
    def __init__(self, x: float, y: float = None, z: float = None):
        self._x = x
        self._y = get_var(y, x)
        self._z = get_var(z, x)

    def __repr__(self):
        return "<x:{} y:{} z:{}>".format(self._x, self._y, self._z)

    def as_vec(self) -> VEC:
        return float(self._x), float(self._y), float(self._z)

    def as_rot(self, _x: float = None, _z: float = None, _y: float = None) -> QUAT:
        x = get_var(_x, self._x)
        y = get_var(_y, self._y)
        z = get_var(_z, self._z)
        return vec2quat(x, z, y)

    @property
    def left_rotation(self):
        if self.x != 0:
            return self.as_rot(self.x, 0, 0)
        if self.y != 0:
            return self.as_rot(0, self.y, 0)
        if self.z != 0:
            return self.as_rot(0, 0, self.z)
        return self.as_rot()

    @property
    def right_rotation(self):
        if self.left_rotation[0] != 0:
            return self.as_rot(0, self.y, self.z)
        if self.left_rotation[1] != 0:
            return self.as_rot(self.x, 0, self.z)
        if self.left_rotation[2] != 0:
            return self.as_rot(self.x, self.y, 0)
        return Point(0).as_rot()

    @property
    def x(self):
        return self.as_vec()[0]

    @property
    def y(self):
        return self.as_vec()[1]

    @property
    def z(self):
        return self.as_vec()[2]

    @property
    def center_x(self):
        return self.x - 0.5

    @property
    def center_y(self):
        return self.y - 1

    @property
    def center_z(self):
        return self.z - 0.5


class Axis(Enum):
    X = 0
    Z = 1
    Y = 2
