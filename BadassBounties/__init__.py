import os

import unrealsdk

from ..ModMenu import EnabledSaveType, SDKMod, Game, Keybind, ModTypes

from .challengemanager import ChallengeManagerInstance

from .savegamemanager import SaveGameManager
from .events import KilledEnemyEventManager
from .options import B_FEEDBACK_OPTION


def _get_pc() -> unrealsdk.UObject:
    return unrealsdk.GetEngine().GamePlayers[0].Actor


# noinspection PyUnusedLocal
class BadassBounties(SDKMod):
    Name = "Badass Bounties"
    Description = "Adds many randomly generated Bounties to the game."
    Author = "Juso | JoltzDude139"
    Version = "1.0"
    Types = ModTypes.Gameplay
    SaveEnabledState = EnabledSaveType.LoadOnMainMenu
    SupportedGames = Game.BL2

    def __init__(self):
        super().__init__()
        self.PATH = os.path.dirname(os.path.realpath(__file__))
        self.save_manager = SaveGameManager(self.PATH)
        self.Keybinds = [
            Keybind("Show Bounty Menu", "F4", OnPress=lambda _: ChallengeManagerInstance.show_challenge_menu()),
            Keybind("Show Active Bounties", "F5", OnPress=lambda _: ChallengeManagerInstance.show_current_challenges()),
        ]
        self.Options = [B_FEEDBACK_OPTION]

    def Enable(self):
        super().Enable()
        KilledEnemyEventManager.register_hooks()
        self.save_manager.enable()

    def Disable(self):
        super().Disable()
        KilledEnemyEventManager.remove_hooks()
        self.save_manager.disable()


unrealsdk.RegisterMod(BadassBounties())
