from typing import List
import unrealsdk

from ..ModMenu import EnabledSaveType, SDKMod, RegisterMod, ModTypes, KeybindManager, OptionManager, Game


class SimpleZoom(SDKMod):
    Name: str = "Simple Zoom"
    Description: str = "Allows you to zoom with a keybind."
    Author: str = "Juso"
    Types: ModTypes = ModTypes.Utility
    Version: str = "1.0"
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadOnMainMenu
    SupportedGames: Game = Game.BL2 | Game.TPS | Game.AoDK

    Keybinds: List[KeybindManager.Keybind] = [
        KeybindManager.Keybind("Zoom", "C"),
    ]

    Options: List[OptionManager.Options.Base] = [
        OptionManager.Options.Slider("Zoom FOV", "The FOV to zoom to.", 15, 1, 60, 1),
    ]

    def GameInputPressed(self, bind: KeybindManager.Keybind, event: KeybindManager.InputEvent) -> None:
        if bind.Name == "Zoom" and event == KeybindManager.InputEvent.Pressed:
            self.Zoom()
        elif bind.Name == "Zoom" and event == KeybindManager.InputEvent.Released:
            self.Unzoom()

    def Zoom(self) -> None:
        pc = unrealsdk.GetEngine().GamePlayers[0].Actor
        pc.LowerFirstPersonHands()
        pc.SetFOV(self.Options[0].CurrentValue)

    def Unzoom(self) -> None:
        pc = unrealsdk.GetEngine().GamePlayers[0].Actor
        pc.RaiseFirstPersonHands()
        pc.SetFOV(pc.DefaultFOV)


RegisterMod(SimpleZoom())
