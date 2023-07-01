from typing import Sequence

import unrealsdk  # type: ignore

from Mods import blimgui
from Mods.ModMenu import (
    EnabledSaveType,
    Hook,
    Keybind,
    ModPriorities,
    ModTypes,
    RegisterMod,
    SDKMod,
)

from .backpack import player_inventory
from .ui import draw

IMGUI_SHOW: bool = False


def _toggle() -> None:
    global IMGUI_SHOW
    if IMGUI_SHOW:
        blimgui.close_window()
        IMGUI_SHOW = False
    else:
        blimgui.create_window("Inventory Editor")
        blimgui.set_draw_callback(draw)
        IMGUI_SHOW = True


class InventoryEditor(SDKMod):
    Name: str = "Inventory Editor"
    Author: str = "juso"
    Description: str = (
        "Allows you to edit/add/remove items in your Inventory while ingame."
    )
    Version: str = "1.7"

    Types: ModTypes = ModTypes.Utility
    Priority: int = ModPriorities.Standard
    SaveEnabledState: EnabledSaveType = EnabledSaveType.NotSaved

    def __init__(self):
        self.Keybinds: Sequence[Keybind] = [
            Keybind("Open Editor", "F1", OnPress=_toggle)
        ]

    @Hook("WillowGame.WillowPlayerController.ShowStatusMenu")
    def on_show_status_menu(
        self,
        caller: unrealsdk.UObject,
        function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ) -> bool:
        """Resets the cached inventory data upon opening the players status menu as he might drop items."""
        player_inventory.update()
        return True

    @Hook("WillowGame.WillowPlayerController.WillowClientShowLoadingMovie")
    def on_start_load(
        self,
        caller: unrealsdk.UObject,
        function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ) -> bool:
        """Disable the inventory editor when loading a new map in case the user forgot to close it."""
        if params.MovieName is None:
            return True
        global IMGUI_SHOW
        if IMGUI_SHOW:
            _toggle()
        player_inventory.reset()
        return True

    @Hook("WillowGame.WillowPlayerController.WillowClientDisableLoadingMovie")
    def on_end_load(
        self,
        caller: unrealsdk.UObject,
        function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ) -> bool:
        """Update the cached inventory data upon loading a new map."""
        player_inventory.update()
        return True


instance = InventoryEditor()
RegisterMod(instance)
