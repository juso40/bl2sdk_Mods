from ..challenge import Challenge

import unrealsdk


class KillChallenge(Challenge):

    def __init__(self) -> None:
        super().__init__()
        self.outer_dict_key = "Kills"
        self.required_ai_class: str = "Wont complete this one"

    def register_hooks(self) -> None:
        def on_kill(
                caller: unrealsdk.UObject,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            # The killer has not to be the local player controller
            target = params.aTargetPawn
            if not target:
                return True
            target = target.AIClass

            name = caller.PathName(target)
            if name == self.required_ai_class:
                self.completed = True
                self.total_completions += 1
                self.check_unlockable()

            return True

        unrealsdk.RegisterHook("WillowGame.WillowPlayerPawn.KilledEnemy", str(id(self)), on_kill)

    def remove_hooks(self) -> None:
        unrealsdk.RemoveHook("WillowGame.WillowPlayerPawn.KilledEnemy", str(id(self)))

    def load_challenge(self, save_dict: dict) -> None:
        challenges = save_dict.get(self.outer_dict_key, {}).get(self.name, {})
        self.completed = challenges.get("completed", False)
        self.total_completions = challenges.get("completions", 0)

    def save_challenge(self, save_dict: dict) -> None:
        save_dict[self.outer_dict_key] = save_dict.get(self.outer_dict_key, {})
