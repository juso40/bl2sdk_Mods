from typing import List, Tuple
import random

import unrealsdk

from .kills import KillsChallenge
from ...mixins import FeedbackMixin
from ...mixins import RewardMixin
from ...rewards import ERewardType
from ...rewards import get_balanced_reward

RANGES: List[Tuple[int, int]] = [(15, 30), (30, 50), (35, 70)]  # (min, max) for NVHM, TVHM and UVHM

TAG_GROUPS = {
    "Humanoid": ["BodyTag_Bruiser", "BodyTag_Engineer", "BodyTag_Goliath", "BodyTag_Human", "BodyTag_Marauder",
                 "BodyTag_Nomad", "BodyTag_Psycho", "BodyTag_Knight", "BodyTag_Natives", "BodyTag_Wizard"],
    "Robot": ["BodyTag_Constructor", "BodyTag_Gyrocopter", "BodyTag_HyperionTurret", "BodyTag_Loader",
              "BodyTag_Surveyor", "BodyTag_Turret", "BodyTag_SpiderTank"],
    "Creature": ["BodyTag_BugMorph", "BodyTag_Crystalisk", "BodyTag_PrimalBeast", "BodyTag_PrimalBeastBaby",
                 "BodyTag_PrimalBeastBig", "BodyTag_PrimalBeast_KingMong", "BodyTag_Rakk", "BodyTag_Rat",
                 "BodyTag_RatThief", "BodyTag_Skag", "BodyTag_Skagzilla", "BodyTag_Spiderant", "BodyTag_Stalker",
                 "BodyTag_Thresher", "BodyTag_Drifter", "BodyTag_DrifterBaby", "BodyTag_DrifterBadass",
                 "BodyTag_Craboid_Small", "BodyTag_Crabworm", "BodyTag_Crawmerax", "BodyTag_GiantSpore",
                 "BodyTag_Scaylion", "BodyTag_SmallTurkeyMinion"],
    "Mythical": ["BodyTag_AnchorMan", "BodyTag_Infected", "BodyTag_Infected_Pod", "BodyTag_Golem",
                 "BodyTag_Infected_Mimic", "BodyTag_Dragons", "BodyTag_Dwarf", "BodyTag_DwarfMiner",
                 "BodyTag_HallowSkeleton", "BodyTag_Knight", "BodyTag_Mimic", "BodyTag_Nast_AnchorMan",
                 "BodyTag_Orc", "BodyTag_Orczerker", "BodyTag_Skeleton", "BodyTag_Snowminion",
                 "BodyTag_Snowman", "BodyTag_Spider", "BodyTag_SpiderQueen", "BodyTag_Stumpy", "BodyTag_Treant",
                 "BodyTag_Wisp", "BodyTag_Wizard"]
}


class TagGroupKillsChallenge(KillsChallenge, FeedbackMixin, RewardMixin):
    key = "TagGroup"
    reward_type = ERewardType.RARE

    def __init__(self):
        super().__init__()
        self.needs = 1
        self.track = "TagGroup"
        self._name = "NormalKills"
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
        if (
                target and target.BodyClass and
                target.BodyClass.BodyTag and
                target.BodyClass.BodyTag.Name in TAG_GROUPS[self.track]
        ):
            self.has += 1
            self.progress_feedback()

    def reset_progress(self):
        super().reset_progress()

        self.needs = random.randint(*RANGES[self.playthrough_index])  # Update needed Kills
        self.track = random.choice(list(TAG_GROUPS.keys()))  # Update Tracked Body Tag
        self._name = f"Kill {self.track} Enemies"
        self.reward = get_balanced_reward(self.playthrough_index, self.level, self.reward_type)
