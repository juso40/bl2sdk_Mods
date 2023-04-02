from typing import Any

import unrealsdk  # type: ignore

from Mods.coroutines import start_coroutine_post_render
from Mods.ModMenu import Game, ModTypes, OptionManager, SDKMod

from .canvas import (
    Canvas,
    HorizontalAlign,
    VerticalAlign,
    get_aligned_pos,
    relative_to_screen_coordinates,
)
from .examples import examples_coroutine, options, show_examples
from .fonts import DepthFieldGlowInfo, FontRenderInfo, Fonts

__all__ = [
    "Canvas",
    "HorizontalAlign",
    "VerticalAlign",
    "get_aligned_pos",
    "DepthFieldGlowInfo",
    "FontRenderInfo",
    "Fonts",
    "relative_to_screen_coordinates",
]


class CanvasLIB(SDKMod):
    Name = "CanvasLIB"
    Version = "1.1"
    Types = ModTypes.Library
    Description = "Library for various Canvas related functions."
    Author = "juso"
    Status = "Enabled"
    SupportedGames = Game.BL2 | Game.TPS | Game.TPS
    Options = [options]

    def ModOptionChanged(  # noqa: N802
        self, option: OptionManager.Options.Base, new_value: Any
    ) -> None:
        super().ModOptionChanged(option, new_value)
        if option is show_examples and new_value is True:
            start_coroutine_post_render(examples_coroutine())


unrealsdk.RegisterMod(CanvasLIB())
