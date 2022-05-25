from typing import List, Union, Tuple
from math import sin, cos, sqrt

import unrealsdk

from ..ModMenu import EnabledSaveType, KeybindManager, SDKMod


def get_player_controller():
    return unrealsdk.GetEngine().GamePlayers[0].Actor


u_rotation_180 = 32768
u_rotation_90 = u_rotation_180 / 2
u_pi = 3.1415926
u_conversion = u_pi / u_rotation_180


def rot_to_vec3d(rotation: List[int]) -> List[float]:
    """Takes UE3 Rotation as List, returns List of normalized vector."""
    f_yaw = rotation[1] * u_conversion
    f_pitch = rotation[0] * u_conversion
    cos_pitch = cos(f_pitch)
    x = cos(f_yaw) * cos_pitch
    y = sin(f_yaw) * cos_pitch
    z = sin(f_pitch)
    return [x, y, z]


def normalize_vec(vector: Union[List[float], Tuple[float, float, float]]) -> List[float]:
    _len = sqrt(sum(x * x for x in vector))
    return [x / _len for x in vector]


class BGOOBL(SDKMod):
    Name: str = "Be Gone Out Of Bounds Loot"
    Version: str = "2.0"
    Types = unrealsdk.ModTypes.Utility
    Description: str = "Adds a keybind option to the game that allows you to teleport all" \
                       " loot on the ground to your current location. By default the key is binded to ENTER."
    Author: str = "Juso"

    Keybinds: List[KeybindManager.Keybind] = [KeybindManager.Keybind("Teleport Loot To Me", Key="Enter")]
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadWithSettings

    def GameInputPressed(self, bind: KeybindManager.Keybind, event: KeybindManager.InputEvent) -> None:
        if event != KeybindManager.InputEvent.Released:
            return
        if bind.Name == "Teleport Loot To Me":
            pc = get_player_controller()
            pawn = pc.Pawn

            px, py, pz = pawn.Location.X, pawn.Location.Y, pawn.Location.Z
            x, y, z = rot_to_vec3d(
                [
                    pc.CalcViewRotation.Pitch,
                    pc.CalcViewRotation.Yaw,
                    pc.CalcViewRotation.Roll
                ]
            )
            x, y, z = normalize_vec([x, y, 0])

            valid_loot = [
                pickup for pickup in get_player_controller().GetWillowGlobals().PickupList
                if pickup.Inventory.Class != unrealsdk.FindClass("WillowMissionItem")
            ]

            loot_by_rarity = {}
            for loot in valid_loot:
                if loot.Inventory.RarityLevel not in loot_by_rarity:
                    loot_by_rarity[loot.Inventory.RarityLevel] = []
                loot_by_rarity[loot.Inventory.RarityLevel].append(loot)

            for i, loot in enumerate(loot_by_rarity.values()):
                z = pz
                for l in loot:
                    # l.ConvertRigidBodyToFixed()
                    l.Location = (px + 50 * x * i, py + 50 * y * i, pz)
                    l.AdjustPickupPhysicsAndCollisionForBeingDropped()
                    z += 30

    def Enable(self):
        super().Enable()

    def Disable(self):
        super().Disable()


unrealsdk.RegisterMod(BGOOBL())
