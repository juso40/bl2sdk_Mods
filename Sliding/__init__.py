import unrealsdk  # type: ignore

from Mods.ModMenu import EnabledSaveType, Game, Hook, ModTypes, SDKMod
from Mods.tweens import (
    Tween,
    circ_out,
    cubic_in_out,
    cubic_out,
    elastic_out,
    quad_out,
)
from Mods.uemath import Vector


class Sliding(SDKMod):
    Name: str = "Sliding"
    Description: str = "Sliding in BL2."
    Author: str = "Juso"
    Version: str = "2.2"
    Types: ModTypes = ModTypes.Gameplay
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadWithSettings
    SupportedGames: Game = Game.BL2 | Game.AoDK | Game.TPS

    def __init__(self):
        self.do_slide_jump: bool = False
        self.horizontal_velocity: Vector = Vector()
        self.slide_speed: float = 2.2
        self.old_z: float = 0
        self.is_sliding: bool = False
        self.tweener: Tween = Tween()

    def tween_slide(self, pc: unrealsdk.UObject) -> None:
        if self.tweener.is_running():
            self.tweener.kill()
        arms = pc.Pawn.Arms
        if not arms.Attachments:
            return
        self.tweener = Tween()
        t = self.tweener
        t.tween_property(
            arms.SkeletalMesh.RotOrigin,
            "Pitch",
            final_value=500,
            duration=0.2,
        ).from_current().transition(cubic_in_out)
        t.tween_property(
            arms.SkeletalMesh.RotOrigin,
            "Yaw",
            final_value=-200,
            duration=0.4,
        ).from_current().transition(quad_out)
        t.tween_property(
            arms.SkeletalMesh.RotOrigin,
            "Roll",
            final_value=-6300,
            duration=0.5,
        ).from_current().transition(cubic_out)
        t.tween_property(
            arms.SkeletalMesh.Origin,
            "X",
            final_value=30,
            duration=1.2,
        ).from_current().transition(elastic_out)
        t.tween_property(
            arms.SkeletalMesh.Origin,
            "Y",
            final_value=-14.5,
            duration=0.5,
        ).from_current().transition(circ_out)
        t.tween_property(
            arms.SkeletalMesh.Origin,
            "Z",
            final_value=-175,
            duration=0.5,
        ).from_current().transition(circ_out)
        t.set_parallel(True)
        t.start()

    def tween_reset(self, pc: unrealsdk.UObject) -> None:
        if self.tweener.is_running():
            self.tweener.kill()
        arms = pc.Pawn.Arms
        if not arms.Attachments:
            return
        self.tweener = Tween()
        t = self.tweener
        self.tweener = Tween()
        t = self.tweener
        t.tween_property(
            arms.SkeletalMesh.RotOrigin,
            "Pitch",
            final_value=0,
            duration=0.5,
        ).from_current().transition(cubic_in_out)
        t.tween_property(
            arms.SkeletalMesh.RotOrigin,
            "Yaw",
            final_value=0,
            duration=0.4,
        ).from_current().transition(quad_out)
        t.tween_property(
            arms.SkeletalMesh.RotOrigin,
            "Roll",
            final_value=0,
            duration=0.3,
        ).from_current().transition(cubic_in_out)
        t.tween_property(
            arms.SkeletalMesh.Origin,
            "X",
            final_value=40,
            duration=0.4,
        ).from_current().transition(circ_out)
        t.tween_property(
            arms.SkeletalMesh.Origin,
            "Y",
            final_value=0,
            duration=0.6,
        ).from_current().transition(circ_out)
        t.tween_property(
            arms.SkeletalMesh.Origin,
            "Z",
            final_value=-167,
            duration=0.5,
        ).from_current().transition(circ_out)
        t.set_parallel(True)
        t.start()

    def exit_slide(self, pc: unrealsdk.UObject) -> None:
        if not self.is_sliding:
            return
        self.is_sliding = False
        self.slide_speed = 2.2
        unrealsdk.CallPostEdit(False)
        pc.Pawn.CrouchedPct = 0.5
        unrealsdk.CallPostEdit(True)
        self.tween_reset(pc)

    def enter_slide(self, pc: unrealsdk.UObject) -> None:
        if self.is_sliding:
            return
        self.is_sliding = True
        self.old_z = pc.Pawn.Location.Z
        self.slide_speed = 2.2
        unrealsdk.CallPostEdit(False)
        pc.Pawn.CrouchedPct = self.slide_speed
        unrealsdk.CallPostEdit(True)
        self.tween_slide(pc)

    def slide(
        self,
        pc: unrealsdk.UObject,
        delta_time: float,
    ) -> None:
        # z_diff is the height difference between the current frame and the last frame in cm (Unreal units)
        z_diff: float = pc.Pawn.Location.Z - self.old_z

        # We generally want to slow down over time, but if we are going up a slope, we want to slow down even more
        # Slididng down a slope should slightly increase the speed
        if z_diff < 0:  # We are going down a slope
            self.slide_speed -= z_diff * 0.0005
        else:  # We are going up a slope or on flat ground
            self.slide_speed -= delta_time * 0.7 + z_diff * 0.004

        self.old_z = pc.Pawn.Location.Z
        pc.Pawn.CrouchedPct = self.slide_speed

    def can_slide(self, pc: unrealsdk.UObject, pawn: unrealsdk.UObject) -> bool:
        accel = pawn.Acceleration
        return (
            self.is_sliding
            and pc.bDuck
            and pawn.IsOnGroundOrShortFall()
            and not (accel.X == 0.0 and accel.Y == 0.0)
        )

    @Hook("WillowGame.WillowPlayerInput.Jump")
    def jump(
        self,
        caller: unrealsdk.UObject,
        function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ) -> bool:
        if self.is_sliding:
            pc = caller.Outer
            vel: Vector = Vector(pc.Pawn.Velocity)
            vel.z = 0
            self.horizontal_velocity = vel
            self.do_slide_jump = True
        return True

    @Hook("WillowGame.WillowPlayerController.PlayerWalking.PlayerMove")
    def handle_move(
        self,
        caller: unrealsdk.UObject,
        function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ):
        pc: unrealsdk.UObject = caller
        pawn: unrealsdk.UObject = pc.Pawn

        # We most likely wont pass our slide exit conditions after pressing jump,
        # as that will cause the player to stand up
        # So we need to do the slide jump as one of the first things.
        if self.do_slide_jump:
            if pawn.IsOnGroundOrShortFall():
                pawn.DoJump(True)
            else:
                self.do_slide_jump = False

                unrealsdk.CallPostEdit(False)
                pawn.Velocity.X = self.horizontal_velocity.x
                pawn.Velocity.Y = self.horizontal_velocity.y
                unrealsdk.CallPostEdit(True)
                return True

        # Check our exit conditions
        if not self.can_slide(pc, pawn):
            self.exit_slide(pc)
            return True

        # We are sliding
        # If we dont call CallPostEdit(False) we will for whatever reason remove all status effects from the player
        unrealsdk.CallPostEdit(False)
        self.slide(pc, params.DeltaTime)
        unrealsdk.CallPostEdit(True)

        # After actually sliding, check if we are still fast enough to slide
        if self.slide_speed < 0.5:
            self.exit_slide(pc)
        return True

    @Hook("WillowGame.WillowPlayerInput.DuckPressed")
    def handle_duck(
        self,
        caller: unrealsdk.UObject,
        function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ):
        pc = caller.Outer
        if pc.bInSprintState:
            self.enter_slide(pc)
        return True


unrealsdk.RegisterMod(Sliding())
