from typing import Callable, Any
import datetime
import dataclasses

import unrealsdk

from ..rewards import Reward


def _claim(reward: Reward, pc: unrealsdk.UObject) -> None:
    mission_def = unrealsdk.FindObject("MissionDefinition", "GD_Episode01.M_Ep1_Champion")
    backup_game_stage = mission_def.GameStage
    backup_title = mission_def.MissionName
    backup_credits = mission_def.Reward.CreditRewardMultiplier.BaseValueScaleConstant
    backup_reward_items = [r for r in mission_def.Reward.RewardItems]
    backup_reward_item_pools = [p for p in mission_def.Reward.RewardItemPools]

    mission_def.GameStage = reward.level
    pc.RCon(f"set GD_Episode01.M_Ep1_Champion MissionName {reward.description}")
    mission_def.Reward.RewardItems = []
    reward_pool = unrealsdk.FindObject("Object", reward.lootpool)
    mission_def.Reward.RewardItemPools = [reward_pool, reward_pool]
    mission_def.Reward.CreditRewardMultiplier.BaseValueScaleConstant = 10

    def magic():
        pc.ServerGrantMissionRewards(mission_def, False)
        pc.ShowStatusMenu()

        def reset_mission_def() -> None:
            mission_def.GameStage = backup_game_stage
            pc.RCon(f"set GD_Episode01.M_Ep1_Champion MissionName {backup_title}")
            mission_def.Reward.RewardItems = backup_reward_items
            mission_def.Reward.RewardItemPools = backup_reward_item_pools
            mission_def.Reward.CreditRewardMultiplier.BaseValueScaleConstant = backup_credits

        call_in(5, reset_mission_def)

    call_in(0.01, magic)


def call_in(time: float, call: Callable[[], Any]) -> None:
    """Call the given callable after the given time has passed."""
    timer = datetime.datetime.now()
    future = timer + datetime.timedelta(seconds=time)

    # Create a wrapper to call the routine that is suitable to be passed to RunHook.
    def tick(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
        # Invoke the routine. If it returns False, unregister its tick hook.
        if datetime.datetime.now() >= future:
            call()
            unrealsdk.RemoveHook("WillowGame.WillowGameViewportClient.Tick", "RewardCallIn" + str(call))
        return True

    # Hook the wrapper.
    unrealsdk.RegisterHook("WillowGame.WillowGameViewportClient.Tick", "RewardCallIn" + str(call), tick)


class RewardMixin:
    reward: Reward
    claimed: bool

    def claim_reward(self, pc: unrealsdk.UObject) -> None:
        reward: Reward = self.reward
        reward_copy = dataclasses.replace(reward)
        _claim(reward_copy, pc)
        self.claimed = True

    @property
    def reward_desc(self) -> str:
        return self.reward.description
