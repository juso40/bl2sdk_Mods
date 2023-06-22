from typing import Callable

import imgui

from . import editor, inventory


def draw() -> None:
    io = imgui.get_io()
    imgui.set_next_window_size(io.display_size.x, io.display_size.y, imgui.ALWAYS)
    imgui.set_next_window_position(0, 0, imgui.ALWAYS)
    with imgui.begin(
        "Inventory Editor",
        flags=imgui.WINDOW_NO_RESIZE
        | imgui.WINDOW_NO_DECORATION
        | imgui.WINDOW_NO_COLLAPSE
        | imgui.WINDOW_NO_MOVE
        | imgui.WINDOW_NO_TITLE_BAR,
    ):
        h_space, v_space = imgui.get_content_region_available()
        with imgui.begin_child("Inventory", h_space / 2, v_space, border=True):
            call_with_title("Backpack", inventory.draw)
        imgui.same_line()
        with imgui.begin_child("Editor", h_space / 2, v_space, border=True):
            call_with_title("Editor", editor.draw)


def call_with_title(title: str, child_func: Callable[[], None]) -> None:
    """Calls the given function in a child region with a text and separator above it."""
    imgui.text(title)
    imgui.separator()
    child_func()
