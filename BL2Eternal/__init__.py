from typing import Any, List

import unrealsdk

from ..ModMenu import SDKMod, EnabledSaveType, ModTypes, Game, OptionManager

from .mechanics import dash, glory_kill

DASH_OPTION = OptionManager.Options.Boolean(Caption="Dash", Description="Enable dash.", StartingValue=True)
GLORY_KILL_OPTION = OptionManager.Options.Boolean(
    Caption="Glory Kill", Description="Enable glory kill.", StartingValue=True
)
DASH_SCREEN_PARTICLE = OptionManager.Options.Boolean(
    Caption="Dash Screen Particle", StartingValue=Game.GetCurrent() != Game.TPS,  # TPS doesn't have this
    Description="Enable the screen particle effect when dashing.", IsHidden=Game.GetCurrent() == Game.TPS
)

class Eternal(SDKMod):
    Name: str = "BL2 Eternal"
    Description: str = "Doom Eternal, but it's BL2."
    Author: str = "Juso"
    Version: str = "1.5.0"
    SupportedGames = Game.BL2 | Game.TPS | Game.AoDK
    Types: ModTypes = ModTypes.Gameplay
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadWithSettings
    Options: List[OptionManager.Options.Base] = [
        DASH_OPTION,
        GLORY_KILL_OPTION,
    ]

    def Enable(self) -> None:
        super().Enable()
        dash.enable()
        glory_kill.enable()

    def Disable(self) -> None:
        super().Disable()
        dash.disable()
        glory_kill.disable()

    def ModOptionChanged(self, option: OptionManager.Options.Base, new_value: Any) -> None:
        super().ModOptionChanged(option, new_value)
        if option is DASH_OPTION:
            if new_value:
                dash.enable()
            else:
                dash.disable()
        elif option is GLORY_KILL_OPTION:
            if new_value:
                glory_kill.enable()
            else:
                glory_kill.disable()
        elif option is DASH_SCREEN_PARTICLE:
            dash.enable_screen_particle(new_value)

unrealsdk.RegisterMod(Eternal())
