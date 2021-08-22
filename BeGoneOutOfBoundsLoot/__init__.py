from typing import List

import unrealsdk

from ..ModMenu import EnabledSaveType, KeybindManager, SDKMod


def get_player_controller():
    return unrealsdk.GetEngine().GamePlayers[0].Actor


class BGOOBL(SDKMod):
    Name: str = "Be Gone Out Of Bounds Loot"
    Version: str = "1.2"
    Types = unrealsdk.ModTypes.Utility
    Description: str = "Adds a keybind option to the game that allows you to teleport all loot on the ground to your " \
                       f"current location. By default the key is binded to ENTER.\n\n{Version}"
    Author: str = "Juso"

    Keybinds: List[KeybindManager.Keybind] = [KeybindManager.Keybind("Teleport Loot To Me", Key="Enter")]
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadWithSettings

    def GameInputPressed(self, bind: KeybindManager.Keybind, event: KeybindManager.InputEvent) -> None:
        if event != KeybindManager.InputEvent.Released:
            return
        if bind.Name == "Teleport Loot To Me":
            pawn = get_player_controller().Pawn
            location = (pawn.Location.X, pawn.Location.Y, pawn.Location.Z)
            for Pickup in get_player_controller().GetWillowGlobals().PickupList:
                Pickup.Location = location
                Pickup.AdjustPickupPhysicsAndCollisionForBeingDropped()
                lst: List[float, float, float] = list(location)
                lst[2] += 10
                location = tuple(lst)

    def Enable(self):
        super().Enable()

    def Disable(self):
        super().Disable()


unrealsdk.RegisterMod(BGOOBL())
