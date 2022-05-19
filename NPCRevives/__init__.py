from typing import Optional

import unrealsdk

from ..ModMenu import EnabledSaveType, SDKMod, Hook, Game


def dist(a, b):
    return ((a.X - b.X) ** 2 + (a.Y - b.Y) ** 2 + (a.Z - b.Z) ** 2) ** 0.5


class NPCRevives(SDKMod):
    Name = "NPC Revives"
    Description = "Get revived from friendly NPCs."
    Author = "Juso"
    Version = "1.0"
    SaveEnabledState = EnabledSaveType.LoadWithSettings
    SupportedGames = Game.TPS | Game.BL2 | Game.AoDK

    def __init__(self):
        super(NPCRevives, self).__init__()
        self.reviving_mind: Optional[unrealsdk.UObject] = None

    def Enable(self):
        super().Enable()

    def Disable(self):
        super().Disable()

    def start_self_revive(self):
        pc = unrealsdk.GetEngine().GamePlayers[0].Actor
        pc.ReviveTarget = pc.Pawn
        if Game.GetCurrent() == Game.TPS:
            pc.Pawn.SetBeingRevived(True, pc.Pawn, False)
        else:
            pc.Pawn.SetBeingRevived(True, pc.Pawn)

    @Hook("WillowGame.WillowPlayerPawn.SetupPlayerInjuredState")
    def player_injured(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        all_minds = unrealsdk.FindAll("WillowMind")[1:]
        friendly_minds = [x for x in all_minds if x.MyWillowPawn.IsFriendly(caller)]
        closest = sorted(friendly_minds, key=lambda x: dist(x.MyWillowPawn.Location, caller.Location))[0]

        # 50m radius
        if dist(closest.MyWillowPawn.Location, caller.Location) > 5000:
            return True

        self.reviving_mind = closest
        closest.ForceMoveToActor(caller)
        closest.MyWillowPawn.SetSprinting(True)
        if dist(closest.MyWillowPawn.Location, caller.Location) < 100:
            self.start_self_revive()

        return True

    @Hook("WillowGame.WillowActionSequencePawn.ReachedDestination")
    def reached_player(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        if caller.MyWillowMind is not self.reviving_mind:
            return True

        pc = unrealsdk.GetEngine().GamePlayers[0].Actor
        # Revive if closer than 1m
        if dist(caller.MyWillowPawn.Location, pc.Pawn.Location) < 100:
            self.start_self_revive()
        return True

    @Hook("WillowGame.WillowPlayerController.ClearControllerInjuredState")
    def stop_injured(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        if self.reviving_mind:
            self.reviving_mind.ClearScriptedMove(True)
            self.reviving_mind.AIComponent.ActivateEvent("Scripted")
        self.reviving_mind = None
        return True


unrealsdk.RegisterMod(NPCRevives())
