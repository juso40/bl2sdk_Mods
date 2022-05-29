from .base import KillChallenge


class HaderaxKillChallenge(KillChallenge):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Haderax Slain"
        self.required_enemy = "GD_Anemone_SandWormBoss_1.Character.CharacterClass_Anemone_SandWormBoss_1"

    def save_challenge(self, save_dict: dict) -> None:
        super().save_challenge(save_dict)
        save_dict[self.outer_dict_key][self.name] = {
            "completed": self.completed,
            "completions": self.total_completions,
        }
