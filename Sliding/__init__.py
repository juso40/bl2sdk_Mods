import unrealsdk
from unrealsdk import *

from . import bl2tools


class Sliding(unrealsdk.BL2MOD):
    Name = "Sliding"
    Description = "Sliding in BL2."
    Author = "Juso"

    def __init__(self):
        self.slide_duration = 2.0
        self.slide_speed = 2.2
        self.old_z = 0
        self.b_update = False

    def handle_move(self, caller, function, params):
        pc = bl2tools.get_player_controller()
        slope_delta = pc.Pawn.Location.Z - self.old_z

        if slope_delta / params.DeltaTime > 2.0:
            self.slide_duration -= (params.DeltaTime * 1.3)

        elif slope_delta / params.DeltaTime < -2.0:  # down
            self.slide_duration -= (params.DeltaTime / 2)

        else:
            self.slide_duration -= params.DeltaTime

        if pc.bDuck == 1 and self.slide_duration > 0.:

            pc.Rotation.Roll = 700
            pc.Pawn.CrouchedPct = 2.1
            self.slide_duration -= params.DeltaTime


        elif pc.bDuck != 1 or self.slide_duration <= 0.:
            pc.Rotation.Roll = 0
            pc.Pawn.CrouchedPct = 0.42

        self.old_z = pc.Pawn.Location.Z

    def handle_duck(self, caller, function, params):
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

    def Enable(self):
        def DoSlide(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            # self.handle_duck(caller, function, params)
            return True

        def AdvancedMove(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            # self.handle_move(caller, function, params)
            Log("Ayy")

            return True

        unrealsdk.RegisterHook("WillowGame.WillowPlayerInput.DuckPressed", "SlideHook", DoSlide)
        unrealsdk.RegisterHook("Engine.PlayerController.PCServerMoveInner", "MoveHook", AdvancedMove)

    def Disable(self):
        unrealsdk.RemoveHook("WillowGame.WillowPlayerInput.DuckPressed", "SlideHook")
        unrealsdk.RemoveHook("Engine.PlayerController.PCServerMoveInner", "MoveHook")


unrealsdk.RegisterMod(Sliding())
