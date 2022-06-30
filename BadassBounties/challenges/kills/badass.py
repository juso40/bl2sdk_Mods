from typing import List, Tuple
import random

import unrealsdk

from .kills import KillsChallenge
from ...mixins import FeedbackMixin
from ...mixins import RewardMixin
from ...rewards import ERewardType, get_balanced_reward

RANGES: List[Tuple[int, int]] = [(3, 7), (5, 11), (7, 13)]  # (min, max) for NVHM, TVHM and UVHM


class BadassKillsChallenge(KillsChallenge, FeedbackMixin, RewardMixin):
    key = "BadassKills"
    reward_type = ERewardType.EPIC

    def __init__(self):
        super().__init__()
        self.needs = 1
        self.track = "Badasses"
        self._name = "Kill Badass Enemies"
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
        if target and target.IsChampion():
            self.has += 1
            self.progress_feedback()

    def reset_progress(self):
        super().reset_progress()
        self.needs = random.randint(*RANGES[self.playthrough_index])  # Update needed Kills
        self.reward = get_balanced_reward(self.playthrough_index, self.level, self.reward_type)
