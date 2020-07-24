import unrealsdk
from unrealsdk import *

from . import bl2tools

import json
import os


class Spawns:

    def __init__(self, path):
        self.PATH = path
        self.b_load = False
        self.set_location_counter = 0
        self.filename = ""

    def Enable(self):

        def SaveGame_Hook(caller: UObject, function: UFunction, params: FStruct) -> bool:

            if GetEngine().GetCurrentWorldInfo().GetStreamingPersistentMapName() != "menumap" and not self.b_load:
                self.filename = params.Filename
                self.save_spawn_station(GetEngine().GetCurrentWorldInfo().GRI.ActiveRespawnCheckpointTeleportActor)
            return True

        def LoadSave(caller: UObject, function: UFunction, params: FStruct) -> bool:
            if params.bIsInitialSpawn or params.bIsClassChange:
                self.b_load = True
                self.set_location_counter = 0
                pc = bl2tools.get_player_controller()
                self.filename = pc.GetSaveGameNameFromid(pc.GetCachedSaveGame().SaveGameId)
            return True

        def Spawn_Hook(caller: UObject, function: UFunction, params: FStruct) -> bool:
            self.set_location_counter += 1
            # On the 3rd time calling this function the pawn actually gets placed in the map itself
            # I couldn't find any better function, it seems this is the easiest implementation
            if self.b_load and self.set_location_counter == 3:
                self.b_load = False
                self.set_spawn_location(bl2tools.get_player_controller().Pawn)
                return False
            return True

        unrealsdk.RegisterHook("WillowGame.WillowSaveGameManager.SaveGame", "SaveGame_HookBSABT", SaveGame_Hook)
        unrealsdk.RegisterHook("WillowGame.WillowPlayerController.ShouldLoadSaveGameOnSpawn", "LoadSaveBSABT", LoadSave)
        unrealsdk.RegisterHook("WillowGame.WillowPlayerController.ClientSetPawnLocation", "Spawn_HookBSABT", Spawn_Hook)

    def Disable(self):
        unrealsdk.RemoveHook("WillowGame.WillowSaveGameManager.SaveGame", "SaveGame_HookBSABT")
        unrealsdk.RemoveHook("WillowGame.WillowPlayerController.ShouldLoadSaveGameOnSpawn", "OnSpawn_HookBSABT")
        unrealsdk.RemoveHook("WillowGame.WillowPlayerController.ClientSetPawnLocation", "Spawn_HookBSABT")

    def save_spawn_station(self, station):
        my_spawn_dict = {}
        if os.path.exists(os.path.join(self.PATH, "spawnpoint.json")):
            with open(os.path.join(self.PATH, "spawnpoint.json"), "r") as file:
                try:
                    my_spawn_dict = json.load(file)
                except:
                    Log("Error loading spawnpoint.json")
        with open(os.path.join(self.PATH, "spawnpoint.json"), "w") as file:
            exit = station.ExitPoints[0].Location
            my_spawn_dict[self.filename] = (exit.X, exit.Y, exit.Z)
            json.dump(my_spawn_dict, file, indent=4)


    def set_spawn_location(self, pawn):
        if os.path.exists(os.path.join(self.PATH, "spawnpoint.json")):
            with open(os.path.join(self.PATH, "spawnpoint.json"), "r") as file:
                try:
                    my_spawn_dict = json.load(file)
                    pawn.Location = tuple(my_spawn_dict[self.filename])
                except:
                    Log("Could not load the spawnpoint.json")
        else:
            Log("{} did not exist yet.".format(os.path.join(self.PATH, "spawnpoint.json")))