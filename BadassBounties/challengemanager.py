import random
from typing import List, Dict, Type, cast, Union

import unrealsdk

from ..UserFeedback import OptionBox, OptionBoxButton, TrainingBox

from .challenges import Challenge
from .challenges.kills import TagGroupKillsChallenge
from .challenges.kills import BadassKillsChallenge
from .challenges.kills import BossKillsChallenge
from .challenges.kills import RaidKillsChallenge
from .challenges.kills import ElementalKillsChallenge

from .mixins import FeedbackMixin
from .mixins import RewardMixin

__all__ = [
    "ChallengeManagerInstance"
]

CHALLENGE_PER_PT = [3, 5, 7]  # Number of challenges per playthrough

KEY_TO_CHALLENGE: Dict[str, Type[Challenge]] = {
    TagGroupKillsChallenge.key: TagGroupKillsChallenge,
    BadassKillsChallenge.key: BadassKillsChallenge,
    BossKillsChallenge.key: BossKillsChallenge,
    RaidKillsChallenge.key: RaidKillsChallenge,
    ElementalKillsChallenge.key: ElementalKillsChallenge,
}  # Key: Name of challenge, Value: Challenge class

# Key is the min required level to roll the given challenges
CHALLENGE_MIN_LEVELS: Dict[int, List[Type[Challenge]]] = {
    0: [TagGroupKillsChallenge,
        BadassKillsChallenge,
        ElementalKillsChallenge
        ],
    20: [BossKillsChallenge],
    50: [RaidKillsChallenge],
}


class ChallengeManager:

    def __init__(self):
        self.active_challenges: List[Challenge] = []

    @property
    def playthrough_index(self) -> int:
        """
        Returns the current playthrough index.
        """
        return unrealsdk.GetEngine().GetCurrentWorldInfo().GRI.GetCurrPlaythrough()

    @property
    def player_level(self) -> int:
        """
        Returns the current players level.
        """
        pc = unrealsdk.GetEngine().GamePlayers[0].Actor
        try:
            return pc.Pawn.GetGameStage()
        except AttributeError:
            return pc.OverpowerChoiceValue + pc.PlayerReplicationInfo.ExpLevel

    def show_challenge_menu(self) -> None:
        """
        Shows the challenge menu.
        """
        menu: OptionBox = OptionBox(
            Title="Bounties",
            Caption="Welcome to Badass Bounties! "
                    "You can complete randomized bounties for rewards. "
                    "The harder the bounty, the better the reward.\n\nHappy hunting!",
            Buttons=[
                OptionBoxButton(
                    Name="Show Current Bounties",
                    Tip=""
                ),
                OptionBoxButton(
                    Name="Claim Bounty Rewards",
                    Tip=""
                ),
                OptionBoxButton(
                    Name="Re-roll Current Bounties",
                    Tip=""
                ),
                OptionBoxButton(
                    Name="Cancel",
                    Tip=""
                )
            ]
        )
        menu.OnPress = lambda button: {
            "Show Current Bounties": self.show_current_challenges,
            "Claim Bounty Rewards": self.claim_challenge_rewards,
            "Re-roll Current Bounties": self.confirm_reroll,
            "Cancel": lambda: None
        }.get(button.Name, lambda: None)()
        menu.Show()

    def show_current_challenges(self) -> None:
        """
        Shows the current challenges.
        """
        self.fill_challenges()  # We assume the not all possible challenges are loaded.

        challenges = cast(List[FeedbackMixin], self.active_challenges)
        message: str = "\n".join(c.description for c in challenges)
        box: TrainingBox = TrainingBox(
            Title=f"Bounties - Level {self.active_challenges[0].level if self.active_challenges else 0}",
            Message=message,
            PausesGame=True
        )
        box.Show()

    def claim_challenge_rewards(self) -> None:
        """
        Claims the rewards for the current challenges.
        """
        pc = unrealsdk.GetEngine().GamePlayers[0].Actor

        # Check if any challenge is completed and if so, not yet claimed
        if not any(c.completed and not c.claimed for c in self.active_challenges):
            box = OptionBox(
                Title="Bounty Rewards",
                Caption="You currently have no bounty completed.",
                Buttons=[OptionBoxButton(Name="Close", Tip="")]
            )
        else:
            # Now get claim buttons for all completed and not claimed challenges
            claim_buttons = []
            completed_challenges: List[Union[Challenge, RewardMixin]]
            completed_challenges = [c for c in self.active_challenges if c.completed and not c.claimed]

            # Use enumerate to create unique names for each button
            for i, c in enumerate(completed_challenges):
                b = OptionBoxButton(f"{i + 1}: {c.name}", Tip=f"Claim {c.reward_desc}")
                claim_buttons.append(b)
            box = OptionBox(Title="Bounty Rewards", Caption="Claim your rewards!", Buttons=claim_buttons)

            # Register the claim buttons claim function
            # lambda c=c because function default arguments are bound at definition time, not call time
            box.OnPress = lambda button: {
                f"{i + 1}: {c.name}": lambda c=c: c.claim_reward(pc) for i, c in enumerate(completed_challenges)
            }.get(button.Name, lambda: None)()

        box.Show()

    def confirm_reroll(self) -> None:
        title = "Reroll Bounties"
        eridium_color = lambda x: f"<font color=\"#cb0993\">{x} Eridium</font>"

        pri = unrealsdk.GetEngine().GamePlayers[0].Actor.PlayerReplicationInfo
        if pri.GetCurrencyOnHand(1) < self.reroll_cost():
            message = "You do not have enough Eridium to reroll your bounties." \
                      f" You need {eridium_color(self.reroll_cost())}."
            box = OptionBox(
                Title=title,
                Caption=message,
                Buttons=[OptionBoxButton(Name="Close")]
            )
            box.Show()
            return

        message = f"Are you sure you want to reroll your current bounties? This will cost you " \
                  f"{eridium_color(f'{self.reroll_cost()}/{pri.GetCurrencyOnHand(1)}')}</font>."
        if any(c.completed and not c.claimed for c in self.active_challenges):
            message = f"You currently have completed bounties. " \
                      f"By confirming you will not be able to claim rewards.\n\n{message}"
        box = OptionBox(
            Title=title,
            Caption=message,
            Buttons=[
                OptionBoxButton(Name="Close", Tip="Close the window and keep current bounties."),
                OptionBoxButton(Name="Confirm", Tip="Reroll all bounties and loose current progress."),
            ]
        )
        box.OnPress = lambda button: {
            "Close": lambda: None,
            "Confirm": lambda: (self.reroll_current_challenges(), self.show_challenge_menu())
        }.get(button.Name, lambda: None)()
        box.Show()

    def reroll_cost(self) -> int:
        """
        Returns the cost of rerolling the current challenges. 2 Eridium per not completed challenge.
        """
        return sum(2 for c in self.active_challenges if not c.completed)

    def reroll_current_challenges(self) -> None:
        """
        Rerolls the current challenges.
        """
        pri = unrealsdk.GetEngine().GamePlayers[0].Actor.PlayerReplicationInfo
        pri.AddCurrencyOnHand(1, -self.reroll_cost())

        self.remove_current_challenges()
        self.fill_challenges()

    def remove_current_challenges(self) -> None:
        """
        Removes all current challenges.
        """
        for c in self.active_challenges:
            c.deactivate()
        self.active_challenges = []

    def fill_challenges(self) -> None:
        """
        Fills the current challenges.
        """

        # Filter the challenges based on the current level
        available_challenges: List[Type[Challenge]] = []
        for level, challenges in CHALLENGE_MIN_LEVELS.items():
            if level <= self.player_level:  # Add challenges if level is high enough
                available_challenges.extend(challenges)

        def get_random_challenge() -> Type[Challenge]:
            """
            Returns a random challenge.
            """
            return random.choice(available_challenges)

        # Clamp the level between 10 and 50 if in NVHM or TVHM
        clamped_level = max(10, min(self.player_level, 50)) if self.playthrough_index < 2 else self.player_level
        while len(self.active_challenges) < CHALLENGE_PER_PT[self.playthrough_index]:
            c = get_random_challenge()()
            c.set_playthrough(self.playthrough_index)
            c.set_level(clamped_level)
            c.reset_progress()  # Randomize the challenge
            if c.name in [c.name for c in self.active_challenges]:  # Don't allow duplicates
                continue
            c.activate()
            self.active_challenges.append(c)

    def save_challenges(self, save_dict: dict) -> None:
        """
        Saves the current challenges.
        """
        if len(self.active_challenges) != CHALLENGE_PER_PT[self.playthrough_index]:
            unrealsdk.Log("[ChallengeManager] The number of challenges is not correct. This should not happen.")
            return
        pt_challenges = []  # for each pt we have a list of challenges
        # We will only save while we already have all challenges registered.
        for c in self.active_challenges:
            c_dict = {}  # each challenge stores its progress in a dict
            c.save_progress(c_dict)
            pt_challenges.append(c_dict)  # add the dict to the list
        save_dict[str(self.playthrough_index)] = pt_challenges  # overwrite the current pt challenges with new ones

    def load_challenges(self, save_dict: dict, new_pt=None) -> None:
        """
        Loads the current challenges.
        """
        self.remove_current_challenges()  # Remove all current challenges, we will get new ones
        if new_pt is None:
            pt_challenges = save_dict.get(str(self.playthrough_index), [])
        else:
            pt_challenges = save_dict.get(str(new_pt), [])
        for c_dict in pt_challenges:  # type: dict
            c = KEY_TO_CHALLENGE[list(c_dict.keys())[0]]()  # Create a new Challenge Object
            c.load_progress(c_dict)  # Load the progress
            c.activate()
            self.active_challenges.append(c)


ChallengeManagerInstance: ChallengeManager = ChallengeManager()
