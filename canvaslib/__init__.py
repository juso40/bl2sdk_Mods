import string
from typing import Any

import unrealsdk

from Mods.ModMenu import Game, ModTypes, Options, SDKMod
from Mods.ModMenu import OptionManager
from Mods.coroutines import PostRenderCoroutine, start_coroutine_post_render
from .canvas import Canvas, HorizontalAlign, VerticalAlign, get_aligned_pos
from .fonts import DepthFieldGlowInfo, FontRenderInfo, Fonts

__all__ = [
    "Canvas",
    "HorizontalAlign",
    "VerticalAlign",
    "get_aligned_pos",
    "DepthFieldGlowInfo",
    "FontRenderInfo",
    "Fonts",
]

show_examples = Options.Boolean("Show Examples", "Display examples of the CanvasLIB functions.", StartingValue=False)
show_fonts = Options.Boolean("Show Fonts", "Display font examples.", StartingValue=False)
show_aligns = Options.Boolean("Show Aligns", "Display examples of alignments.", StartingValue=False)
show_rects = Options.Boolean("Show Rects", "Display examples of rectangles.", StartingValue=False)

options = Options.Nested(
    "Examples", "Examples for the CanvasLIB functions.",
    Children=[show_examples, show_fonts, show_aligns, show_rects]
)

_all_fonts = [
    ("Default__Font", Fonts.Default__Font,),
    ("Default__MultiFont", Fonts.Default__MultiFont,),
    ("TinyFont", Fonts.TinyFont,),
    ("SmallFont", Fonts.SmallFont,),
    ("Font_Hud_Medium", Fonts.Font_Hud_Medium,),
    ("font_xbox18", Fonts.font_xbox18,),
    ("font_ps3", Fonts.font_ps3,),
    ("Font_Willowbody_18pt", Fonts.Font_Willowbody_18pt,),
    ("Font_Willowhead_8pt", Fonts.Font_Willowhead_8pt,),
    ("Font_Willowbody_18pt_KOR", Fonts.Font_Willowbody_18pt_KOR,),
    ("Font_Willowbody_18pt_JPN", Fonts.Font_Willowbody_18pt_JPN,),
    ("Font_Willowbody_18pt_TWN", Fonts.Font_Willowbody_18pt_TWN),
]


def _show_fonts(c: Canvas, some_text: str) -> None:
    y = 0.1
    for font_name, f in _all_fonts:
        c.font = Fonts.SmallFont
        x, _ = c.draw_text(
            f"{font_name}: ", 0, y, horizontal_align=HorizontalAlign.LEFT,
            vertical_align=VerticalAlign.TOP,
            color=(255, 255, 255, 255)
        )
        c.font = f
        y_before = y
        _, y = c.draw_text(
            some_text, x, y, horizontal_align=HorizontalAlign.LEFT, vertical_align=VerticalAlign.TOP,
            color=(255, 255, 255, 255)
        )
        if y - y_before < 30:
            y += 30


def _show_aligns(c: Canvas) -> None:
    c.font = Fonts.Font_Willowbody_18pt_KOR
    c.set_draw_color(255, 255, 0, 255)
    c.draw_text(
        "Align TOP LEFT", 0, 0, horizontal_align=HorizontalAlign.LEFT, vertical_align=VerticalAlign.TOP,
    )
    c.draw_text(
        "Align TOP CENTER", 0.5, 0, horizontal_align=HorizontalAlign.CENTER, vertical_align=VerticalAlign.TOP,
    )
    c.draw_text(
        "Align TOP RIGHT", 1, 0, horizontal_align=HorizontalAlign.RIGHT, vertical_align=VerticalAlign.TOP,
    )
    c.draw_text(
        "Align CENTER LEFT", 0, 0.5, horizontal_align=HorizontalAlign.LEFT, vertical_align=VerticalAlign.CENTER,
    )
    c.draw_text(
        "Align CENTER CENTER", 0.5, 0.5, horizontal_align=HorizontalAlign.CENTER,
        vertical_align=VerticalAlign.CENTER,
    )
    c.draw_text(
        "Align CENTER RIGHT", 1, 0.5, horizontal_align=HorizontalAlign.RIGHT,
        vertical_align=VerticalAlign.CENTER,
    )
    c.draw_text(
        "Align BOTTOM LEFT", 0, 1, horizontal_align=HorizontalAlign.LEFT, vertical_align=VerticalAlign.BOTTOM,
    )
    c.draw_text(
        "Align BOTTOM CENTER", 0.5, 1, horizontal_align=HorizontalAlign.CENTER,
        vertical_align=VerticalAlign.BOTTOM,
    )
    c.draw_text(
        "Align BOTTOM RIGHT", 1, 1, horizontal_align=HorizontalAlign.RIGHT, vertical_align=VerticalAlign.BOTTOM,
    )


def _show_rect(c: Canvas) -> None:
    c.draw_rect(
        0.4, 0.5, 0.1, 0.1, horizontal_align=HorizontalAlign.CENTER, vertical_align=VerticalAlign.CENTER,
        color=(255, 0, 0, 100)
    )
    c.draw_rect(
        0.5, 0.5, 0.2, 0.1, horizontal_align=HorizontalAlign.CENTER, vertical_align=VerticalAlign.CENTER,
        color=(0, 255, 0, 100)
    )
    c.draw_rect(
        0.6, 0.5, 0.1, 0.1, horizontal_align=HorizontalAlign.CENTER, vertical_align=VerticalAlign.CENTER,
        color=(0, 0, 255, 100)
    )


def examples_coroutine() -> PostRenderCoroutine:
    some_text = string.printable.replace("\n", "").replace("\r", "")
    while True:
        yield None
        _c = yield
        with Canvas(_c) as c:
            if show_fonts.CurrentValue is True:
                _show_fonts(c, some_text)
            if show_aligns.CurrentValue is True:
                _show_aligns(c)
            if show_rects.CurrentValue is True:
                _show_rect(c)
        if show_examples.CurrentValue is False:
            return None


class CanvasLIB(SDKMod):
    Name = "CanvasLIB"
    Version = "1.0"
    Types = ModTypes.Library
    Description = "Library for various Canvas related functions."
    Author = "juso"
    Status = "Enabled"
    SettingsInputs = {}
    SupportedGames = Game.BL2 | Game.TPS | Game.TPS
    Options = [options]

    def ModOptionChanged(self, option: OptionManager.Options.Base, new_value: Any) -> None:
        super().ModOptionChanged(option, new_value)
        if option is show_examples and new_value is True:
            start_coroutine_post_render(examples_coroutine())


unrealsdk.RegisterMod(CanvasLIB())
