from dataclasses import dataclass
from typing import Any, List, Optional

import unrealsdk  # type: ignore

from Mods.ModMenu import EnabledSaveType, Game, Hook, OptionManager, RegisterMod, SDKMod


def dist(a, b):
    return ((a.X - b.X) ** 2 + (a.Y - b.Y) ** 2 + (a.Z - b.Z) ** 2) ** 0.5


blacklist = [
    "GD_Tulip_DeathTrap.Character.CharClass_DeathTrap",
    "GD_Scorpio.Character.CharClass_Scorpio",
    "GD_RolandDeployableTurret.Character.CharClass_RolandDeployableTurret",
    "GD_Anemone_Talon.Character.CharClass_Bloodwing",
    "GD_Nasturtium_BugMorph_Bloodhound.Character.CharClass_Nasturtium_BugMorph_Bloodhound",
]


@dataclass
class NPCHero:
    mind: unrealsdk.UObject
    scripted_stance: int
    stop_sequence: bool


class NPCRevives(SDKMod):
    Name = "NPC Revives"
    Description = "Get revived from friendly NPCs."
    Author = "Juso"
    Version = "1.1"
    SaveEnabledState = EnabledSaveType.LoadWithSettings
    SupportedGames = Game.TPS | Game.BL2 | Game.AoDK

    def __init__(self):
        super(NPCRevives, self).__init__()
        self.injured_target: Optional[unrealsdk.UObject] = None

        self.revive_max_dist: int = 300
        self.revive_alert_dist: int = 5000

        self.max_reviving_npcs: int = 5
        self.reviving_npcs: List[NPCHero] = []

        self.Options = [
            OptionManager.Options.Slider(
                Caption="Revive Distance",
                Description="The distance at which NPCs will revive you. 100 is roughly 1m.",
                StartingValue=self.revive_max_dist,
                MinValue=100,
                MaxValue=500,
                Increment=10,
            ),
            OptionManager.Options.Slider(
                Caption="Revive Alert Distance",
                Description="The distance at which NPCs will alert you to revive you. 100 is roughly 1m.",
                StartingValue=self.revive_alert_dist,
                MinValue=500,
                MaxValue=5000,
                Increment=50,
            ),
            OptionManager.Options.Slider(
                Caption="Max Reviving NPCs",
                Description="The maximum number of NPCs that will try to revive you at once.",
                StartingValue=self.max_reviving_npcs,
                MinValue=1,
                MaxValue=10,
                Increment=1,
            ),
        ]

    def ModOptionChanged(  # noqa: N802
        self, option: OptionManager.Options.Base, new_value: Any
    ) -> None:
        if option.Caption == "Revive Distance":
            self.revive_max_dist = new_value
        elif option.Caption == "Revive Alert Distance":
            self.revive_alert_dist = new_value
        elif option.Caption == "Max Reviving NPCs":
            self.max_reviving_npcs = new_value

    def in_revive_dist(self, reviver_pawn: unrealsdk.UObject) -> bool:
        if not self.injured_target:
            return False

        return (
            dist(reviver_pawn.Location, self.injured_target.Location)
            < self.revive_max_dist
        )

    def start_injured_self_revive(self) -> None:
        if not self.injured_target:
            return

        self.injured_target.Controller.ReviveTarget = self.injured_target
        if Game.GetCurrent() == Game.TPS:
            self.injured_target.SetBeingRevived(True, self.injured_target, False)
        else:
            self.injured_target.SetBeingRevived(True, self.injured_target)

    def force_move_npcs(self) -> None:
        if not self.injured_target:
            return

        for npc in self.reviving_npcs:
            npc.mind.ScriptedStance = 2  # Sprint
            npc.mind.ScriptedFocusStyle = 1  # Focus on injured target
            npc.mind.ForceMoveToActor(self.injured_target)

    @Hook("WillowGame.WillowPlayerPawn.SetupPlayerInjuredState")
    def player_injured(
        self,
        caller: unrealsdk.UObject,
        function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ) -> bool:
        """Player goes into FFYL state."""

        all_minds = unrealsdk.FindAll("WillowMind")[1:]
        friendly_minds = [
            x for x in all_minds if x.MyWillowPawn and x.MyWillowPawn.IsFriendly(caller)
        ]
        friendly_minds = [
            x for x in friendly_minds if x.PathName(x.AIClass) not in blacklist
        ]
        if not friendly_minds:
            return True
        closest = sorted(
            friendly_minds, key=lambda x: dist(x.MyWillowPawn.Location, caller.Location)
        )
        closest = [
            x
            for x in closest
            if dist(x.MyWillowPawn.Location, caller.Location) < self.revive_alert_dist
        ]
        if not closest:
            return True

        self.reviving_npcs = [
            NPCHero(mind=x, scripted_stance=x.ScriptedStance, stop_sequence=True)
            for x in closest[: self.max_reviving_npcs]
        ]

        # Set the Injured WillowPlayerPawn as the new target
        self.injured_target = caller

        # Force the closest WillowMind to move to the injured WillowPlayerPawn
        self.force_move_npcs()

        return True

    @Hook("WillowGame.WillowPlayerPawn.injured.Tick")
    def tick_dist_check(
        self,
        caller: unrealsdk.UObject,
        function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ) -> bool:
        """Player is in FFYL state."""

        if caller is self.injured_target:
            # Make sure NPCs still move to player
            self.force_move_npcs()

            # Check if any NPC is close enough to revive
            if any(
                self.in_revive_dist(x.mind.MyWillowPawn) for x in self.reviving_npcs
            ):
                self.start_injured_self_revive()
        return True

    @Hook("WillowGame.WillowPlayerPawn.ClearPlayerInjuredState")
    def stop_injured(
        self,
        caller: unrealsdk.UObject,
        function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ) -> bool:
        """Player leaves FFYL state."""

        # NPCs can only revive one player at a time.
        if caller is not self.injured_target:
            return True

        # If a WillowMind is tasked to revive us, clear it
        for npc in self.reviving_npcs:
            npc.mind.ClearScriptedMove(True)
            npc.mind.ScriptedStance = npc.scripted_stance
            npc.mind.AIComponent.ActivateEvent("Scripted")
            npc.mind.CheckForPerch(False, True)

        self.reviving_npcs = []
        self.injured_target = None
        return True

    @Hook("WillowGame.Action_GoToScriptedDestination.SetMoveNode")
    def cancel_move_nodes(
        self,
        caller: unrealsdk.UObject,
        function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ) -> bool:
        """Cancel move nodes for our reviving NPC."""

        if caller.MyWillowMind in [x.mind for x in self.reviving_npcs]:
            self.force_move_npcs()
            # Cancel the next move nodes, instead revive us!
            return False
        return True

    @Hook("GearboxFramework.ActionSequence.Update")
    def update_action_sequence(
        self,
        caller: unrealsdk.UObject,
        function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ) -> bool:
        """Wake up idling NPCs."""
        if not self.reviving_npcs:
            return True

        if caller.MyWillowMind not in [x.mind for x in self.reviving_npcs]:
            return True

        # Update all reviving NPCs
        for npc in self.reviving_npcs:
            if caller.MyWillowMind is npc.mind and npc.stop_sequence:
                npc.stop_sequence = False
                caller.InterruptLatentAction()
                caller.StopSequence()
                caller.Stop()
                caller.Start()

        self.force_move_npcs()
        return True


RegisterMod(NPCRevives())
