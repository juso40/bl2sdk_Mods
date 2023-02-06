import math as m
from typing import List, Tuple, Union

import unrealsdk

from .constants import *
from .structs import Rotator, Vector

Vec3 = Union[Tuple[float, float, float], List[float], Vector]
Rot = Union[Tuple[int, int, int], List[int], Rotator]


def rotator_to_vector(rot: Union[Rot, unrealsdk.UObject]) -> Vec3:
    """Convert a Rotator to a Vector."""
    if isinstance(rot, (tuple, list)):
        pitch, yaw, roll = rot
    elif isinstance(rot, Rotator):
        pitch, yaw, roll = rot.pitch, rot.yaw, rot.roll
    else:
        pitch, yaw, roll = rot.Pitch, rot.Yaw, rot.Roll

    yaw_conv = yaw * URU_TO_RADIANS
    pitch_conv = pitch * URU_TO_RADIANS
    cos_pitch = m.cos(pitch_conv)
    x = m.cos(yaw_conv) * cos_pitch
    y = m.sin(yaw_conv) * cos_pitch
    z = m.sin(pitch_conv)
    return x, y, z


def vector_to_rotator(vector: Vec3) -> Rot:
    """Convert a normalized Vector to a Rotator."""
    x, y, z = vector
    pitch = m.atan2(z, m.sqrt(x * x + y * y)) * RADIANS_TO_URU
    yaw = m.atan2(y, x) * RADIANS_TO_URU
    roll = 0
    return int(pitch), int(yaw), roll


def magnitude(vector: Vec3) -> float:
    """Get the magnitude of a Vector."""
    return m.sqrt(sum(x * x for x in vector))


def normalize(vector: Vec3) -> Vec3:
    """Get the normalized Vector."""
    mag = magnitude(vector)
    if mag == 0:
        return 0, 0, 0
    x, y, z, = vector
    return x / mag, y / mag, z / mag


def distance(a: Vec3, b: Vec3) -> float:
    """Get the distance between two Vectors."""
    return magnitude((a[0] - b[0], a[1] - b[1], a[2] - b[2]))


def square_distance(a: Vec3, b: Vec3) -> float:
    """Get the squared distance between two Vectors."""
    return sum(((a - b) * (a - b) for a, b in zip(a, b)))


def look_at(actor: unrealsdk.UObject, target: Vec3) -> None:
    """Set the rotation of a transform to look at a target location."""
    bx, by, bz = target
    a = actor.Location
    look_vector = normalize((bx - a.X, by - a.Y, bz - a.Z))
    actor.Rotation = vector_to_rotator(look_vector)


def get_axes(rotation: Rot) -> Tuple[Vector, Vector, Vector]:
    """Get the axes of a Rotator."""

    pitch, yaw, roll = rotation
    x = normalize(rotator_to_vector(rotation))

    y = normalize(rotator_to_vector((0, yaw + URU_90, roll)))
    y = (y[0], y[1], 0)

    z = normalize(rotator_to_vector((pitch + URU_90, yaw - URU_90, roll)))

    return Vector(*x), Vector(*y), Vector(*z)


def world_to_screen(
        canvas: unrealsdk.UObject,
        target: Vec3,
        player_rot: Rot,
        player_loc: Vec3,
        player_fov: float
) -> Tuple[float, float]:
    axis_x, axis_y, axis_z = get_axes(player_rot)

    delta = [a - b for a, b in zip(target, player_loc)]

    transformed = (sum(a * b for a, b in zip(delta, axis_y)),
                   sum(a * b for a, b in zip(delta, axis_z)),
                   max(1.0, sum(a * b for a, b in zip(delta, axis_x))),
                   )

    fov = player_fov

    screen_center_x = canvas.ClipX / 2
    screen_center_y = canvas.ClipY / 2
    vec_2d_x = screen_center_x + transformed[0] * (screen_center_x / m.tan(fov * PI / 360.0)) / transformed[2]
    vec_2d_y = screen_center_y - transformed[1] * (screen_center_x / m.tan(fov * PI / 360.0)) / transformed[2]
    return vec_2d_x, vec_2d_y


def clamp(value: float, _min: float, _max: float) -> float:
    return _min if value < _min else _max if value > _max else value


def round_to_multiple(x: float, multiple: float) -> float:
    return multiple * round(x / multiple) if multiple != 0.0 else x


def euler_rotate_vector_2d(x: float, y: float, angle: float) -> Tuple[float, float]:
    """Rotate a 2D vector by an angle in degrees."""
    angle = angle * URU_TO_RADIANS
    s = m.sin(angle)
    c = m.cos(angle)
    x_r = x * c - y * s
    y_r = x * s + y * c
    return x_r, y_r


def dot_product(
        vec_a: Vec3,
        vec_b: Vec3,
        ignore_z: bool = True
) -> Tuple[float, float, float]:
    """Get the dot product of 2 normalized vectors."""

    xa, ya, za = vec_a
    xb, yb, zb = vec_b

    return (xa * xb + ya * yb) if ignore_z else (xa * xb + ya * yb + za * zb)
