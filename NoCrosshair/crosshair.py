from typing import Any, cast

import unrealsdk  # type: ignore

from Mods.canvaslib import Canvas, HorizontalAlign, VerticalAlign
from Mods.coroutines import PostRenderCoroutine, WaitWhile, start_coroutine_post_render
from Mods.ModMenu import Options

StaticCrosshair = Options.Boolean(
    "Static Crosshair",
    "Enable a static crosshair.",
    StartingValue=False,
)

RectSize = Options.Slider(
    "Rect Size",
    "Size of the rect.",
    StartingValue=3,
    MinValue=1,
    MaxValue=10,
    Increment=1,
)


class DefaultColor:
    ColorR = Options.Slider(
        "Red",
        "Red color value.",
        StartingValue=255,
        MinValue=0,
        MaxValue=255,
        Increment=1,
    )
    ColorG = Options.Slider(
        "Green",
        "Green color value.",
        StartingValue=255,
        MinValue=0,
        MaxValue=255,
        Increment=1,
    )
    ColorB = Options.Slider(
        "Blue",
        "Blue color value.",
        StartingValue=255,
        MinValue=0,
        MaxValue=255,
        Increment=1,
    )
    ColorA = Options.Slider(
        "Alpha",
        "Alpha color value.",
        StartingValue=255,
        MinValue=0,
        MaxValue=255,
        Increment=1,
    )
    Nested = Options.Nested(
        "Color",
        "Color of the crosshair.",
        Children=[ColorR, ColorG, ColorB, ColorA],
    )


options = [
    StaticCrosshair,
    RectSize,
    DefaultColor.Nested,
]

ENABLED: bool = False
COLOR: tuple = (255, 255, 255, 255)


def option_changed(option: Options.Base, new_value: Any) -> None:
    if option is StaticCrosshair:
        if cast(bool, new_value):
            enable()
        else:
            disable()


def enable() -> None:
    global ENABLED
    ENABLED = True
    start_coroutine_post_render(crosshair())


def disable() -> None:
    global ENABLED
    ENABLED = False


def wait_condition() -> bool:
    pc = unrealsdk.GetEngine().GamePlayers[0].Actor
    return pc.Pawn is None or pc.IsPauseMenuOpen() or pc.bStatusMenuOpen


def crosshair() -> PostRenderCoroutine:
    global COLOR
    while ENABLED:
        yield WaitWhile(wait_condition)
        c = yield
        with Canvas(c) as canvas:
            canvas.draw_rect(
                x=0.5,
                y=0.5,
                width=RectSize.CurrentValue,
                height=RectSize.CurrentValue,
                horizontal_align=HorizontalAlign.CENTER,
                vertical_align=VerticalAlign.CENTER,
                color=COLOR,
            )
