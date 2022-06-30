from typing import Union

import Mods.UserFeedback as uf
from ..options import B_FEEDBACK_OPTION
from ..challenges.kills import KillsChallenge


# Honestly there is no idea why this Mixin exists, I just wanted to play around with them after hearing about them.
# I should probably remove them at some point because this just increases the complexity of the code.
# But I probably won't because I'm lazy.

class FeedbackMixin:
    """
     Mixin class for providing feedback to the user.
     The class must have the following attributes:
        - self.completed: bool
        - self.name: str
        - self.progress: str
     """

    @property
    def description(self: KillsChallenge) -> str:
        if self.completed and not self.claimed:
            return f"[x] <font color=\"#38B448\">{self.name}</font> {self.progress}"
        elif self.completed and self.claimed:
            return f"[x] <font color=\"#FFA500\">{self.name}</font> {self.progress}"
        return f"[   ] <font color=\"#F3584B\">{self.name}</font> {self.progress}"

    def progress_feedback(self: Union[KillsChallenge, "FeedbackMixin"]) -> None:
        if B_FEEDBACK_OPTION.CurrentValue and not self.completed:
            uf.ShowHUDMessage(self.name, self.description)
        if self.has == self.needs:  # Just completed
            uf.ShowHUDMessage(self.name, self.description)
