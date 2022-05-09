from typing import List

import unrealsdk

from ..ModMenu import EnabledSaveType, SDKMod, RegisterMod, ModTypes, KeybindManager, OptionManager, Game, Hook


class MissionQuickswitcher(SDKMod):
    Name: str = "MissionQuickswitcher"
    Description: str = "Allows you to quickly switch between missions with a keybind."
    Author: str = "Juso"
    Types: ModTypes = ModTypes.Utility
    Version: str = "1.0"
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadOnMainMenu
    SupportedGames: Game = Game.BL2 | Game.TPS | Game.AoDK

    Keybinds: List[KeybindManager.Keybind] = [
        KeybindManager.Keybind("Next Mission", "Up"),
        KeybindManager.Keybind("Previous Mission", "Down"),
    ]

    def GameInputPressed(self, bind: KeybindManager.Keybind, event: KeybindManager.InputEvent) -> None:
        if event != KeybindManager.InputEvent.Released:
            return
        if bind.Name == "Next Mission":
            self.ChangeActiveMission(1)
        elif bind.Name == "Previous Mission":
            self.ChangeActiveMission(-1)

    @staticmethod
    def ChangeActiveMission(change: int) -> None:
        mission_tracker: unrealsdk.UObject = unrealsdk.GetEngine().GetCurrentWorldInfo().GRI.MissionTracker
        if mission_tracker is None:
            return
        active_missions: List[unrealsdk.UObject] = [q.MissionDef for q in mission_tracker.MissionList if
                                                    q.Status in (1, 3, 5)]
        active_index: int = active_missions.index(mission_tracker.ActiveMission)
        active_index = (active_index + change) % len(active_missions)
        mission_tracker.SetActiveMission(active_missions[active_index])


RegisterMod(MissionQuickswitcher())
