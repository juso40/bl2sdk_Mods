import json
import os

import unrealsdk

from .challengemanager import ChallengeManagerInstance


def _get_pc() -> unrealsdk.UObject:
    return unrealsdk.GetEngine().GamePlayers[0].Actor


class SaveGameManager:
    def __init__(self, module_path: str) -> None:
        self.module_path: str = module_path
        self.save_file_name: str = ""
        self.player_progress: dict = {}

    def enable(self) -> None:
        self.player_progress = {}
        self.try_update_file_name_from_cached_save_game()
        self.load()
        self.register_hooks()

    def disable(self) -> None:
        self.save()
        self.player_progress = {}
        self.remove_hooks()

    def register_hooks(self) -> None:
        def launch_save_game(
                caller: unrealsdk.UFunction,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct,
        ) -> bool:
            """Player pressed 'CONTINUE'."""
            self.load()  # Make sure we have the latest save data
            return True

        def set_pt(
                caller: unrealsdk.UFunction,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            """Playthrough Changed."""
            self.load(params.InCurrPlaythrough)
            return True

        def save_game(
                caller: unrealsdk.UObject,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            """Save the players stats."""
            self.save_file_name = f"{params.Filename.split('.')[0]}.json"
            self.save()
            return True

        def player_loaded_save(
                caller: unrealsdk.UObject,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            """Player Loaded Save into game."""
            self.save_file_name = f"{params.Filename.split('.')[0]}.json"
            self.load()
            return True

        unrealsdk.RegisterHook("WillowGame.WillowGFxMovie.LaunchSaveGame", str(id(self)), launch_save_game)
        unrealsdk.RegisterHook("WillowGame.WillowGameReplicationInfo.SetCurrentPlaythrough", str(id(self)), set_pt)
        unrealsdk.RegisterHook("WillowGame.WillowSaveGameManager.SaveGame", str(id(self)), save_game)
        unrealsdk.RegisterHook("WillowGame.WillowSaveGameManager.BeginLoadGame", str(id(self)), player_loaded_save)

    def remove_hooks(self) -> None:
        unrealsdk.RemoveHook("WillowGame.WillowGFxMovie.LaunchSaveGame", str(id(self)))
        unrealsdk.RemoveHook("WillowGame.WillowGameReplicationInfo.SetCurrentPlaythrough", str(id(self)))
        unrealsdk.RemoveHook("WillowGame.WillowSaveGameManager.SaveGame", str(id(self)))
        unrealsdk.RemoveHook("WillowGame.WillowSaveGameManager.BeginLoadGame", str(id(self)))

    def try_update_file_name_from_cached_save_game(self) -> bool:
        """Returns True if the file name was updated."""
        pc = _get_pc()
        save_game = pc.GetCachedSaveGame()
        if save_game:
            f = pc.GetSaveGameNameFromid(save_game.SaveGameId)
            if f:
                self.save_file_name = f.split(".")[0] + ".json"
                return True
        return False

    def save(self) -> None:
        if not self.save_file_name:
            return
        try:
            with open(os.path.join(self.module_path, self.save_file_name), "r") as file:
                self.player_progress = json.load(file)
        except FileNotFoundError:
            self.player_progress = {}  # provide a new dict
        ChallengeManagerInstance.save_challenges(self.player_progress)
        with open(os.path.join(self.module_path, self.save_file_name), "w") as file:
            json.dump(self.player_progress, file, indent=2)

    def load(self, new_pt=None) -> None:
        if self.save_file_name == "":
            if not self.try_update_file_name_from_cached_save_game():
                self.player_progress = {}
                return
        try:
            with open(os.path.join(self.module_path, self.save_file_name), "r") as file:
                self.player_progress = json.load(file)
        except (FileNotFoundError, TypeError):
            self.player_progress = {}

        if new_pt is not None:
            ChallengeManagerInstance.load_challenges(self.player_progress, new_pt)
        else:
            ChallengeManagerInstance.load_challenges(self.player_progress)
