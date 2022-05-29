from .base import KillChallenge


class MasterGeeKillChallenge(KillChallenge):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Master Gee Slain"
        self.required_enemy = "GD_Orchid_RaidShaman.Character.CharClass_Orchid_RaidShaman"

    def save_challenge(self, save_dict: dict) -> None:
        super().save_challenge(save_dict)
        save_dict[self.outer_dict_key][self.name] = {
            "completed": self.completed,
            "completions": self.total_completions,
        }
