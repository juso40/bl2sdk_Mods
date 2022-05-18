from typing import Any
from enum import IntEnum

import os
import re
import json

import unrealsdk

from ..ModMenu import EnabledSaveType, SDKMod, Hook, Game, OptionManager


class ERadarIconType(IntEnum):
    RadarIconType_None = 0
    RadarIconType_Gunfire = 1
    RadarIconType_Threat = 2
    RadarIconType_BountyBoard = 3
    RadarIconType_Shop = 4
    RadarIconType_Health = 5
    RadarIconType_NewU = 6
    RadarIconType_CatchARide = 7
    RadarIconType_Settlement = 8
    RadarIconType_MissionNPC = 9
    RadarIconType_NamedNPC = 10
    RadarIconType_Loot = 11
    RadarIconType_Objective = 12
    RadarIconType_Checkpoint = 13
    RadarIconType_TravelStation = 14
    RadarIconType_CustomizationStation = 15
    RadarIconType_LevelTransition = 16


working_icons = {
    "Shop": ERadarIconType.RadarIconType_Shop,
    "Health": ERadarIconType.RadarIconType_Health,
    "Catch a Ride": ERadarIconType.RadarIconType_CatchARide,
    "Travel Station": ERadarIconType.RadarIconType_TravelStation,
    "Customization Station": ERadarIconType.RadarIconType_CustomizationStation,
    "Level Transition": ERadarIconType.RadarIconType_LevelTransition,
}

name_to_event = {
    Game.TPS: {
        "Coop-Ding": "Ake_UI.UI_HUD_Audio.Ak_Play_UI_Alert_CoOp_Ding",
        "Coop-Buddy Down": "Ake_UI.UI_HUD_Audio.Ak_Play_UI_Alert_CoOp_Buddy_Down",
        "Challenge Completed": "Ake_UI.UI_HUD_Audio.Ak_Play_UI_HUD_Challenge_Completed",
        "New Skin Unlocked": "Ake_UI.UI_HUD_Audio.Ak_Play_UI_HUD_New_Skin_Unlocked",
        "Token Unlocked": "Ake_UI.UI_HUD_Audio.Ak_Play_UI_HUD_Token_Unlocked",
        "PVP Duel End": "Ake_UI.UI_HUD_Audio.Ak_Play_UI_PVP_Duel_End",
        "PVP Duel Start": "Ake_UI.UI_HUD_Audio.Ak_Play_UI_PVP_Duel_Start",
        "Mission Reward": "Ake_UI.UI_Mission.Ak_Play_UI_Mission_Reward",
    },
    Game.BL2: {
        "Coop-Ding": "Ake_UI.UI_HUD.Ak_Play_UI_Alert_CoOp_Ding",
        "Coop-Buddy Down": "Ake_UI.UI_HUD.Ak_Play_UI_Alert_CoOp_Buddy_Down",
        "Challenge Completed": "Ake_UI.UI_HUD.Ak_Play_UI_HUD_Challenge_Completed",
        "New Skin Unlocked": "Ake_UI.UI_HUD.Ak_Play_UI_HUD_New_Skin_Unlocked",
        "Token Unlocked": "Ake_UI.UI_HUD.Ak_Play_UI_HUD_Token_Unlocked",
        "PVP Duel End": "Ake_UI.UI_HUD.Ak_Play_UI_PVP_Duel_End",
        "PVP Duel Start": "Ake_UI.UI_HUD.Ak_Play_UI_PVP_Duel_Start",
        "Mission Reward": "Ake_UI.UI_Mission.Ak_Play_UI_Mission_Reward",
    }
}


def get_pc():
    return unrealsdk.GetEngine().GamePlayers[0].Actor


def spawn_dummy_object(io_def: unrealsdk.UObject, loc: tuple) -> unrealsdk.UObject:
    pop_master: unrealsdk.UObject = unrealsdk.FindAll("WillowPopulationMaster")[-1]

    iobject: unrealsdk.UObject = pop_master.SpawnPopulationControlledActor(
        io_def.InteractiveObjectClass, None, "", loc, (0, 0, 0)
    )

    iobject.SetGameStage(1)
    iobject.SetExpLevel(1)
    iobject.InitializeFromDefinition(io_def, False)

    return iobject


game_to_str = {
    Game.BL2: "BL2",
    Game.TPS: "TPS",
    Game.AoDK: "AoDK"
}


class LootMarker(SDKMod):
    Name = "Loot Marker"
    Description = "Places markers on the map for specific loot."
    Author = "Juso"
    Version = "1.2"
    SaveEnabledState = EnabledSaveType.LoadWithSettings
    SupportedGames = Game.TPS | Game.BL2

    def __init__(self):
        super(LootMarker, self).__init__()
        self.name_to_io_def = {}
        self.path_name_to_willow_io = {}
        self.enable_spawn_sound = True
        self.player_drop_sound = False
        self.ak_event = None
        self.marker_type: int = int(ERadarIconType.RadarIconType_CustomizationStation)

        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "rarities.json"), "r") as f:
            self.rarity_configs = json.load(f)

        self.Options = [
            OptionManager.Options.Spinner(
                "Compatibility Mode",
                f"Enable compatibility with a given mod.",
                StartingValue="Exodus",
                Choices=list(self.rarity_configs[game_to_str[Game.GetCurrent()]].keys())
            ),
            OptionManager.Options.Boolean(
                "Enable Spawn Sound",
                "Play a sound when a unique item is spawned.",
                StartingValue=True
            ),
            OptionManager.Options.Boolean(
                "Enable Player Dropped Sound",
                "Play a sound when a legendary was dropped by the player.",
                StartingValue=False
            ),
            OptionManager.Options.Spinner(
                "Sound Event",
                "Change the sound that should play when a legendary spawns.",
                StartingValue="Coop-Ding",
                Choices=list(name_to_event[Game.GetCurrent()].keys()),
            ),
            OptionManager.Options.Spinner(
                "Marker Type",
                "Change the marker on the map for the Loot.",
                StartingValue="Customization Station",
                Choices=list(working_icons.keys()),
            )

        ]
        self.selected_config = self.rarity_configs[game_to_str[Game.GetCurrent()]]["Exodus"]

    def Enable(self):
        self.ak_event = unrealsdk.FindObject("AkEvent", name_to_event[Game.GetCurrent()]["Coop-Ding"])
        super().Enable()

    def Disable(self):
        super().Disable()

    def ModOptionChanged(self, option: OptionManager.Options.Base, new_value: Any) -> None:
        if option.Caption == "Compatibility Mode":
            self.selected_config = self.rarity_configs[game_to_str[Game.GetCurrent()]][new_value]
            # Config has changed, clear up wrong waypoints
            for willow_io in self.path_name_to_willow_io.values():
                willow_io.Destroyed()
            self.path_name_to_willow_io.clear()
        elif option.Caption == "Enable Spawn Sound":
            self.enable_spawn_sound = new_value
        elif option.Caption == "Enable Player Dropped Sound":
            self.player_drop_sound = new_value
        elif option.Caption == "Sound Event":
            self.ak_event = unrealsdk.FindObject("AkEvent", name_to_event[Game.GetCurrent()][new_value])
            if unrealsdk.GetEngine().GetCurrentWorldInfo().GetStreamingPersistentMapName().lower() != "menumap":
                unrealsdk.GetEngine().GamePlayers[0].Actor.PlayAkEvent(self.ak_event)
        elif option.Caption == "Marker Type":
            self.marker_type = int(working_icons[new_value])
            for m in self.path_name_to_willow_io.values():
                m.SetCompassIcon(self.marker_type)

    @Hook("Engine.WillowInventory.DropFrom")
    def willow_pickup_spawned(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        if not self.enable_spawn_sound or (caller.Owner is get_pc().Pawn and not self.player_drop_sound):
            return True
        if any(
                caller.RarityLevel in range(c["min_level"], c["max_level"] + 1)
                for c in self.selected_config
        ):
            caller.PlayAkEvent(self.ak_event)
        return True

    @Hook("WillowGame.WillowPickup.ConvertRigidBodyToFixed")
    def willow_pickup_ground(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        if not any(
                caller.InventoryRarityLevel in range(c["min_level"], c["max_level"] + 1) for c in self.selected_config
        ):
            return True
        rarity_name = ""
        for c in self.selected_config:
            if caller.InventoryRarityLevel in range(c["min_level"], c["max_level"] + 1):
                rarity_name = c["name"]
                break
        name = caller.Inventory.GenerateHumanReadableName() if caller.Inventory else "Loot"
        if name not in self.name_to_io_def:
            item_level = re.search(r"\d+", name)
            if item_level:
                item_level = int(item_level.group(0))
                description = f"Level {item_level}"
            else:
                description = "Loot baby baby!"
            header = re.sub(r" INVALID \d+", "", name)
            description = fr"{description}\n{header}"

            new_io = unrealsdk.ConstructObject(Class="InteractiveObjectDefinition", Name=name.replace(" ", "_"))
            unrealsdk.KeepAlive(new_io)
            new_io.ObjectFlags.B |= 4
            pc = get_pc()

            pc.ConsoleCommand(fr"set {pc.PathName(new_io)} StatusMenuMapInfoBoxHeader {rarity_name}")
            pc.ConsoleCommand(fr"set {pc.PathName(new_io)} StatusMenuMapInfoBoxDescription {description}")

            self.name_to_io_def[name] = new_io

        path_name = caller.PathName(caller)
        if path_name not in self.path_name_to_willow_io:
            dummy = spawn_dummy_object(self.name_to_io_def[name],
                                       (caller.Location.X, caller.Location.Y, caller.Location.Z))
            dummy.SetCompassIcon(self.marker_type)
            self.path_name_to_willow_io[path_name] = dummy
        return True

    @Hook("WillowGame.WillowPickup.PickedUpBy")
    def willow_pickup_picked_up(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        path_name = caller.PathName(caller)
        if path_name in self.path_name_to_willow_io:
            self.path_name_to_willow_io[path_name].Destroyed()
            del self.path_name_to_willow_io[path_name]
        return True

    @Hook("WillowGame.WillowPlayerController.WillowClientShowLoadingMovie")
    def level_cleanup(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        for w_io in self.path_name_to_willow_io.values():
            w_io.Destroyed()
        self.path_name_to_willow_io.clear()

        return True


unrealsdk.RegisterMod(LootMarker())
