from typing import Callable, Set
import traceback

import unrealsdk

from ..ModMenu import *

try:
    # only for my IDE to add auto completion.
    import pyd_imgui
except ImportError:
    from . import pyd_imgui

__all__ = [
    "pyd_imgui",
    "toggle_cursor",
    "toggle_gui",
    "subscribe_end_scene",
    "unsubscribe_end_scene"
]

_on_end_scene: Set[Callable[[], None]] = set()

_d3d9_success: bool = False
_enabled: bool = False


def d3d9hook() -> None:
    global _d3d9_success
    if not pyd_imgui.d3d9_hook_init(end_scene_callback):
        unrealsdk.Log("[PyImgui] Could not initialize D3D9 Hook!")
        _d3d9_success = False
    _d3d9_success = True


def end_scene_callback() -> None:
    # noinspection PyBroadException
    try:
        for func in _on_end_scene:
            func()
    except Exception:
        # call new_frame to override the current draw stack
        pyd_imgui.new_frame()
        # instead show the error message
        pyd_imgui.begin("An Exception occured!", flags=pyd_imgui.WINDOW_FLAGS_ALWAYS_AUTO_RESIZE)
        pyd_imgui.text("[PyImgui] An exception was raised in drawthread!")
        pyd_imgui.text("Please fix the error before continuing using this mod!")
        pyd_imgui.text("Full traceback:")
        pyd_imgui.separator()
        pyd_imgui.text_unformatted(traceback.format_exc())
        pyd_imgui.end()
        pyd_imgui.end_frame()

        unrealsdk.Log(f"[PyImgui] An exception was raised in drawthread! Game might crash now.")
        unrealsdk.Log(traceback.format_exc())


def toggle_cursor() -> bool:
    """
    Toggle the input handler between game and imgui.

    :return: True if imgui handles input, False if game handles input.
    """
    ret = pyd_imgui.toggle_wnd_proc()
    unrealsdk.GetEngine().GamePlayers[0].Actor.IgnoreLookInput(ret)
    return ret


def toggle_gui() -> bool:
    """
    Toggle the callback to python from rendering thread.

    :return: True if python will be called on endScene, else false.
    """
    return pyd_imgui.toggle_imgui()


def subscribe_end_scene(func: Callable[[None], None]) -> None:
    """
    Add a function that should be called each d3d9 EndScene call.

    :param func: The function that should be called each EndScene call.
    :return:
    """
    _on_end_scene.add(func)


def unsubscribe_end_scene(func: Callable[[None], None]) -> None:
    """
    Remove a function from the list of functions that should be called each d3d9 EndScene call.

    :param func: The function you don't want to be called in EndScene.
    :return:
    """
    if func in _on_end_scene:
        _on_end_scene.remove(func)


if not _enabled:
    _enabled = True
    d3d9hook()


class GUI(SDKMod):
    global _d3d9_success
    # Dummy Class to show that this library is loaded.
    Name = "PyImgui"
    Author = "Juso"
    Version = pyd_imgui.__version__
    Description = "A library with pybinds for Imgui."

    Types = ModTypes.Library
    Priority = ModPriorities.Library
    SupportedGames = Game.BL2 | Game.TPS
    SettingsInputs = {}

    Status = "Enabled" if _d3d9_success else "Error"


unrealsdk.RegisterMod(GUI())

if not _d3d9_success:
    Exception("Something went wrong while hooking DX9!")
