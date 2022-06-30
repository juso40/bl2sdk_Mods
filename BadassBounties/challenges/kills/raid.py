from typing import List, Tuple
import random

import unrealsdk

from .kills import KillsChallenge
from ...mixins import FeedbackMixin
from ...mixins import RewardMixin
from ...rewards import ERewardType, get_balanced_reward

RANGES: List[Tuple[int, int]] = [(1, 1), (1, 1), (1, 1)]  # (min, max) for NVHM, TVHM and UVHM
AI_CLASSES = {
    "Haderax": "GD_Anemone_SandWormBoss_1.Character.CharacterClass_Anemone_SandWormBoss_1",
    "Pyro Pete": "GD_Iris_Raid_PyroPete.Character.CharClass_Iris_Raid_PyroPete",
    "Hyperius": "GD_Orchid_RaidEngineer.Character.CharClass_Orchid_RaidEngineer",
    "Master Gee": "GD_Orchid_RaidShaman.Character.CharClass_Orchid_RaidShaman",
    "Vermivorous": "GD_BugMorphRaid.Character.CharClass_BugMoprhRaid",
    "Terramorphous": "GD_Thresher_Raid.Character.CharClass_Thresher_Raid",
    "Dexiduous": "GD_DrifterRaid.Character.CharClass_DrifterRaid",
    "Voracidous": "GD_Sage_Raid_Beast.Character.CharClass_Sage_Raid_Beast",
    "Son of Crawmerax the Invincible": "GD_Crawmerax_Son.Character.CharClass_Crawmerax_Son",

    "Ancient Dragons": "GD_DragonHeart_Raid.Character.CharClass_DragonHeart_Raid",
    # This is a bit of a hack, but it works
}


class RaidKillsChallenge(KillsChallenge, FeedbackMixin, RewardMixin):
    key = "RaidKills"
    reward_type = ERewardType.RAID

    def __init__(self):
        super().__init__()
        self.needs = 1
        self.track = "AIClass"
        self._name = "RaidKills"
        self.reward = None

    @property
    def completed(self) -> bool:
        return self.has >= self.needs

    def activate(self) -> None:
        super().activate()

        # The following hack is to support the Ancient Dragons Raid Challenge
        if self.track != "GD_DragonHeart_Raid.Character.CharClass_DragonHeart_Raid":
            return

        def dragon_loot_spewer_callback(
                caller: unrealsdk.UObject,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            ai_pawn = params.BossActor
            ai_class = caller.PathName(ai_pawn.AIClass)

            if not params.bEnable:
                unrealsdk.Log(ai_pawn.GetHealth() / ai_pawn.GetMaxHealth())

            if ai_class == self.track and not params.bEnable and ai_pawn.GetHealth() / ai_pawn.GetMaxHealth() < 0.5:
                self.has += 1
                self.progress_feedback()
            return True

        unrealsdk.RegisterHook(
            "WillowGame.WillowGameReplicationInfo.InitBossBar",
            f"ugly_dragon_hack{id(self)}",
            dragon_loot_spewer_callback
        )

    def deactivate(self) -> None:
        super().deactivate()
        unrealsdk.RemoveHook(
            "WillowGame.SequenceEvent.CheckActivate", f"ugly_dragon_hack{id(self)}",
        )

    def on_killed_enemy(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> None:
        target = caller
        if target and caller.PathName(target.AIClass) == self.track:
            self.has += 1
            self.progress_feedback()

    def reset_progress(self):
        super().reset_progress()

        self.needs = random.randint(*RANGES[self.playthrough_index])  # Update needed Kills
        name, ai = random.choice(list(AI_CLASSES.items()))
        self.track = ai
        self._name = f"Slay {name}"
        self.reward = get_balanced_reward(self.playthrough_index, self.level, self.reward_type)
