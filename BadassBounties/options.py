from typing import List
from ..ModMenu import OptionManager


__all__: List[str] = ["B_FEEDBACK_OPTION"]

B_FEEDBACK_OPTION = OptionManager.Options.Boolean(
    Caption="Enable Update-Feedback",
    Description="When enabled shows Feedback when challenge progress got updated.",
    StartingValue=True
)


