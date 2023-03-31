import unrealsdk  # type: ignore

from Mods.ModMenu import Game, ModTypes, SDKMod

from .easing import (
    back_in,
    back_in_out,
    back_out,
    bounce_in,
    bounce_in_out,
    bounce_out,
    circ_in,
    circ_in_out,
    circ_out,
    cubic_in,
    cubic_in_out,
    cubic_out,
    ease,
    elastic_in,
    elastic_in_out,
    elastic_out,
    expo_in,
    expo_in_out,
    expo_out,
    linear,
    quad_in,
    quad_in_out,
    quad_out,
    quart_in,
    quart_in_out,
    quart_out,
    quint_in,
    quint_in_out,
    quint_out,
    sine_in,
    sine_in_out,
    sine_out,
)
from .tween import Tween

__all__ = [
    "Tween",
    "ease",
    "linear",
    "quad_in",
    "quad_out",
    "quad_in_out",
    "cubic_in",
    "cubic_out",
    "cubic_in_out",
    "quart_in",
    "quart_out",
    "quart_in_out",
    "quint_in",
    "quint_out",
    "quint_in_out",
    "sine_in",
    "sine_out",
    "sine_in_out",
    "expo_in",
    "expo_out",
    "expo_in_out",
    "circ_in",
    "circ_out",
    "circ_in_out",
    "back_in",
    "back_out",
    "back_in_out",
    "elastic_in",
    "elastic_out",
    "elastic_in_out",
    "bounce_in",
    "bounce_out",
    "bounce_in_out",
]

class Tweens(SDKMod):
    Name = "Tweens"
    Version = "1.0"
    Types = ModTypes.Library
    Description = "A tweening library with various easing functions."
    Author = "juso"
    Status = "Enabled"
    SettingsInputs = {}
    SupportedGames = Game.BL2 | Game.TPS | Game.TPS


unrealsdk.RegisterMod(Tweens())
