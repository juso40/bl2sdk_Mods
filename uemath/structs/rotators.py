from __future__ import annotations

import math as m
from typing import List, Optional, TYPE_CHECKING, Tuple, Union, cast

import unrealsdk

if TYPE_CHECKING:
    from .vectors import Vector
from Mods.uemath.constants import *

UERotator = unrealsdk.FStruct
UEVector = unrealsdk.FStruct
Sequence3Int = Union[Tuple[int, int, int], List[int]]
Rot = Union["Rotator", Tuple[int, int, int]]
Vec3 = Union["Vector", Tuple[float, float, float]]


# https://beyondunrealwiki.github.io/pages/rotator.html
class Rotator:
    """Wrapper Class for UE3 Rotator Structs and their math operations."""

    def __init__(
            self,
            data: Optional[Union[UERotator, UEVector, "Vector", Sequence3Int]] = None,
            *,
            pitch: Optional[int] = None,
            yaw: Optional[int] = None,
            roll: Optional[int] = None
    ):
        """Initialize a Rotator from a sequence of 3 int, or from a UE3 Rotator or Vector.

        :param data: A sequence of 3 int, or a UE3 Rotator or Vector. If data is a Vector it will be converted to a
        Rotator, this loses Roll information.
        :param pitch: The pitch of this Rotator. Will overwrite the pitch of the data if provided.
        :param yaw: The yaw of this Rotator. Will overwrite the yaw of the data if provided.
        :param roll: The roll of this Rotator. Will overwrite the roll of the data if provided.
        """

        self.pitch = 0
        self.yaw = 0
        self.roll = 0

        if data is not None:
            if isinstance(data, (list, tuple)):
                self.pitch, self.yaw, self.roll = data
            elif isinstance(data, Vector):
                rot = data.to_rotator()
                self.pitch = rot.pitch
                self.yaw = rot.yaw
                self.roll = rot.roll
            elif isinstance(data, Rotator):
                self.pitch = data.pitch
                self.yaw = data.yaw
                self.roll = data.roll
            elif cast(UERotator, data).Pitch is not None:
                data = cast(UERotator, data)
                self.pitch = data.Pitch
                self.yaw = data.Yaw
                self.roll = data.Roll
            elif cast(UEVector, data).X is not None:
                rot = Vector(data).to_rotator()
                self.pitch = rot.pitch
                self.yaw = rot.yaw
                self.roll = rot.roll
        if pitch is not None:
            self.pitch = pitch
        if yaw is not None:
            self.yaw = yaw
        if roll is not None:
            self.roll = roll

    def __str__(self) -> str:
        """Return a string representation of this Rotator."""
        return f"Rotator({self.pitch}, {self.yaw}, {self.roll})"

    def __repr__(self) -> str:
        """Return a string representation of this Rotator."""
        return self.__str__()

    def __bool__(self):
        """Return True if this Rotator is not (0, 0, 0)."""
        return any((self.pitch, self.yaw, self.roll))

    def __add__(self, other: Rot) -> Rotator:
        """Add another Rotator to this one."""
        if isinstance(other, Rotator):
            return Rotator((self.pitch + other.pitch, self.yaw + other.yaw, self.roll + other.roll))
        elif isinstance(other, (list, tuple)):
            return Rotator((self.pitch + other[0], self.yaw + other[1], self.roll + other[2]))
        raise TypeError(f"Cannot add Rotator and {type(other)}")

    def __sub__(self, other: Rot) -> Rotator:
        """Subtract another Rotator from this one."""
        if isinstance(other, Rotator):
            return Rotator((self.pitch - other.pitch, self.yaw - other.yaw, self.roll - other.roll))
        elif isinstance(other, (list, tuple)):
            return Rotator((self.pitch - other[0], self.yaw - other[1], self.roll - other[2]))
        raise TypeError(f"Cannot subtract Rotator and {type(other)}")

    def __eq__(self, other: Rot) -> bool:
        """Return True if this Rotator is equal to another."""
        if isinstance(other, Rotator):
            return self.pitch == other.pitch and self.yaw == other.yaw and self.roll == other.roll
        elif isinstance(other, (list, tuple)):
            return self.pitch == other[0] and self.yaw == other[1] and self.roll == other[2]
        return False

    def __ne__(self, other: Rot) -> bool:
        """Return True if this Rotator is not equal to another."""
        return not self.__eq__(other)

    def to_vector(self, to_tuple: bool = False) -> Vec3:
        """Convert this Rotator to a Vector.

        Rotation will be converted to forward vector.
        """
        yaw_conv = self.yaw * URU_TO_RADIANS
        pitch_conv = self.pitch * URU_TO_RADIANS
        cos_pitch = m.cos(pitch_conv)
        x = m.cos(yaw_conv) * cos_pitch
        y = m.sin(yaw_conv) * cos_pitch
        z = m.sin(pitch_conv)

        tup = (x, y, z)
        return tup if to_tuple else Vector(tup)

    def to_tuple(self) -> Tuple[int, int, int]:
        """Return this Rotator as a tuple."""
        return int(self.pitch), int(self.yaw), int(self.roll)

    def get_axes(self) -> Tuple[Vec3, Vec3, Vec3]:
        """Get the axes of a Rotator.

        The axes describe the forward, right and up vectors of this Rotator.
        """

        x = cast(Vector, self.to_vector()).normalize()
        y = Vector(Rotator((0, self.yaw + URU_90, self.roll))).normalize()
        y.z = 0
        z = Vector(Rotator((self.pitch + URU_90, self.yaw, self.roll))).normalize()
        return x, y, z

    @staticmethod
    def from_axes(x: Vec3, y: Vec3, z: Vec3) -> "Rotator":
        """Create a Rotator from given orthogonal axes.
        Example input:
            x = (1, 0, 0)
            y = (0, 1, 0)
            z = (0, 0, 1)
            -> Rotator((0, 0, 0))
            x = (0, 0, 1)
            y = (0, 1, 0)
            z = (-1, 0, 0)
            -> Rotator((16384, 0, 0))
        """
        x = Vector(x)
        y = Vector(y)
        z = Vector(z)
        x.normalize()
        y.normalize()
        z.normalize()
        pitch = -int(m.asin(z.y) * RADIANS_TO_URU)
        roll = -int(m.atan2(z.x, z.z) * RADIANS_TO_URU)
        yaw = -int(m.atan2(y.x, x.x) * RADIANS_TO_URU)
        return Rotator((pitch, yaw, roll))

    def look_at(self, target: Vector) -> "Rotator":
        """Get the Rotator needed to look at a target Global Location."""
        target = target - self.to_vector()
        return target.to_rotator()


from .vectors import Vector  # Circular import
