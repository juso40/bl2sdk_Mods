from .base import KillChallenge


class HyperiusKillChallenge(KillChallenge):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Hyperius Slain"
        self.required_enemy = "GD_Orchid_RaidEngineer.Character.CharClass_Orchid_RaidEngineer"

    def save_challenge(self, save_dict: dict) -> None:
        super().save_challenge(save_dict)
        save_dict[self.outer_dict_key][self.name] = {
            "completed": self.completed,
            "completions": self.total_completions,
        }
