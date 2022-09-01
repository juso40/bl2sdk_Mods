from typing import Any

from ..ModMenu import ModPriorities, ModTypes, RegisterMod, SDKMod, Options, EnabledSaveType, Hook

import unrealsdk


def rcon(cmd: str) -> None:
    pc = unrealsdk.GetEngine().GamePlayers[0].Actor
    pc.RCon(cmd)


class FPSSlider(SDKMod):
    Name: str = "FPS Slider"
    Author: str = "juso"
    Description: str = (
        "Adds two custom sliders to the game's FPS slider. "
        "One for the game's min FPS and one for the game's max FPS.\n"
        "Check the mod settings menu."
    )
    Version: str = "1.0"

    Types: ModTypes = ModTypes.Utility
    Priority = ModPriorities.Standard
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadWithSettings

    MinFPSSlider = Options.Slider(
        Caption="Min FPS",
        Description="Set the game's min FPS.",
        StartingValue=60,
        MinValue=24,
        MaxValue=360,
        Increment=1
    )

    MaxFPSSlider = Options.Slider(
        Caption="Max FPS",
        Description="Set the game's max FPS.",
        StartingValue=60,
        MinValue=24,
        MaxValue=360,
        Increment=1
    )
    Options = [MinFPSSlider, MaxFPSSlider]

    def Enable(self) -> None:
        super().Enable()

    def Disable(self) -> None:
        super().Disable()
        rcon("set Engine MaxSmoothedFrameRate 62")
        rcon("set Engine MinSmoothedFrameRate 22")

    def ModOptionChanged(self, option, new_value: Any) -> None:
        self.update_fps()

    def update_fps(self) -> None:
        rcon("SCALE SET FramerateLocking 0")
        rcon(f"set Engine MaxSmoothedFrameRate {self.MaxFPSSlider.CurrentValue}")
        rcon(f"set Engine MinSmoothedFrameRate {self.MinFPSSlider.CurrentValue}")

    @Hook("WillowGame.WillowHUD.CreateWeaponScopeMovie")
    def _map_load(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
        self.update_fps()
        return True


RegisterMod(FPSSlider())
