from .base import KillChallenge


class VoracidousKillChallenge(KillChallenge):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Voracidous Slain"
        self.required_enemy = "GD_Sage_Raid_Beast.Character.CharClass_Sage_Raid_Beast"

    def save_challenge(self, save_dict: dict) -> None:
        super().save_challenge(save_dict)
        save_dict[self.outer_dict_key][self.name] = {
            "completed": self.completed,
            "completions": self.total_completions,
        }
