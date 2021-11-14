import unrealsdk
from unrealsdk import *

from ..ModMenu import SDKMod, Game, EnabledSaveType, ModTypes, Hook, RegisterMod


class Scaler(SDKMod):
    Name = "TVHM Scaler"
    Description = "Scales all zones in TVHM to your level."
    Version = "1.0"
    SupportedGames = Game.AoDK
    Types = ModTypes.Utility | ModTypes.Gameplay
    SaveEnabledState = EnabledSaveType.LoadOnMainMenu
    Author = "Juso"

    @Hook("WillowGame.WillowPlayerController.WillowClientShowLoadingMovie")
    def start_loading(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct):
        player_level = unrealsdk.GetEngine().GamePlayers[0].Actor.GetCachedSaveGame().ExpLevel
        balance_tvhm = unrealsdk.FindObject("GameBalanceDefinition", "GD_Aster_GameStages.Balance.Aster_P2_GameBalance")
        for region in balance_tvhm.BalanceByRegion:
            region.MinDefaultGameStage.BaseValueConstant = player_level
            region.MaxDefaultGameStage.BaseValueConstant = player_level
        return True


RegisterMod(Scaler())
