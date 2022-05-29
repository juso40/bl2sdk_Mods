from . import BaseUnlockable

import unrealsdk


class RespawnLegendaryUnlockable(BaseUnlockable):
    def __init__(self) -> None:
        super(RespawnLegendaryUnlockable, self).__init__("Random Legendary on reset")
        self.legendary_pool = "GD_Itempools.WeaponPools.Pool_Weapons_All_06_Legendary"
        self.reward_backup = []

    def unlock(self) -> None:
        start_mission = unrealsdk.FindObject("MissionDefinition", "GD_Episode01.M_Ep1_Champion")
        self.reward_backup = [x for x in start_mission.Reward.RewardItemPools]
        start_mission.Reward.RewardItemPools = [unrealsdk.FindObject("ItemPoolDefinition", self.legendary_pool)]

    def lock(self) -> None:
        start_mission = unrealsdk.FindObject("MissionDefinition", "GD_Episode01.M_Ep1_Champion")
        start_mission.Reward.RewardItemPools = self.reward_backup
