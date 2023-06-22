from typing import Callable

import imgui

from . import editor, materials, menubar


def draw() -> None:
    with imgui.begin_main_menu_bar() as main_menu_bar:
        if main_menu_bar.opened:
            menubar.draw()
        offset = imgui.get_window_height()
    io = imgui.get_io()
    imgui.set_next_window_size(
        io.display_size.x, io.display_size.y - offset, imgui.ALWAYS
    )
    imgui.set_next_window_position(0, offset, imgui.ALWAYS)
    with imgui.begin(
        "Material Editor",
        flags=imgui.WINDOW_NO_RESIZE
        | imgui.WINDOW_NO_DECORATION
        | imgui.WINDOW_NO_COLLAPSE
        | imgui.WINDOW_NO_MOVE
        | imgui.WINDOW_NO_TITLE_BAR,
    ):
        call_with_title("Materials", materials.draw)
        imgui.separator()
        call_with_title("Editor", editor.draw)


def call_with_title(title: str, child_func: Callable[[], None]) -> None:
    """Calls the given function in a child region with a text and separator above it."""
    imgui.text(title)
    imgui.separator()
    child_func()
