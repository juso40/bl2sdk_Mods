import unrealsdk
from unrealsdk import *

from Mods.ModMenu import Game, ModTypes, SDKMod
from .gametime import Time
from .loop import (
    PostRenderCoroutine,
    TickCoroutine,
    WaitCondition,
    WaitForSeconds,
    WaitWhile,
    WaitUntil,
    start_coroutine_post_render,
    start_coroutine_tick,
)

__all__ = [
    "Time",
    "WaitCondition",
    "WaitWhile",
    "WaitForSeconds",
    "WaitUntil",
    "TickCoroutine",
    "PostRenderCoroutine",
    "start_coroutine_tick",
    "start_coroutine_post_render",
]


class Coroutines(SDKMod):
    Name = "Coroutines"
    Version = "1.1"
    Types = ModTypes.Library
    Description = "Library that adds simple coroutine support."
    Author = "juso"
    Status = "Enabled"
    SettingsInputs = {}
    SupportedGames = Game.BL2 | Game.TPS | Game.TPS


unrealsdk.RegisterMod(Coroutines())
