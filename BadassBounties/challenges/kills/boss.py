from typing import List, Tuple
import random

import unrealsdk

from .kills import KillsChallenge
from ...mixins import FeedbackMixin
from ...mixins import RewardMixin
from ...rewards import ERewardType, get_balanced_reward

RANGES: List[Tuple[int, int]] = [(1, 3), (2, 4), (3, 5)]  # (min, max) for NVHM, TVHM and UVHM
AI_CLASSES = {
    #  "BNK-3R": "GD_HyperionBunkerBoss.Character.CharClass_BunkerBoss",  # Does not trigger a kill
    "Wilhelm": "GD_Willhelm.Character.CharClass_Willhelm",
    # "The Warrior": "GD_FinalBoss.Character.CharClass_FinalBoss",  # Does not trigger a kill
    "H3RL-E": "GD_Orchid_LoaderBoss.Character.CharClass_Orchid_LoaderBoss",
    # "Roscoe": "GD_Orchid_RakkHive.Character.CharacterClass_RakkHive",  # Can not be killed after story
    # "The Leviathan": "GD_Orchid_BossWorm.Character.CharacterClass_Orchid_BossWorm",  # Can not be killed after story
    "Badassasaurus": "GD_Truckasaurus.Character.CharClass_Truckasaurus",
    "Motor Momma": "GD_Iris_MotorMama.Character.CharClass_Iris_MotorMama",
    "Jackenstein": "GD_Sage_FinalBoss.Character.CharClass_Sage_FinalBoss",
    "Woundspike": "GD_Sage_Ep4_Data.Creature.CharClass_Sage_Ep4_Creature",
    "Gold Golem": "GD_GolemGold.Character.CharClass_GolemGold",
    "Handsome Dragon": "GD_DragonBridgeBoss.Character.CharClass_DragonBridgeBoss",
    "Handsome Sorcerer": "GD_JackWarlock.Character.CharClass_JackWarlock",
    "Mister Boney Pants Guy": "GD_BoneyPants.Character.CharClass_BoneyPants",
    "Sorcerer's Daughter": "GD_AngelBoss.Character.CharClass_AngelBoss",
    "Pumpkin Kingpin": "GD_PumpkinheadFlying.Character.CharClass_PumpkinheadFlying",
    "Wattle Gobbler": "GD_BigBird.Character.CharClass_BigBird",
    "Tinder Snowflakes": "GD_Snowman.Character.CharClass_Snowman",
    "Uranus": "GD_Anemone_UranusBOT.Character.CharClass_Anemone_UranusBOT",
    "Saturn": "GD_LoaderUltimateBadass.Character.CharClass_LoaderUltimateBadass",
}


class BossKillsChallenge(KillsChallenge, FeedbackMixin, RewardMixin):
    key = "BossKills"
    reward_type = ERewardType.EPIC

    def __init__(self):
        super().__init__()
        self.needs = 1
        self.track = "AIClass"
        self._name = "BossKills"
        self.reward = None

    @property
    def completed(self) -> bool:
        return self.has >= self.needs

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
        self._name = f"Kill {name}"
        self.reward = get_balanced_reward(self.playthrough_index, self.level, self.reward_type)
