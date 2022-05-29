from .base import KillChallenge


class AncientDragonsKillChallenge(KillChallenge):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Ancient Dragons Slain"
        self.required_enemy = "GD_DragonHeart_Raid.Character.CharClass_DragonHeart_Raid"

    def save_challenge(self, save_dict: dict) -> None:
        super().save_challenge(save_dict)
        save_dict[self.outer_dict_key][self.name] = {
            "completed": self.completed,
            "completions": self.total_completions,
        }
