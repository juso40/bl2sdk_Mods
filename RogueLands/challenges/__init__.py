from typing import List

from .challenge import Challenge

import importlib
import os

# import all folders in this directory
for f in os.listdir(os.path.dirname(__file__)):
    if os.path.isdir(os.path.join(os.path.dirname(__file__), f)):
        importlib.import_module(".{}".format(f), package=__package__)

__all__: List[str] = ["ChallengeManagerInstance"]


class ChallengeManager:

    def load_challenges(self, save_dict: dict) -> None:
        challenges_dict = save_dict.get("Challenges", {})
        for c in Challenge.challenges:
            c.load_challenge(challenges_dict)

    def save_challenges(self, save_dict: dict) -> None:
        challenge_dict = save_dict.get("Challenges", {})
        for c in Challenge.challenges:
            c.save_challenge(challenge_dict)
        save_dict["Challenges"] = challenge_dict

    def get_challenge_progress(self) -> str:
        return "\n".join(
            c.readable_challenge_progress for c in Challenge.challenges if c.name
        )

    def get_challenges_total(self) -> str:
        return "\n".join(
            c.readable_challenge_completions for c in Challenge.challenges if c.name
        )

    def get_presentable_challenge_unlockables(self) -> str:
        return "\n".join(
            c.challenge_unlockable for c in Challenge.challenges if c.unlockable
        )

    def on_death(self) -> None:
        for c in Challenge.challenges:
            c.on_death()

    def register_hooks(self) -> None:
        for c in Challenge.challenges:
            c.register_hooks()

    def remove_hooks(self) -> None:
        for c in Challenge.challenges:
            c.remove_hooks()

    def update(self) -> None:
        for c in Challenge.challenges:
            if c.unlockable:
                c.check_unlockable()


ChallengeManagerInstance: ChallengeManager = ChallengeManager()
