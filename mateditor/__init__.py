from typing import Sequence

from Mods import blimgui
from Mods.ModMenu import (
    EnabledSaveType,
    Keybind,
    ModPriorities,
    ModTypes,
    Options,
    RegisterMod,
    SDKMod,
)

from .ui import draw

IMGUI_SHOW: bool = False


def _toggle() -> None:
    global IMGUI_SHOW
    if IMGUI_SHOW:
        blimgui.close_window()
        IMGUI_SHOW = False
    else:
        blimgui.create_window("Material Editor")
        blimgui.set_draw_callback(draw)
        IMGUI_SHOW = True


class MaterialEditor(SDKMod):
    Name: str = "Material Editor"
    Author: str = "juso"
    Description: str = (
        "Allows you to edit MaterialInstanceConstant Objects in realtime."
    )
    Version: str = "1.3"

    Types: ModTypes = ModTypes.Utility
    Priority: int = ModPriorities.Standard
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadWithSettings

    Status: str = "Disabled"

    def __init__(self):
        self.Options: Sequence[Options.Base] = []
        self.Keybinds: Sequence[Keybind] = [
            Keybind("Open Editor", "F1", OnPress=_toggle)
        ]

    def Enable(self) -> None:  # noqa: N802
        super().Enable()

    def Disable(self) -> None:  # noqa: N802
        super().Disable()


instance = MaterialEditor()
RegisterMod(instance)
