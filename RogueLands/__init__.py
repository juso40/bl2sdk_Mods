import os
import webbrowser

import unrealsdk

from ..ModMenu import EnabledSaveType, SDKMod, Hook, Game, Keybind, ModTypes

from . import savemanager
from . import playerfeedback
from .stats import StatManagerInstance
from .challenges import ChallengeManagerInstance
from .scaling import ScalerManagerInstance


def _get_pc() -> unrealsdk.UObject:
    return unrealsdk.GetEngine().GamePlayers[0].Actor


# noinspection PyUnusedLocal
class RogueLands(SDKMod):
    Name = "RogueLands"
    Description = """\
RogueLands is a mod that turns Borderlands into a Rogue-Lite game. \
This mod works similar to the 1life challenge, but with the twist, \
that when you die, you respawn at the start of the game with all your Exp. \
You will lose all your items, but you will keep your stats and skills. \
All progress with this mod will count towards the UVHM. You do not need to have it unlocked to play. \
Overpower Levels will also be ignored, it is recommended to create a new character for this mod!\
    """
    Author = "Juso"
    Version = "1.3"
    Types = ModTypes.Gameplay
    SaveEnabledState = EnabledSaveType.LoadOnMainMenu
    SupportedGames = Game.BL2

    def __init__(self):
        super(RogueLands, self).__init__()
        self.PATH = os.path.dirname(os.path.realpath(__file__))
        self.save_manager = savemanager.SaveManager(self.PATH)
        self.player_feedback = playerfeedback.PlayerFeedback()

        _p = self.player_feedback
        self.Keybinds = [
            Keybind("Show Challenge Progress", "F5", OnPress=lambda _: _p.show_challenge_progress()),
            Keybind("Show Challenge Rewards", "F7", OnPress=lambda _: _p.show_challenge_unlockables()),
            Keybind("Show Stats", "F8", OnPress=lambda _: _p.show_stats(False)),
            Keybind("?", "O", OnPress=lambda _: webbrowser.open("https://youtu.be/dQw4w9WgXcQ"))
        ]

    def Enable(self):
        super().Enable()
        self.save_manager.enable()
        self.player_feedback.enable()
        ChallengeManagerInstance.register_hooks()
        StatManagerInstance.register_hooks()
        ScalerManagerInstance.register_hooks()

    def Disable(self):
        super().Disable()
        ChallengeManagerInstance.remove_hooks()
        StatManagerInstance.remove_hooks()
        ScalerManagerInstance.remove_hooks()

    @Hook("WillowGame.WillowPlayerPawn.StartInjuredDeathSequence")
    def on_death(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        """Reset the players inventory and mission progress."""
        # Enter Spectator Mode
        pc = _get_pc()
        pc.Unpossess()
        pc.HideHUD()
        pc.ServerSpectate()
        self.player_feedback.on_death()
        self.save_manager.on_death()
        return True

    @Hook("WillowGame.WillowPlayerController.WillowClientDisableLoadingMovie")
    def on_map_load(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        """Every map load."""
        self.save_manager.try_update_file_name_from_cached_save_game()

        ScalerManagerInstance.update()  # Call Update to check if we need to remove hooks
        ChallengeManagerInstance.update()

        # Make sure the player has all 4 slots unlocked
        inv_man = caller.GetPawnInventoryManager()
        if inv_man:
            inv_man.SetWeaponReadyMax(4)
        self.save_manager.save()
        return True


unrealsdk.RegisterMod(RogueLands())
