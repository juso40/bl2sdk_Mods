import json
import os

import unrealsdk

from .stats import StatManagerInstance
from .challenges import ChallengeManagerInstance


def _get_pc() -> unrealsdk.UObject:
    return unrealsdk.GetEngine().GamePlayers[0].Actor


class SaveManager:
    def __init__(self, module_path: str) -> None:
        self.module_path = module_path
        self.save_file_name = ""
        self.player_progress = {}

    def enable(self) -> None:
        self.player_progress = {}
        self.try_update_file_name_from_cached_save_game()
        self.load()
        self.save()

        self.register_hooks()
        ChallengeManagerInstance.update()

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
            ChallengeManagerInstance.update()
            caller.WPCOwner.OnSelectOverpowerLevel(caller.WPCOwner.GetCachedSaveGame(), 0)
            caller.LaunchSaveGame(2)
            return False

        def set_pt(
                caller: unrealsdk.UFunction,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            """Playthrough Changed."""
            unrealsdk.GetEngine().GetCurrentWorldInfo().GRI.SetCurrentPlaythrough(params.PrimaryWPC, 2)
            return False

        def save_game(
                caller: unrealsdk.UObject,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            """Save the players stats."""
            if not self.player_progress:
                return True
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

    def on_death(self) -> None:
        """Player died."""
        self.reset_stats()
        self.reset_inventory()
        self.reset_mission_progress()

    def reset_inventory(self) -> None:
        """Reset the players inventory."""
        pc = _get_pc()
        # Remove Inventory
        save_game = pc.GetCachedSaveGame()
        save_game.WeaponData = []
        save_game.ItemData = []
        # Reset Skills
        pri = pc.PlayerReplicationInfo
        pri.GeneralSkillPoints += pc.ResetSkillTree(True)

    def reset_mission_progress(self) -> None:
        """Reset the player mission progress."""
        pc = _get_pc()

        # Skip Claptrap talking in first mission
        start_mission = unrealsdk.FindObject("MissionDefinition", "GD_Episode01.M_Ep1_Champion")
        start_mission.bHeardKickoff = True
        pc.MissionPlaythroughs[2].MissionList = [
            (start_mission, 1, [0], None, [], 50, False, True)
        ]
        file_name = pc.GetSaveGameNameFromid(pc.GetCachedSaveGame().SaveGameId)
        pc.GetWillowGlobals().GetWillowSaveGameManager().Save(pc, file_name, 0)

    def reset_stats(self) -> None:
        """Reset the players stats."""
        if not self.player_progress:
            self.load()
        StatManagerInstance.on_death()
        ChallengeManagerInstance.on_death()
        self.save()

    def save(self) -> None:
        if not self.save_file_name:
            return
        self.player_progress = {}
        StatManagerInstance.save_stats(self.player_progress)
        ChallengeManagerInstance.save_challenges(self.player_progress)
        with open(os.path.join(self.module_path, self.save_file_name), "w") as file:
            json.dump(self.player_progress, file, indent=2)

    def load(self) -> None:
        if self.save_file_name == "":
            if not self.try_update_file_name_from_cached_save_game():
                self.player_progress = {}
                return
        try:
            with open(os.path.join(self.module_path, self.save_file_name), "r") as file:
                self.player_progress = json.load(file)
        except (FileNotFoundError, TypeError):
            self.player_progress = {}

        StatManagerInstance.load_stats(self.player_progress)
        ChallengeManagerInstance.load_challenges(self.player_progress)
