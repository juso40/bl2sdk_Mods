import unrealsdk
from unrealsdk import *

from .structs import Rotator, Vector
from .umath import (clamp, distance, dot_product, euler_rotate_vector_2d, get_axes, look_at, magnitude, normalize,
                    rotator_to_vector, round_to_multiple, square_distance, vector_to_rotator, world_to_screen)
from ..ModMenu import ModTypes, SDKMod, Game

__all__ = [
    "Vector",
    "Rotator",
    "look_at",
    "world_to_screen",
    "clamp",
    "round_to_multiple",
    "euler_rotate_vector_2d",
    "rotator_to_vector",
    "vector_to_rotator",
    "normalize",
    "magnitude",
    "distance",
    "dot_product",
    "square_distance",
    "get_axes",
]


# https://docs.unrealengine.com/udk/Two/CoreUnrealScriptObjects.html#Structures
# https://wiki.beyondunreal.com/Legacy%3aUnrealScript_Vector_Maths


class UEMath(SDKMod):
    Name = "UEMath Library"
    Version = "1.0"
    Types = ModTypes.Library
    Description = "Math library with wrapper functions for UE Rotator and Vector operations."
    Author = "Juso"
    Status = "Enabled"
    SettingsInputs = {}
    SupportedGames = Game.BL2 | Game.TPS | Game.TPS


unrealsdk.RegisterMod(UEMath)
