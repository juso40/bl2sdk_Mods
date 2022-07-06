import unrealsdk

from ..ModMenu import SDKMod, EnabledSaveType, ModTypes, Game

from .mechanics import dash, glory_kill


class Eternal(SDKMod):
    Name: str = "BL2 Eternal"
    Description: str = "Doom Eternal, but it's BL2."
    Author: str = "Juso"
    Version: str = "1.2"
    SupportedGames = Game.BL2
    Types: ModTypes = ModTypes.Gameplay
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadWithSettings

    def Enable(self) -> None:
        super().Enable()
        dash.enable()
        glory_kill.enable()

    def Disable(self) -> None:
        super().Disable()
        dash.disable()
        glory_kill.disable()


unrealsdk.RegisterMod(Eternal())
