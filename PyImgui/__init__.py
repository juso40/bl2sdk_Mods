from typing import List, Callable, Set
import threading
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
    _draw_thread = threading.Thread(target=d3d9hook, daemon=True)
    _draw_thread.start()
    _draw_thread.join()


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
