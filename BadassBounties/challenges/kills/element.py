from typing import List, Tuple
import random

import unrealsdk

from .kills import KillsChallenge
from ...mixins import FeedbackMixin
from ...mixins import RewardMixin
from ...rewards import ERewardType
from ...rewards import get_balanced_reward

RANGES: List[Tuple[int, int]] = [(15, 30), (30, 50), (35, 70)]  # (min, max) for NVHM, TVHM and UVHM

DAMAGE_TYPES = {
    "Corrosive": "GD_Corrosive",
    "Explosive": "GD_Explosive",
    "Non-Elemental": "GD_Impact",
    "Incendiary": "GD_Incendiary",
    "Shock": "GD_Shock",
    "Slag": "GD_Amp",
}


class ElementalKillsChallenge(KillsChallenge, FeedbackMixin, RewardMixin):
    key = "Elemental"
    reward_type = ERewardType.RARE

    def __init__(self):
        super().__init__()
        self.needs = 1
        self.track = "Elements"
        self._name = "ElementKills"
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
        if self.track in str(params.Pipeline.DamageTypeDef):
            self.has += 1
            self.progress_feedback()

    def reset_progress(self):
        super().reset_progress()

        self.needs = random.randint(*RANGES[self.playthrough_index])  # Update needed Kills
        name, self.track = random.choice(list(DAMAGE_TYPES.items()))  # Update Tracked Body Tag

        self._name = f"Get {name} Kills"
        self.reward = get_balanced_reward(self.playthrough_index, self.level, self.reward_type)
