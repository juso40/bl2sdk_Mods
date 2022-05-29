from .base import MissionChallenge
from ..unlocks import IncreasedXPUnlockable


class MainStoryMissionChallenge(MissionChallenge):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Main Story Completed"
        self.unlockable = IncreasedXPUnlockable()
        self.required_mission = "GD_Episode17.M_Ep17_KillJack"

    def save_challenge(self, save_dict: dict) -> None:
        super().save_challenge(save_dict)
        save_dict[self.outer_dict_key][self.name] = {
            "completed": self.completed,
            "completions": self.total_completions,
        }
