import site
from typing import Callable

import unrealsdk

from ..ModMenu import EnabledSaveType, ModPriorities, ModTypes, RegisterMod, SDKMod

site.addsitedir("Mods/blimgui/dist")

__version__ = "0.1.0"

import pyglet
from pyglet import gl
import imgui
from imgui.integrations.pyglet import create_renderer

DRAW_FUN = Callable[[], None]

WINDOW = None
IMPL = None


def create_window(
        caption: str,
        width: int = 1280,
        height: int = 720,
        resizable: bool = True
) -> None:
    """
    Create a new window with the given parameters. If a window already exists, rename only.

    :param caption: The caption of the window
    :param width: The width of the window
    :param height: The height of the window
    :param resizable: If True, window is resizable, else cannot be resized.
    :return: None
    """
    global WINDOW
    global IMPL
    if not WINDOW and not IMPL:
        gl.glClearColor(1, 1, 1, 1)
        imgui.create_context()
        WINDOW = pyglet.window.Window(width=width, height=height, resizable=resizable, caption=caption)
        IMPL = create_renderer(WINDOW)
    elif WINDOW:
        WINDOW.set_caption(caption=caption)


def close_window() -> bool:
    """
    Close the current window if any is open.

    :return: Bool, True if window successfully closed, else False
    """
    global WINDOW
    global IMPL
    global ACTIVE_CALLBACK
    try:

        IMPL.shutdown()
        WINDOW.close()

        WINDOW = None
        IMPL = None
        ACTIVE_CALLBACK = update
        return True
    except Exception as e:
        unrealsdk.Log(e)
        return False


def update() -> None:
    if imgui.begin_main_menu_bar():
        if imgui.begin_menu("File", True):

            clicked_quit, selected_quit = imgui.menu_item(
                "Quit", "Cmd+Q", False, True
            )
            if clicked_quit:
                close_window()
            imgui.end_menu()
        imgui.end_main_menu_bar()

    imgui.begin("Hello World", True)
    imgui.text("This is a text!")
    imgui.text_colored("Colored Text, wow!", 0.2, 1., 0.)

    imgui.end()


def draw() -> None:
    """
    Calls the currently active callback function to update the rendered content in the new window.

    :return: None
    """
    if not WINDOW:
        return
    imgui.new_frame()
    ACTIVE_CALLBACK()
    WINDOW.clear()
    imgui.render()
    IMPL.render(imgui.get_draw_data())


ACTIVE_CALLBACK = update


def set_draw_callback(callback: DRAW_FUN) -> None:
    """
    Set the given callable as active callback each draw tick.

    :param callback: Reference to the callable.
    :return: None
    """
    global ACTIVE_CALLBACK
    ACTIVE_CALLBACK = callback


def _OnTick(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
    draw()
    for w in pyglet.app.windows:
        w.switch_to()
        w.dispatch_events()
        w.dispatch_event("on_draw")
        w.flip()
    return True


unrealsdk.RunHook("WillowGame.WillowGameViewportClient.Tick", "WindowTick", _OnTick)


class BLImgui(SDKMod):
    Name = "BLImgui"
    Author = "Juso"
    Description = "A library that allows the creation of a separate window with imgui support."
    Version = __version__

    Types = ModTypes.Library
    SaveEnabledState = EnabledSaveType.LoadWithSettings
    Priority = ModPriorities.Library
    Status = "Enabled"


instance = BLImgui()
RegisterMod(instance)
