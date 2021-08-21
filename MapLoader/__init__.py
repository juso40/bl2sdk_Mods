from typing import List
import os
import json
import threading

import unrealsdk
from unrealsdk import *

from ..ModMenu import EnabledSaveType, ModTypes, SDKMod, OptionManager

from . import bl2tools
from . import placeablehelper


class MapLoader(SDKMod):
    Name = "Map Loader"
    Version = "1.2"
    Types = ModTypes.Utility | ModTypes.Content
    Description = "Allows the use of custom map files created by the MapEditor.\n " \
                  "To add/remove a custom map simply place/remove the .json map file into/from the <MapLoader/Maps/> " \
                  "directory.\n" \
                  "Each map file has its own Options/Mods entry that you can either enable or disable."
    Author = "Juso"
    SaveEnabledState = EnabledSaveType.LoadWithSettings

    def __init__(self):
        self.path: os.PathLike = os.path.dirname(os.path.realpath(__file__))

        self.loading_option = OptionManager.Options.Spinner(Caption="Threaded Loading",
                                                            Description="Faster travel times, "
                                                                        "instead slowly load in custom map changes.",
                                                            StartingValue="Disabled",
                                                            Choices=["Enabled", "Disabled"])
        self.Options: List[OptionManager.Options.Base] = [self.loading_option]
        self.available_maps: List[str] = [os.path.splitext(file)[0] for file
                                          in os.listdir(os.path.join(self.path, "Maps"))
                                          if file.lower().endswith(".json")]
        self.loader_threads: List[threading.Thread] = []

        for amap in self.available_maps:  # type: str
            self.Options.append(
                OptionManager.Options.Spinner(
                    Caption=amap, Description=f"Modifies {self.get_modified_maps(amap)}", StartingValue="Enabled",
                    Choices=["Enabled", "Disabled"]
                )
            )

    def Enable(self) -> None:
        def end_load(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            unrealsdk.RegisterHook("WillowGame.WillowGameViewportClient.Tick", __file__, thread_tick)

            level_name: str = bl2tools.get_world_info().GetStreamingPersistentMapName().lower()
            for op in self.Options:  # type: OptionManager.Options.Spinner
                # Check if map gets modified using its description we earlier set
                if op.CurrentValue == "Enabled" and level_name in op.Description:
                    if self.loading_option.CurrentValue == "Enabled":
                        t = threading.Thread(target=self.load_map, args=(op.Caption, level_name))
                        self.loader_threads.append(t)
                        t.start()
                    else:
                        self.load_map(op.Caption, level_name)
            return True

        def start_load(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            if params.MovieName is None:
                return True
            if self.loader_threads:
                for t in self.loader_threads:
                    t.join()
                self.loader_threads.clear()
                unrealsdk.RemoveHook("WillowGame.WillowGameViewportClient.Tick",
                                     __file__)
            return True

        def thread_tick(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            if self.loader_threads and all(not x.is_alive() for x in self.loader_threads):
                self.loader_threads.clear()
                unrealsdk.RemoveHook("WillowGame.WillowGameViewportClient.Tick",
                                     __file__)
            return True

        unrealsdk.RegisterHook("WillowGame.WillowPlayerController.WillowClientDisableLoadingMovie",
                               __file__,
                               end_load)
        unrealsdk.RegisterHook("WillowGame.WillowPlayerController.WillowClientShowLoadingMovie",
                               __file__,
                               start_load)

    def Disable(self) -> None:
        unrealsdk.RemoveHook("WillowGame.WillowPlayerController.WillowClientDisableLoadingMovie",
                             __file__)
        unrealsdk.RemoveHook("WillowGame.WillowPlayerController.WillowClientShowLoadingMovie",
                             __file__)

    def get_modified_maps(self, name: str) -> List[str]:
        if os.path.isfile(os.path.join(self.path, "Maps", f"{name}.json")):
            with open(os.path.join(self.path, "Maps", f"{name}.json")) as fp:
                map_dict: dict = json.load(fp)
            return list(map_dict.keys())

        return []

    def load_map(self, name: str, curr_map: str) -> None:
        """
        Load a custom map from a given .json file.

        :param name: The name of the .json map file.
        :return:
        """
        if os.path.isfile(os.path.join(self.path, "Maps", f"{name}.json")):
            with open(os.path.join(self.path, "Maps", f"{name}.json")) as fp:
                map_dict = json.load(fp)
        else:
            unrealsdk.Log(f"Map {os.path.join(self.path, 'Maps', f'{name}.json')} does not exist!")
            return

        load_this = map_dict.get(curr_map, None)
        if not load_this:  # No Map data for currently loaded map found!
            return
        placeablehelper.load_map(load_this)  # Finally, load the actual map from data dict


unrealsdk.RegisterMod(MapLoader())
