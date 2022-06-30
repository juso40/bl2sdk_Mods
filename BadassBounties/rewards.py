from dataclasses import dataclass
from enum import Enum

import random


@dataclass
class Reward:
    name: str
    description: str
    lootpool: str
    level: int


class ERewardType(Enum):
    RARE = 0
    EPIC = 1
    LEGENDARY = 2
    RAID = 3


RARE_POOL = "GD_Itempools.EnemyDropPools.Pool_GunsAndGear_04_Rare"
EPIC_POOL = "GD_Itempools.EnemyDropPools.Pool_GunsAndGear_05_VeryRare"
LEGENDARY_POOL = "GD_Itempools.EnemyDropPools.Pool_GunsAndGear_06_Legendary"

REWARD_LOOTPOOLS_WEIGHTS = {
    ERewardType.RARE: [0.7, 0.2, 0.1],
    ERewardType.EPIC: [0.2, 0.7, 0.1],
    ERewardType.LEGENDARY: [0.2, 0.3, 0.5],
    ERewardType.RAID: [0.0, 0.0, 1]
}


def get_balanced_reward(pt: int, level: int, reward_type: ERewardType) -> Reward:
    weights = REWARD_LOOTPOOLS_WEIGHTS[ERewardType(reward_type)].copy()
    weights[0] -= level / 450
    weights[1] += level / 500  # Increase the weight of the Legendary rewards depending on the current level
    weights[2] += level / 300  # Increase the weight of the Legendary rewards depending on the current level
    pool: str = random.choices([RARE_POOL, EPIC_POOL, LEGENDARY_POOL], weights=weights, k=1)[0]
    return Reward(
        name=f"Level {level} Reward",
        description=f"Level {level} Reward",
        lootpool=pool,
        level=level
    )
