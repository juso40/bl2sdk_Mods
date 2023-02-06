from __future__ import annotations

import math as m
from typing import Optional, TYPE_CHECKING, Tuple, Union

if TYPE_CHECKING:
    from .rotators import Rotator
from ..constants import *

Scalar = Union[float, int]
Rot = Union["Rotator", Tuple[int, int, int]]
Vec3 = Union["Vector", Tuple[float, float, float]]


class Vector:
    """Wrapper Class for UE3 Vector Structs and their math operations."""

    def __init__(self,
                 x: float = 0,
                 y: float = 0,
                 z: float = 0,
                 ue_vector: Optional[unrealsdk.FStruct] = None,
                 rotator: Optional[Rotator] = None,
                 ue_rotator: Optional[unrealsdk.FStruct] = None):
        """Create a new Vector object.

        :param x: Default x value of this vector.
        :param y: Default y value of this vector.
        :param z: Default z value of this vector.
        :param ue_vector: Optional, if passed, will use the values from this vector instead.
        :param rotator: Optional, if passed, will convert this rotator to a vector and use the values from it.
        :param ue_rotator:  Optional, if passed, will convert this rotator to a vector and use the values from it.
        """
        self.x = x
        self.y = y
        self.z = z

        if ue_vector and rotator and ue_rotator:
            raise ValueError("Can only pass one of ue_vector, rotator, or ue_rotator.")

        if ue_vector:
            self.x = ue_vector.X
            self.y = ue_vector.Y
            self.z = ue_vector.Z
        elif rotator:
            vec = rotator.to_vector()
            self.x = vec.x
            self.y = vec.y
            self.z = vec.z
        elif ue_rotator:
            vec = Rotator(ue_rotator=ue_rotator).to_vector()
            self.x = vec.x
            self.y = vec.y
            self.z = vec.z

    def __add__(self, other: Vec3) -> Vector:
        """Add another vector to this one."""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (list, tuple)):
            return Vector(self.x + other[0], self.y + other[1], self.z + other[2])
        else:
            raise TypeError(f"Cannot add {type(other)} to Vector.")

    def __radd__(self, other: Vec3) -> Vector:
        """Add another vector to this one."""
        return self + other

    def __sub__(self, other: Vec3) -> Vector:
        """Subtract another vector from this one."""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, (list, tuple)):
            return Vector(self.x - other[0], self.y - other[1], self.z - other[2])
        else:
            raise TypeError(f"Cannot subtract {type(other)} from Vector.")

    def __rsub__(self, other: Vec3) -> Vector:
        """Subtract this vector from another one."""
        if isinstance(other, Vector):
            return Vector(other.x - self.x, other.y - self.y, other.z - self.z)
        elif isinstance(other, (list, tuple)):
            return Vector(other[0] - self.x, other[1] - self.y, other[2] - self.z)
        else:
            raise TypeError(f"Cannot subtract Vector from {type(other)}.")

    def __mul__(self, other: Union[Scalar, Vec3]) -> Vector:
        """Multiply this vector by a scalar or do a cross product with another vector."""
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector):
            return self.cross(other)
        elif isinstance(other, (list, tuple)):
            return self.cross(Vector(*other))
        else:
            raise TypeError(f"Cannot multiply Vector by {type(other)}.")

    def __rmul__(self, other: Union[Scalar, Vec3]) -> Vector:
        """Multiply this vector by a scalar or do a cross product with another vector."""
        if isinstance(other, (float, int)):
            return self * other
        elif isinstance(other, Vector):
            return other.cross(self)
        elif isinstance(other, (list, tuple)):
            return Vector(*other).cross(self)
        else:
            raise TypeError(f"Cannot multiply Vector by {type(other)}.")

    def __truediv__(self, other: Union[float, int]) -> Vector:
        """Divide this vector by a scalar."""
        return Vector(self.x / other, self.y / other, self.z / other)

    def __rtruediv__(self, other: Union[float, int]) -> Vector:
        """Divide this vector by a scalar."""
        if isinstance(other, (float, int)):
            return self / other
        raise TypeError(f"Cannot divide {type(other)} by Vector.")

    def __eq__(self, other: Vec3) -> bool:
        """Check if this vector is equal to another."""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return self.x == other[0] and self.y == other[1] and self.z == other[2]

    def __ne__(self, other: Vec3) -> bool:
        """Check if this vector is not equal to another."""
        return not self == other

    def __str__(self) -> str:
        """Return a string representation of this vector."""
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __repr__(self) -> str:
        """Return a string representation of this vector."""
        return self.__str__()

    def __getitem__(self, item: int) -> float:
        """Return the value of this vector at the given index."""
        return (self.x, self.y, self.z)[item]

    def __setitem__(self, key: int, value: float):
        """Set the value of this vector at the given index."""
        vals = [self.x, self.y, self.z]
        vals[key] = value
        self.x, self.y, self.z = vals

    def __iter__(self):
        """Return an iterator for this vector."""
        return iter((self.x, self.y, self.z))

    def __len__(self):
        """Return the length of this vector."""
        return 3

    def __hash__(self):
        """Return a hash of this vector."""
        return hash((self.x, self.y, self.z))

    def __bool__(self):
        """Return if this vector is truthy."""
        return bool(self.x or self.y or self.z)

    def __neg__(self):
        """Return the negative of this vector."""
        return Vector(-self.x, -self.y, -self.z)

    def to_rotator(self, to_tuple=False) -> Rot:

        """Convert a normalized Vector to a Rotator."""
        pitch = m.atan2(self.z, m.sqrt(self.x * self.x + self.y * self.y)) * RADIANS_TO_URU
        yaw = m.atan2(self.y, self.x) * RADIANS_TO_URU
        roll = 0
        return (int(pitch), int(yaw), roll) if to_tuple else Rotator(int(pitch), int(yaw), roll)

    def to_tuple(self) -> Tuple[float, float, float]:
        """Return a tuple representation of this vector."""
        return self.x, self.y, self.z

    @property
    def magnitude(self) -> float:
        """Return the magnitude of this vector."""
        return m.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    @property
    def magnitude_squared(self) -> float:
        """Return the magnitude squared of this vector."""
        return self.x * self.x + self.y * self.y + self.z * self.z

    @property
    def normalized(self) -> Vector:
        """Return a normalized version of this vector."""
        mag = self.magnitude
        self.x /= mag
        self.y /= mag
        self.z /= mag
        return self

    def normalize(self) -> Vector:
        """Return a new vector that is normalized."""
        return Vector(self.x / self.magnitude, self.y / self.magnitude, self.z / self.magnitude)

    def dot(self, other: Vector) -> float:
        """Return the dot product of this vector and another."""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: Vector) -> Vector:
        """Return the cross product of this vector and another."""
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def distance(self, other: Vector) -> float:
        """Return the distance between this vector and another."""
        return (self - other).magnitude

    def distance_squared(self, other: Vector) -> float:
        """Return the distance squared between this vector and another."""
        return (self - other).magnitude_squared

    def angle(self, other: Vector) -> float:
        """Return the angle between this vector and another."""
        return m.acos(self.normalized.dot(other.normalized)) * RADIANS_TO_URU

    def rotate_towards(self, target: Vector, max_rotation_delta: float = 360) -> Vector:
        """Rotate this vector towards another vector by a maximum amount per step.

        :param target: The target vector to rotate towards.
        :param max_rotation_delta: The maximum angle in radians allowed for this rotation.
        """
        angle = self.angle(target)
        if angle == 0:
            return self
        return self.rotate(self.cross(target).normalized, min(angle, max_rotation_delta))

    def rotate(self, axis: Vector, angle: float) -> Vector:
        """Rotate this vector around an axis by an angle.

        :param axis: The axis to rotate around.
        :param angle: The angle to rotate by.
        """
        axis = axis.normalized
        sin = m.sin(angle * URU_TO_RADIANS)
        cos = m.cos(angle * URU_TO_RADIANS)
        return self * cos + axis.cross(self) * sin + axis * axis.dot(self) * (1 - cos)

    def lerp(self, other: Vector, alpha: float) -> Vector:
        """Return a linear interpolation between this vector and another.

        :param other: The other vector to interpolate towards.
        :param alpha: The amount to interpolate by.
        """
        return self + (other - self) * alpha


from .rotators import Rotator
