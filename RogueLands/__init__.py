from dataclasses import dataclass, asdict

from typing import Optional, List, Any
import json
import os
import webbrowser

import unrealsdk

from ..ModMenu import EnabledSaveType, SDKMod, Hook, Game, Keybind, ModTypes


def _get_pc() -> unrealsdk.UObject:
    return unrealsdk.GetEngine().GamePlayers[0].Actor


def _show_training_message(title: str, message: str, blocking_duration: float = 3) -> None:
    pc = _get_pc()
    pc.GFxUIManager.ShowTrainingDialog(message, title, blocking_duration, 0, False)


@dataclass
class PlayerStats:
    kills: int = 0
    total_kills: int = 0
    badass_kills: int = 0
    total_badass_kills: int = 0
    total_deaths: int = 0
    money_collected: int = 0
    total_money_collected: int = 0
    eridium_collected: int = 0
    total_eridium_collected: int = 0
    seraph_crystals_collected: int = 0
    total_seraph_crystals_collected: int = 0
    killed_terra: bool = False
    killed_hyperius: bool = False
    killed_gee: bool = False
    killed_pete: bool = False
    killed_voracidous: bool = False
    killed_dexidious: bool = False
    killed_ancient_dragons: bool = False
    killed_haderax: bool = False
    killed_vermi: bool = False
    story_completed: bool = False


class RogueLands(SDKMod):
    Name = "RogueLands"
    Description = """\
RogueLands is a mod that turns Borderlands into a Rogue-Lite game. \
This mod works similar to the 1life challenge, but with the twist, \
that when you die, you respawn at the start of the game with all your Exp. \
You will loose all your items, but you will keep your stats and skills. \
All progress with this mod will count towards the UVHM. You do not need to have it unlocked to play. \
Overpower Levels will also be ignored, it is recommended to create a new character for this mod!\
    """
    Author = "Juso"
    Version = "1.0"
    Types = ModTypes.Gameplay
    SaveEnabledState = EnabledSaveType.LoadOnMainMenu
    SupportedGames = Game.BL2

    def __init__(self):
        super(RogueLands, self).__init__()
        self.save_file_name: str = "PlaceHolder"
        self.player_stats: Optional[PlayerStats] = None
        self.PATH = os.path.dirname(os.path.realpath(__file__))

        self.Keybinds = [
            Keybind("Show Challenge Progress", "F5", OnPress=lambda _: self.show_challenge_progress()),
            Keybind("?", "O", OnPress=lambda _: webbrowser.open("https://youtu.be/dQw4w9WgXcQ"))
        ]

    def Enable(self):
        super().Enable()
        _show_training_message("RogueLands", "RogueLands is currently enabled!\n"
                                             "This means, if you die you will loose all your progress"
                                             " in UVHM and all your items.\n"
                                             "If you want to play without losing progress, disable RogueLands.",
                               blocking_duration=1
                               )

    def Disable(self):
        super().Disable()

    @Hook("WillowGame.WillowGFxDialogBox.AppendButton")
    def playthrough_choice(
            self,
            caller: unrealsdk.UFunction,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct,
    ) -> bool:
        """Populate the PT Choices."""
        if params.ButtonTag == "Dif2":
            return False
        if params.ButtonTag == "Dif1":
            return False
        if params.ButtonTag != "Dif3":
            return True

        caller.AppendButton(
            "Dif3",
            "RogueLands Mode",
            "Rogue-Lite Game Mode. When you die, you respawn at the start of the game with all your Exp. You will "
            "loose all your items, but you will keep your stats and skills.",
            params.OnClicked
        )
        caller.SetDefaultButton("Dif3", False)
        return False

    @Hook("WillowGame.WillowGFxMovie.LaunchSaveGame")
    def launch_save_game(
            self,
            caller: unrealsdk.UFunction,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct,
    ) -> bool:
        """Player pressed 'CONTINUE'."""
        caller.WPCOwner.OnSelectOverpowerLevel(caller.WPCOwner.GetCachedSaveGame(), 0)
        caller.LaunchSaveGame(2)
        return False

    @Hook("WillowGame.WillowGameReplicationInfo.SetCurrentPlaythrough")
    def set_pt(self, caller: unrealsdk.UFunction, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
        """Playthrough Changed."""
        unrealsdk.GetEngine().GetCurrentWorldInfo().GRI.SetCurrentPlaythrough(params.PrimaryWPC, 2)
        return False

    @Hook("WillowGame.WillowSaveGameManager.BeginLoadGame")
    def player_loaded_save(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        """Player Loaded Save into game."""
        self.save_file_name = f"{params.Filename.split('.')[0]}_stats.json"
        unrealsdk.Log(self.save_file_name)
        self.load_stats()
        if unrealsdk.GetEngine().GetCurrentWorldInfo().GetStreamingPersistentMapName().lower() == "menumap":
            return True
        if unrealsdk.GetEngine().GetCurrentWorldInfo().GRI.CurrentPlaythrough != 2:
            _show_training_message(
                "RogueLands",
                "Your are currently in the wrong Playthrough. Please select the 'Rogue-Lands Mode'.",
                blocking_duration=5
            )
        return True

    @Hook("WillowGame.WillowSaveGameManager.SaveGame")
    def save_game(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        """Save the players stats."""
        if not self.player_stats:
            return True
        self.save_file_name = f"{params.Filename.split('.')[0]}_stats.json"
        self.save_stats()
        return True

    @Hook("WillowGame.WillowPlayerController.UpdateMissionStatus")
    def update_mission_status(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        """Update the players mission status."""

        # We only care for Ready For Turn In or for Completed
        if params.NewMissionStatus != 3:
            return True
        mission_name = caller.PathName(params.Mission)
        self.update_challenge_stats(mission_name)
        return True

    @Hook("WillowGame.WillowPlayerPawn.StartInjuredDeathSequence")
    def on_death(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        """Reset the players inventory and mission progress."""
        pc = _get_pc()
        pc.Unpossess()
        pc.HideHUD()
        pc.ServerSpectate()
        self.show_stats()
        self.reset_stats()
        self.reset_inventory()
        self.reset_mission_progress()
        self.player_stats.total_deaths += 1
        return True

    @Hook("WillowGame.WillowPlayerController.WillowClientDisableLoadingMovie")
    def on_map_load(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        """Every map load."""

        pc = _get_pc()
        self.save_file_name = pc.GetSaveGameNameFromid(pc.GetCachedSaveGame().SaveGameId).split('.')[0] + "_stats.json"

        # Make sure the player has all 4 slots unlocked
        inv_man = caller.GetPawnInventoryManager()
        if inv_man:
            inv_man.SetWeaponReadyMax(4)
        self.save_stats()
        return True

    @Hook("WillowGame.WillowPawn.SetGameStage")
    def on_set_game_stage(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        """Scale the Pawns to the players level."""
        if "WillowPlayerPawn" in str(caller.Class):
            return True

        pc = _get_pc()
        if pc.PlayerReplicationInfo.ExpLevel < 50:
            unrealsdk.DoInjectedCallNext()
            caller.SetGameStage(pc.PlayerReplicationInfo.ExpLevel)
            return False
        return True

    @Hook("Engine.WillowInventory.ClientInitializeInventoryFromDefinition")
    def on_item_init(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        """Force scale items to the players level."""

        # If the item is owned by PlayerPawn or PlayerController, don't scale it
        if caller.AdditionalQueryInterfaceSource and "Player" in str(caller.AdditionalQueryInterfaceSource.Class):
            return True

        pc = _get_pc()
        if pc.PlayerReplicationInfo.ExpLevel < 50:
            caller.SetExpLevel(pc.PlayerReplicationInfo.ExpLevel)
            caller.SetGameStage(pc.PlayerReplicationInfo.ExpLevel)
            caller.DefinitionData.ManufacturerGradeIndex = pc.PlayerReplicationInfo.ExpLevel
            caller.DefinitionData.GameStage = pc.PlayerReplicationInfo.ExpLevel
        return True

    @Hook("WillowGame.WillowPlayerController.OnCurrencyChanged")
    def on_add_currency(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        """Update the players stats."""

        if self.player_stats is None:
            self.load_stats()

        # Don't update the currency if the player lost money
        if params.ChangedCurrency.CurrentAmount < params.ChangedCurrency.LastKnownAmount:
            return True
        currency_diff = params.ChangedCurrency.CurrentAmount - params.ChangedCurrency.LastKnownAmount
        if params.ChangedCurrency.FormOfCurrency == 0:
            self.player_stats.money_collected += currency_diff
            self.player_stats.total_money_collected += currency_diff
        elif params.ChangedCurrency.FormOfCurrency == 1:
            self.player_stats.eridium_collected += currency_diff
            self.player_stats.total_eridium_collected += currency_diff
        elif params.ChangedCurrency.FormOfCurrency == 2:
            self.player_stats.seraph_crystals_collected += currency_diff
            self.player_stats.total_seraph_crystals_collected += currency_diff
        self.save_stats()
        return True

    @Hook("WillowGame.WillowPlayerPawn.KilledEnemy")
    def on_kill(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        """Update the players stats."""
        if self.player_stats is None:
            self.load_stats()
        self.player_stats.kills += 1
        self.player_stats.total_kills += 1
        if params.aTargetPawn.IsChampion():
            self.player_stats.badass_kills += 1
            self.player_stats.total_badass_kills += 1

        self.update_challenge_stats(caller.PathName(params.aTargetPawn.AIClass))

        self.save_stats()
        return True

    def update_challenge_stats(self, name: str) -> None:
        """Update the players stats, related to raid bosses. Name can either be Mission Definition or AIClass."""
        if self.player_stats is None:
            self.load_stats()

        if name == " GD_Z2_ThresherRaid.M_ThresherRaid":
            self.player_stats.killed_terra = True
        elif name == "GD_Orchid_Raid.M_Orchid_Raid1":
            self.player_stats.killed_hyperius = True
        elif name == "GD_Orchid_Raid.M_Orchid_Raid3":
            self.player_stats.killed_gee = True
        elif name == "GD_IrisRaidBoss.M_Iris_RaidPete":
            self.player_stats.killed_pete = True
        elif name == "GD_Sage_Raid.M_Sage_Raid":
            self.player_stats.killed_voracidous = True
        elif name == "GD_Aster_RaidBoss.M_Aster_RaidBoss":
            self.player_stats.killed_ancient_dragons = True
        elif name == "GD_Anemone_Side_RaidBoss.M_Anemone_CacophonousLure":
            self.player_stats.killed_haderax = True
        elif name == "GD_DrifterRaid.Character.CharClass_DrifterRaid":
            self.player_stats.killed_dexidious = True
        elif name == "GD_BugMorphRaid.Character.CharClass_BugMoprhRaid":
            self.player_stats.killed_vermi = True
        elif name == "GD_Episode17.M_Ep17_KillJack":
            self.player_stats.story_completed = True
        else:
            return  # We have not found the boss
        self.save_stats()

        if not all((self.player_stats.story_completed,
                    self.player_stats.killed_terra,
                    self.player_stats.killed_hyperius,
                    self.player_stats.killed_gee,
                    self.player_stats.killed_pete,
                    self.player_stats.killed_voracidous,
                    self.player_stats.killed_ancient_dragons,
                    self.player_stats.killed_haderax,
                    self.player_stats.killed_dexidious,
                    self.player_stats.killed_vermi,
                    )):
            self.show_challenge_progress(
                title="New Challenge completed!",
                start_text="You finished a new challenge, but you are not quite done yet!"
            )
        else:
            _show_training_message(
                "True Ending!",
                "Your mission progress has been reset. "
                "You may now restart the game and continue with all your items.",
                blocking_duration=6
            )
            self.show_stats(player_died=False)
            self.show_challenge_progress(
                title="Congratulations! Vault Hunter!",
                start_text="You successfully completed all challenges in a single life!"
            )
            self.reset_stats()
            self.reset_mission_progress()
            pc = _get_pc()
            pc.Unpossess()
            pc.HideHUD()
            pc.ServerSpectate()

    def show_challenge_progress(self, title: str = "Challenge Progress", start_text: str = "") -> None:
        """Show the challenge progress."""
        if self.player_stats is None:
            self.load_stats()

        def color_text(t: str, cond: bool) -> str:
            return f"""<font color={'"#14e55b">[funstat][x]' if cond else '"#f80104">[funstat][   ]'} {t}</font>\n"""

        text = f"{start_text}\n"
        text += color_text("Story Completed", self.player_stats.story_completed)
        text += color_text("Terramorphous Slain", self.player_stats.killed_terra)
        text += color_text("Hyperius Slain", self.player_stats.killed_hyperius)
        text += color_text("Master Gee Slain", self.player_stats.killed_gee)
        text += color_text("Pyro Pete Slain", self.player_stats.killed_pete)
        text += color_text("Voracidous Slain", self.player_stats.killed_voracidous)
        text += color_text("Ancient Dragons Slain", self.player_stats.killed_ancient_dragons)
        text += color_text("Haderax Slain", self.player_stats.killed_haderax)
        text += color_text("Dexidious Slain", self.player_stats.killed_dexidious)
        text += color_text("Vermivorous Slain", self.player_stats.killed_vermi)

        _show_training_message(title, text)

    def reset_inventory(self) -> None:
        """Reset the players inventory."""
        pc = _get_pc()
        save_game = pc.GetCachedSaveGame()
        save_game.WeaponData = []
        save_game.ItemData = []

        # Reset Skills
        pri = pc.PlayerReplicationInfo
        pri.GeneralSkillPoints += pc.ResetSkillTree(True)

        # Might keep currency
        # pri.AddCurrencyOnHand(0, -pri.GetCurrencyOnHand(0))
        # pri.AddCurrencyOnHand(1, -pri.GetCurrencyOnHand(1))
        # pri.AddCurrencyOnHand(2, -pri.GetCurrencyOnHand(2))

    def reset_mission_progress(self) -> None:
        """Reset the players mission progress."""
        pc = _get_pc()
        pc.MissionPlaythroughs[2].MissionList = []
        file_name = pc.GetSaveGameNameFromid(pc.GetCachedSaveGame().SaveGameId)
        pc.GetWillowGlobals().GetWillowSaveGameManager().Save(pc, file_name, 0)

    def reset_stats(self) -> None:
        """Reset the players stats."""
        if not self.player_stats:
            self.load_stats()
        self.player_stats.kills = 0
        self.player_stats.badass_kills = 0
        self.player_stats.money_collected = 0
        self.player_stats.eridium_collected = 0
        self.player_stats.seraph_crystals_collected = 0
        self.player_stats.killed_terra = False
        self.player_stats.killed_hyperius = False
        self.player_stats.killed_gee = False
        self.player_stats.killed_pete = False
        self.player_stats.killed_voracidous = False
        self.player_stats.killed_ancient_dragons = False
        self.player_stats.killed_haderax = False
        self.player_stats.killed_dexidious = False
        self.player_stats.killed_vermi = False
        self.player_stats.story_completed = False

        self.save_stats()

    def show_stats(self, player_died: bool = True) -> None:
        """Show the players stats."""

        _show_training_message(
            "TOTAL STATS",
            f"""\
<font color="#27c0f1">Your total achievements:</font>
[funstat]Deaths: <font color="#ffd300">{self.player_stats.total_deaths}</font>
[funstat]Kills: <font color="#ffd300">{self.player_stats.total_kills}</font>
[funstat]Badass Kills: <font color="#ffd300">{self.player_stats.total_badass_kills}</font>
[funstat]Cash: <font color="#ffd300">{self.player_stats.total_money_collected}</font>
[funstat]Eridium: <font color="#ffd300">{self.player_stats.total_eridium_collected}</font>
[funstat]Seraph Crystals: <font color="#ffd300">{self.player_stats.total_seraph_crystals_collected}</font>
        """,
            blocking_duration=7
        )

        _show_training_message(
            "1LIFE STATS",
            f"""\
<font color="#27c0f1">You achieved:</font>
[funstat]Kills: <font color="#ffd300">{self.player_stats.kills}</font>
[funstat]Badass Kills: <font color="#ffd300">{self.player_stats.badass_kills}</font>
[funstat]Cash: <font color="#ffd300">{self.player_stats.money_collected}</font>
[funstat]Eridium: <font color="#ffd300">{self.player_stats.eridium_collected}</font>
[funstat]Seraph Crystals: <font color="#ffd300">{self.player_stats.seraph_crystals_collected}</font>
""",
            blocking_duration=5
        )

        if player_died:
            _show_training_message(
                "YOU DIED!",
                """\
But it's not over yet.
Your progress has been reset, but you will keep your exp and currency.
To continue please save quit and press 'CONTINUE' on the main menu.
    """,
                blocking_duration=3
            )

    def save_stats(self) -> None:
        """Save the players stats."""
        if not self.player_stats:
            return
        with open(os.path.join(self.PATH, self.save_file_name), "w") as file:
            json.dump(asdict(self.player_stats), file)

    def load_stats(self) -> None:
        """Load the players stats."""
        try:
            with open(os.path.join(self.PATH, self.save_file_name), "r") as file:
                self.player_stats = PlayerStats(**json.load(file))
        except (FileNotFoundError, TypeError):
            self.player_stats = PlayerStats()


unrealsdk.RegisterMod(RogueLands())
