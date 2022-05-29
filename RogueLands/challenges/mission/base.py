from ..challenge import Challenge

import unrealsdk


class MissionChallenge(Challenge):
    def __init__(self) -> None:
        super().__init__()
        self.name = ""
        self.completed = False
        self.total_completions = 0

        self.outer_dict_key = "Missions"
        self.required_mission = "Wont Complete"

    def register_hooks(self) -> None:
        def update_mission_status(
                caller: unrealsdk.UObject,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct
        ) -> bool:
            if params.NewMissionStatus != 3:
                return True
            if not caller.IsLocalPlayerController():
                return True
            name = caller.PathName(params.Mission)
            if name == self.required_mission:
                self.completed = True
                self.total_completions += 1
            return True

        unrealsdk.RegisterHook(
            "WillowGame.WillowPlayerController.UpdateMissionStatus",
            str(id(self)),
            update_mission_status
        )

    def remove_hooks(self) -> None:
        unrealsdk.RemoveHook("WillowGame.WillowPlayerController.UpdateMissionStatus", str(id(self)))

    def load_challenge(self, save_dict: dict) -> None:
        challenges = save_dict.get(self.outer_dict_key, {}).get(self.name, {})
        self.completed = challenges.get("completed", False)
        self.total_completions = challenges.get("completions", 0)

    def save_challenge(self, save_dict: dict) -> None:
        save_dict[self.outer_dict_key] = save_dict.get(self.outer_dict_key, {})
