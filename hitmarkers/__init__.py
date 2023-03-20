from typing import Any

import unrealsdk

from Mods.ModMenu import EnabledSaveType, Game, ModTypes, OptionManager, RegisterMod, SDKMod, Options
from Mods.coroutines import TickCoroutine, WaitForSeconds, start_coroutine_post_render, start_coroutine_tick
from .markers import draw_hitmarker, draw_killmarker
from .options import CritMarkers, KillMarkers, Markers, options


def draw_markers_in_menu() -> TickCoroutine:
    while True:
        yield WaitForSeconds(0.5, unscaled=True)
        start_coroutine_post_render(draw_hitmarker(was_crit=False))
        yield WaitForSeconds(0.5, unscaled=True)
        start_coroutine_post_render(draw_hitmarker(was_crit=True))
        yield WaitForSeconds(0.5, unscaled=True)
        start_coroutine_post_render(draw_hitmarker(was_crit=False))
        start_coroutine_post_render(draw_killmarker())

        if not Markers.show_marker_in_menu.CurrentValue:
            break


def hk_hit_enemy(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
    if params.PC is not unrealsdk.GetEngine().GamePlayers[0].Actor:
        return True
    was_crit = params.DamageEventData.DamageEventFlags == 1
    start_coroutine_post_render(draw_hitmarker(was_crit=was_crit))
    return True


def hk_kill_enemy(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
    if params.Killer is not unrealsdk.GetEngine().GamePlayers[0].Actor:
        return True
    if not KillMarkers.enabled.CurrentValue:
        return True
    start_coroutine_post_render(draw_killmarker())
    return True


class HitMarkers(SDKMod):
    Name: str = "Hit Markers"
    Description: str = "Shows hit and kill markers."
    Author: str = "juso"
    Types: ModTypes = ModTypes.Utility
    Version: str = "1.0"
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadOnMainMenu
    SupportedGames: Game = Game.BL2 | Game.TPS | Game.AoDK
    Options = options

    def Enable(self) -> None:
        def update_nested(nested_option):
            if isinstance(nested_option, Options.Value):
                self.ModOptionChanged(nested_option, nested_option.CurrentValue)
            elif isinstance(nested_option, Options.Nested):
                for child in nested_option.Children:
                    update_nested(child)

        for option in self.Options:
            update_nested(option)
        unrealsdk.RegisterHook(
            "WillowGame.WillowDamageTypeDefinition.DisplayRecentDamageForPlayer", "HitMarkersDamageHook",
            hk_hit_enemy
        )
        unrealsdk.RegisterHook(
            "WillowGame.WillowPawn.Died", "HitMarkersKillHook",
            hk_kill_enemy
        )

    def Disable(self) -> None:
        unrealsdk.RemoveHook(
            "WillowGame.WillowDamageTypeDefinition.DisplayRecentDamageForPlayer", "HitMarkersDamageHook"
        )
        unrealsdk.RemoveHook(
            "WillowGame.WillowPawn.Died", "HitMarkersKillHook"
        )

    def ModOptionChanged(self, option: OptionManager.Options.Base, new_value: Any) -> None:
        if option is Markers.show_marker_in_menu:
            if new_value:
                start_coroutine_tick(draw_markers_in_menu())


mod_instance = HitMarkers()
RegisterMod(mod_instance)
