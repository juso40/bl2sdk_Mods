from __future__ import annotations

import math as m
from typing import Optional, TYPE_CHECKING, Tuple, Union, cast

if TYPE_CHECKING:
    from .vectors import Vector
from ..constants import *

Rot = Union["Rotator", Tuple[int, int, int]]
Vec3 = Union["Vector", Tuple[float, float, float]]


class Rotator:
    """Wrapper Class for UE3 Rotator Structs and their math operations."""

    def __init__(self,
                 pitch: int = 0,
                 yaw: int = 0,
                 roll: int = 0,
                 ue_rotator: Optional[unrealsdk.FStruct] = None,
                 vector: Optional[Vector] = None,
                 ue_vector: Optional[unrealsdk.FStruct] = None):

        self.pitch = pitch
        self.yaw = yaw
        self.roll = roll

        if ue_rotator and vector and ue_vector:
            raise ValueError("Can only pass one of ue_rotator, vector, or ue_vector.")

        if ue_rotator:
            self.pitch = ue_rotator.Pitch
            self.yaw = ue_rotator.Yaw
            self.roll = ue_rotator.Roll
        elif vector:
            rot = vector.to_rotator()
            self.pitch = rot.pitch
            self.yaw = rot.yaw
            self.roll = rot.roll
        elif ue_vector:
            rot = Vector(ue_vector=ue_vector).to_rotator()
            self.pitch = rot.pitch
            self.yaw = rot.yaw
            self.roll = rot.roll

    def __str__(self) -> str:
        """Return a string representation of this Rotator."""
        return f"Rotator({self.pitch}, {self.yaw}, {self.roll})"

    def __repr__(self) -> str:
        """Return a string representation of this Rotator."""
        return self.__str__()

    def __bool__(self):
        """Return True if this Rotator is not (0, 0, 0)."""
        return any((self.pitch, self.yaw, self.roll))

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
        """Convert this Rotator to a Vector."""
        yaw_conv = self.yaw * URU_TO_RADIANS
        pitch_conv = self.pitch * URU_TO_RADIANS
        cos_pitch = m.cos(pitch_conv)
        x = m.cos(yaw_conv) * cos_pitch
        y = m.sin(yaw_conv) * cos_pitch
        z = m.sin(pitch_conv)
        return (x, y, z) if to_tuple else Vector(x, y, z)

    def to_tuple(self) -> Tuple[int, int, int]:
        """Return this Rotator as a tuple."""
        return self.pitch, self.yaw, self.roll

    def get_axes(self) -> Tuple[Vec3, Vec3, Vec3]:
        """Get the axes of a Rotator."""

        x = cast(Vector, self.to_vector()).normalized
        y = Vector(rotator=Rotator(0, self.yaw + URU_90, self.roll)).normalized
        y.z = 0
        z = Vector(rotator=Rotator(self.pitch + URU_90, self.yaw - URU_90, self.roll)).normalized
        return x, y, z


from .vectors import Vector  # Circular import
