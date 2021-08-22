import unrealsdk
from unrealsdk import *

from ..ModMenu import SDKMod, Hook, EnabledSaveType, ModTypes

from . import bl2tools


class Sliding(SDKMod):
    Name = "Sliding"
    Description = "Sliding in BL2."
    Author = "Juso"
    Version = "2.0"
    Types = ModTypes.Gameplay
    SaveEnabledState = EnabledSaveType.LoadOnMainMenu

    def __init__(self):
        self.slide_duration = 2.0
        self.slide_speed = 2.2
        self.old_z = 0
        self.b_update = False

    @Hook("WillowGame.WillowPlayerController.PlayerWalking.PlayerMove")
    def handle_move(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct):
        pc = bl2tools.get_player_controller()

        slope_delta = pc.Pawn.Location.Z - self.old_z

        if pc.Pawn.Acceleration.X == 0.0 and pc.Pawn.Acceleration.Y == 0.0:  # turn off sliding
            pc.Pawn.CrouchedPct = self.slide_speed = 0.5

        if slope_delta / params.DeltaTime > 2.0:  # sliding up
            self.slide_duration -= (params.DeltaTime * 1.3)

        elif slope_delta / params.DeltaTime < -2.0:  # down
            self.slide_duration -= (params.DeltaTime / 5)

        else:
            self.slide_duration -= params.DeltaTime

        if pc.bDuck and self.slide_duration > 0.:

            pc.Rotation.Roll = int(self.slide_duration * 700)
            pc.Pawn.CrouchedPct = 2.1
            self.slide_duration -= params.DeltaTime

        elif not pc.bDuck or self.slide_duration <= 0.:  # stopped duck or time over
            pc.Rotation.Roll = 0
            pc.Pawn.CrouchedPct = 0.5

        self.old_z = pc.Pawn.Location.Z
        return True

    @Hook("WillowGame.WillowPlayerInput.DuckPressed")
    def handle_duck(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct):
        pc = bl2tools.get_player_controller()
        self.old_z = pc.Pawn.Location.Z
        if pc.bInSprintState:
            self.slide_duration = 2.0
            if pc.bCrouchToggle:
                if caller.bHoldDuck:
                    self.b_update = True
                    caller.bHoldDuck = False
                    pc.bDuck = 0
                    return False
                else:
                    self.b_update = True
                    caller.bHoldDuck = True
                    pc.bDuck = 1
                return False
            else:
                self.b_update = True
                pc.bDuck = 1
                return False
        else:
            return True


unrealsdk.RegisterMod(Sliding())
