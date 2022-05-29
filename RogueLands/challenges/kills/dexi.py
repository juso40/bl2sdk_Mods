from .base import KillChallenge


class DexiduousKillChallenge(KillChallenge):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Dexiduous Slain"
        self.required_enemy = "GD_DrifterRaid.Character.CharClass_DrifterRaid"

    def save_challenge(self, save_dict: dict) -> None:
        super().save_challenge(save_dict)
        save_dict[self.outer_dict_key][self.name] = {
            "completed": self.completed,
            "completions": self.total_completions,
        }
