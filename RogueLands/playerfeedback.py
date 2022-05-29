from ..UserFeedback import TrainingBox

import unrealsdk

from .stats import StatManagerInstance
from .challenges import ChallengeManagerInstance


class PlayerFeedback:
    def __init__(self) -> None:
        self.warning_title = "RogueLands"
        self.warning_body = "RogueLands is currently enabled!\n" \
                            "This means, if you die you will lose all your progress in UVHM and all your items.\n" \
                            "If you want to play without losing progress, disable RogueLands."

        self.wrong_playthrough_title = "RogueLands"
        self.wrong_playthrough_body = "Your are currently in the wrong Playthrough. " \
                                      "Please select the '<font color=\"#ffd300\">Rogue-Lands Mode</font>'."

        self.death_message_title = "You Died!"
        self.death_message_body = "But it's not over yet.\n" \
                                  "Your progress has been reset, but you will keep your exp and currency." \
                                  "To continue please save quit and press 'CONTINUE' on the main menu."

        self.true_ending_title = "True Ending!"
        self.true_ending_body = "Your mission progress has been reset. " \
                                "You may now restart the game and continue with all your items."

        self.stats_title = "1Life Stats"
        self.total_stats_title = "Total Stats"

        self.challenge_progress_title = "Challenge Progress"
        self.total_challenges_title = "Total Challenges"
        self.challenge_unlockables = "Challenge Rewards"

    def enable(self) -> None:
        def show_playthrough_choices(
                caller: unrealsdk.UFunction,
                function: unrealsdk.UFunction,
                params: unrealsdk.FStruct,
        ) -> bool:
            if params.ButtonTag == "Dif2":  # Disable TVHM
                return False
            if params.ButtonTag == "Dif1":  # Disable NVHM
                return False
            if params.ButtonTag != "Dif3":  # We only overwrite UVHM
                return True

            caller.AppendButton(
                "Dif3",
                "RogueLands Mode",
                "Rogue-Lite Game Mode. When you die, you respawn at the start of the game with all your Exp. You will "
                "lose all your items, but you will keep your stats and skills.",
                params.OnClicked
            )
            caller.SetDefaultButton("Dif3", False)
            return False

        unrealsdk.RegisterHook("WillowGame.WillowGFxDialogBox.AppendButton", str(id(self)), show_playthrough_choices)
        self.show_enable_warning()

    def disable(self) -> None:
        unrealsdk.RemoveHook("WillowGame.WillowGFxDialogBox.AppendButton", str(id(self)))

    def on_death(self) -> None:
        self.show_death_messages()
        # self.show_total_challenges()

    def show_enable_warning(self) -> None:
        TrainingBox(Title=self.warning_title, Message=self.warning_body, MinDuration=1.0).Show()

    def show_death_messages(self) -> None:
        box = TrainingBox(Title=self.death_message_title, Message=self.death_message_body, MinDuration=3.0)
        box.OnExit = self.show_stats
        box.Show()

    def show_true_ending(self) -> None:
        # ToDo: Show true ending
        pass

    def show_stats(self, player_died: bool = True) -> None:
        stat_box = TrainingBox(
            Title=self.stats_title,
            Message=StatManagerInstance.get_presentable_stats(),
            MinDuration=1.0
        )
        if player_died:
            def total_stats() -> None:
                b = TrainingBox(
                    Title=self.total_stats_title,
                    Message=StatManagerInstance.get_presentable_stats_total(),
                    MinDuration=1.0
                )
                b.OnExit = self.show_challenge_progress
                b.Show()
            stat_box.OnExit = total_stats

        stat_box.Show()

    def show_challenge_progress(self) -> None:
        text = ChallengeManagerInstance.get_challenge_progress()
        TrainingBox(Title=self.challenge_progress_title, Message=text, MinDuration=1.0).Show()

    def show_total_challenges(self) -> None:
        text = ChallengeManagerInstance.get_challenges_total()
        TrainingBox(Title=self.total_challenges_title, Message=text, MinDuration=1.0).Show()

    def show_challenge_unlockables(self) -> None:
        text = ChallengeManagerInstance.get_presentable_challenge_unlockables()
        message = f"<font size=\"8\">After completing the specified challenges, " \
                  f"the following rewards will be unlocked:</font>\n{text}"
        TrainingBox(Title=self.challenge_unlockables, Message=message, MinDuration=1.0).Show()
