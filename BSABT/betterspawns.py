import unrealsdk

from . import bl2tools

import json
import os


class Spawns:

    def __init__(self, path: str):
        self.PATH: str = path
        self.spawnpoints_path: str = os.path.join(self.PATH, "spawnpoint.json")
        self.b_load_travel: bool = True
        self.b_load_tp: bool = True
        self.set_location_counter: int = 0
        self.filename: str = ""

    def Enable(self):

        def hk_save_game(
                caller: unrealsdk.UObject,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            map_name: str = unrealsdk.GetEngine().GetCurrentWorldInfo().GetStreamingPersistentMapName().lower()

            # Only save the spawn location if we are not in main menu
            # And only save after we have set the spawn location
            if map_name != "menumap" and not (self.b_load_tp and self.b_load_travel):
                self.filename = params.Filename
                self.save_spawn_station(
                    unrealsdk.GetEngine().GetCurrentWorldInfo().GRI.ActiveRespawnCheckpointTeleportActor
                )

            return True

        def hk_load_save(
                caller: unrealsdk.UObject,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            if params.bIsInitialSpawn or params.bIsClassChange:
                # We only want to set the spawn location on the first time the player spawns
                self.b_load_travel = True
                self.b_load_tp = True
                self.set_location_counter = 0
                pc = bl2tools.get_player_controller()
                self.filename = pc.GetSaveGameNameFromid(pc.GetCachedSaveGame().SaveGameId)
            return True

        def hk_spawn_travel(
                caller: unrealsdk.UObject,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            map_name: str = unrealsdk.GetEngine().GetCurrentWorldInfo().GetStreamingPersistentMapName().lower()
            if map_name in ("loader", "fakeentry"):
                return True
            # This only happens when the player used a normal travels station, not a FTStation
            if self.b_load_travel:
                self.b_load_travel = False
                self.set_spawn_location(bl2tools.get_player_controller().Pawn)
                return False
            return True

        def hk_spawn_tp(
                caller: unrealsdk.UObject,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            map_name: str = unrealsdk.GetEngine().GetCurrentWorldInfo().GetStreamingPersistentMapName().lower()
            if map_name in ("loader", "fakeentry"):
                return True
            # This only happens when the player used a normal travels station, not a FTStation
            if self.b_load_tp:
                self.b_load_tp = False
                self.set_spawn_location(bl2tools.get_player_controller().Pawn)
            return True

        unrealsdk.RegisterHook(
            "WillowGame.WillowSaveGameManager.SaveGame",
            "SaveGame_HookBSABT",
            hk_save_game
        )
        unrealsdk.RegisterHook(
            "WillowGame.WillowPlayerController.ShouldLoadSaveGameOnSpawn",
            "LoadSaveBSABT",
            hk_load_save
        )
        unrealsdk.RegisterHook(
            "WillowGame.WillowPlayerController.ClientSetPawnLocation",
            "TravelHookBSABT",
            hk_spawn_travel
        )
        unrealsdk.RegisterHook(
            "WillowGame.WillowPlayerController.StopTeleporterSound",
            "SpawnHookBSABT",
            hk_spawn_tp
        )

    def Disable(self):
        unrealsdk.RemoveHook("WillowGame.WillowSaveGameManager.SaveGame", "SaveGame_HookBSABT")
        unrealsdk.RemoveHook("WillowGame.WillowPlayerController.ShouldLoadSaveGameOnSpawn", "OnSpawn_HookBSABT")
        unrealsdk.RemoveHook("WillowGame.WillowPlayerController.ClientSetPawnLocation", "TravelHookBSABT")
        unrealsdk.RemoveHook("WillowGame.WillowPlayerController.StopTeleporterSound", "SpawnHookBSABT")

    def save_spawn_station(self, station: unrealsdk.UObject):
        my_spawn_dict = {}
        if os.path.exists(self.spawnpoints_path):
            # Load the existing spawnpoints
            with open(self.spawnpoints_path, "r") as file:
                try:
                    my_spawn_dict = json.load(file)
                except Exception:
                    unrealsdk.Log("Error loading spawnpoint.json")

        # Add the new spawnpoint
        with open(self.spawnpoints_path, "w") as file:
            exit_pos = station.ExitPoints[0].Location
            my_spawn_dict[self.filename] = {
                "SaveStation": bl2tools.get_obj_path_name(station),
                "Position": (exit_pos.X, exit_pos.Y, exit_pos.Z)
            }
            json.dump(my_spawn_dict, file, indent=4)

    def set_spawn_location(self, pawn: unrealsdk.UObject):
        # Only if the spawnpoint file exists we can set the spawn location
        if os.path.exists(self.spawnpoints_path):
            with open(self.spawnpoints_path, "r") as file:
                try:
                    my_spawn_dict = json.load(file)
                    last_save_station = unrealsdk.FindObject("Object", my_spawn_dict[self.filename]["SaveStation"])
                    gri = unrealsdk.GetEngine().GetCurrentWorldInfo().GRI
                    gri.ActiveRespawnCheckpointTeleportActor = last_save_station
                    pawn.Location = tuple(my_spawn_dict[self.filename]["Position"])
                except Exception:
                    unrealsdk.Log("Could not load the spawnpoint.json")
        else:
            unrealsdk.Log(f"{self.spawnpoints_path} did not exist yet.")
