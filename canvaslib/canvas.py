from __future__ import annotations

from enum import Enum, auto
from functools import lru_cache
from typing import TYPE_CHECKING, Optional, Tuple, Type, Union

import unrealsdk  # type: ignore  # noqa: TCH002

from .fonts import FontRenderInfo

if TYPE_CHECKING:
    from types import TracebackType

BGRA = Tuple[float, float, float, float]


class HorizontalAlign(Enum):
    LEFT = auto()
    CENTER = auto()
    RIGHT = auto()


class VerticalAlign(Enum):
    TOP = auto()
    CENTER = auto()
    BOTTOM = auto()


@lru_cache(maxsize=256)
def get_aligned_pos(
    x: Union[int, float],
    y: Union[int, float],
    width: Union[int, float],
    height: Union[int, float],
    halign: HorizontalAlign,
    valign: VerticalAlign,
) -> Tuple[float, float]:
    if halign == HorizontalAlign.LEFT:
        pass
    elif halign == HorizontalAlign.CENTER:
        x -= width // 2
    elif halign == HorizontalAlign.RIGHT:
        x -= width
    else:
        raise ValueError("Invalid horizontal align")

    if valign == VerticalAlign.TOP:
        pass
    elif valign == VerticalAlign.CENTER:
        y -= height // 2
    elif valign == VerticalAlign.BOTTOM:
        y -= height
    else:
        raise ValueError("Invalid vertical align")
    return x, y


def relative_to_screen_coordinates(
    canvas: unrealsdk.UObject, x: Union[int, float], y: Union[int, float]
) -> Tuple[float, float]:
    """Converts relative coordinates to screen coordinates.

    Args:
        canvas: The canvas to use for the conversion.
        x: The relative x coordinate. Between 0 and 1.
        y: The relative y coordinate. Between 0 and 1.
    """
    return x * canvas.ClipX, y * canvas.ClipY


font_render_info: FontRenderInfo = FontRenderInfo()


class Canvas:
    """
    Context manager for drawing text on the canvas.
    Upon leaving the context, the font will be restored to the previous one.

    Example:

    >>> with Canvas(canvas) as c:
    >>>     # Draw text with the default font, centered on the screen
    >>>     c.draw_text("Hello World!", 0.5, 0.5,
    >>>                 horizontal_align=HorizontalAlign.CENTER,
    >>>                 vertical_align=VerticalAlign.CENTER)
    >>> # Draw text with a custom font, aligned to the top right corner
    >>> with Canvas(canvas, uefont=Fonts.Font_Willowbody_18pt_TWN) as c:
    >>>     c.draw_text("Hello World!", 1.0, 0.0,
     >>>                horizontal_align=HorizontalAlign.RIGHT,
    >>>                 vertical_align=VerticalAlign.TOP)
    """

    def __init__(
        self, canvas: unrealsdk.UObject, ufont: Optional[unrealsdk.UObject] = None
    ):
        self.canvas: unrealsdk.UObject = canvas
        self.font: Optional[unrealsdk.UObject] = ufont
        self.backup_font: unrealsdk.UObject = self.canvas.Font
        self.draw_color: BGRA = (0, 255, 0, 255)

    def __enter__(self) -> Canvas:
        self.canvas.Font = self.font or self.backup_font
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional["TracebackType"],
    ):
        self.canvas.Font = self.backup_font

    def text_size(
        self, text: str, scale_x: float = 1.0, scale_y: float = 1.0
    ) -> Tuple[float, float]:
        """Returns the width and height of the text in pixels."""
        x, y = self.canvas.TextSize(text)
        return x * scale_x, y * scale_y

    def set_draw_color(self, r: float, g: float, b: float, a: float) -> Canvas:
        """Sets the draw color of the Thext. Values are 0-255."""
        self.draw_color = (b, g, r, a)
        return self

    def draw_text(
        self,
        text: str,
        x: Union[int, float],
        y: Union[int, float],
        scale_x: float = 1.0,
        scale_y: float = 1.0,
        horizontal_align: HorizontalAlign = HorizontalAlign.CENTER,
        vertical_align: VerticalAlign = VerticalAlign.CENTER,
        color: Optional[BGRA] = None,
        font_render_info: FontRenderInfo = font_render_info
    ) -> Tuple[float, float]:
        """Draws text on the canvas.
        If x or y is [0.0-1.0], it will be treated as a percentage of the screen width or height.

        Returns the x and y position of the bottom right corner of the text.
        """
        canvas = self.canvas
        screen_width: int = canvas.SizeX
        screen_height: int = canvas.SizeY
        if x <= 1:
            x = screen_width * x
        if y <= 1:
            y = screen_height * y

        canvas.Font = self.font or self.backup_font
        width, height = self.text_size(text, scale_x, scale_y)
        x, y = get_aligned_pos(x, y, width, height, horizontal_align, vertical_align)
        canvas.SetDrawColorStruct(color or self.draw_color)
        canvas.SetPos(x, y)
        canvas.DrawText(text, False, scale_x, scale_y, font_render_info.as_tuple())

        return x + width, y + height

    def draw_rect(
        self,
        x: Union[int, float],
        y: Union[int, float],
        width: Union[int, float],
        height: Union[int, float],
        horizontal_align: HorizontalAlign = HorizontalAlign.LEFT,
        vertical_align: VerticalAlign = VerticalAlign.TOP,
        color: Optional[BGRA] = None,
    ) -> Tuple[float, float]:
        canvas = self.canvas
        if x <= 1:
            x = canvas.SizeX * x
        if y <= 1:
            y = canvas.SizeY * y
        if width <= 1:
            width = canvas.SizeX * width
        if height <= 1:
            height = canvas.SizeY * height
        x, y = get_aligned_pos(x, y, width, height, horizontal_align, vertical_align)
        canvas.SetDrawColorStruct(color or self.draw_color)
        canvas.SetPos(x, y)
        canvas.DrawRect(width, height, canvas.DefaultTexture)
        return x + width, y + height

    def draw_line(
        self,
        x1: Union[int, float],
        y1: Union[int, float],
        x2: Union[int, float],
        y2: Union[int, float],
        width: Union[int, float] = 1,
        color: Optional[BGRA] = None,
    ) -> None:
        canvas = self.canvas
        if x1 <= 1:
            x1 = canvas.SizeX * x1
        if y1 <= 1:
            y1 = canvas.SizeY * y1
        if x2 <= 1:
            x2 = canvas.SizeX * x2
        if y2 <= 1:
            y2 = canvas.SizeY * y2

        canvas.DrawTextureLine(
            StartPoint=(x1, y1, 0),
            EndPoint=(x2, y2, 0),
            Perc=1,
            Width=width,
            LineColor=color or self.draw_color,
            LineTexture=canvas.DefaultTexture,
            U=0,
            V=0,
            UL=1,
            VL=1,
        )
