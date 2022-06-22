from math import sqrt

import unrealsdk


class Dash:
    DASH_COOLDOWN: float = 0
    DASH_DURATION: float = 0
    DASH_DIR: tuple = (0, 0, 0)
    B_NEEDS_STOP_DASH: bool = False

    DASH_SOUND1: str = "Ake_Wep_SMGs.SMG_Tediore.Ak_Play_Wep_SMG_Tediore_Shot_Release"
    DASH_SOUND2: str = "Ake_Wep_Sniper_Rifle.Sniper_Hyperion.Ak_Play_Wep_Sniper_Hyperion_Reload_Back"

    def wants_to_dash(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        pc = caller.Outer
        if not pc.Pawn:
            return True

        # Only allow dash while in air
        if not pc.Pawn.IsOnGroundOrShortFall():
            self.dash()
        return True

    def dash(self) -> None:
        pc = unrealsdk.GetEngine().GamePlayers[0].Actor
        pawn = pc.Pawn
        if pawn is None:
            return

        _x, _y = pawn.Acceleration.X, pawn.Acceleration.Y
        mag = sqrt(_x ** 2 + _y ** 2)
        if mag == 0:
            return

        if self.DASH_COOLDOWN <= 0:
            pawn.PlayAkEvent(unrealsdk.FindObject("AkEvent", self.DASH_SOUND1))
            pawn.PlayAkEvent(unrealsdk.FindObject("AkEvent", self.DASH_SOUND2))
            self.B_NEEDS_STOP_DASH = True
            self.DASH_COOLDOWN = 1.5
            self.DASH_DURATION = 0.15
            self.DASH_DIR = ((_x / mag) * 6500, (_y / mag) * 6500, 0)

    def tick_dash(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        pawn = caller.Pawn
        if pawn is None:
            return True
        self.DASH_COOLDOWN -= params.DeltaTime
        self.DASH_DURATION -= params.DeltaTime
        if self.DASH_COOLDOWN <= 0:
            self.DASH_COOLDOWN = 0
        if self.DASH_DURATION <= 0:
            self.DASH_DURATION = 0
            if self.B_NEEDS_STOP_DASH:
                self.B_NEEDS_STOP_DASH = False
                _x, _y = pawn.Velocity.X, pawn.Velocity.Y
                mag = sqrt(_x ** 2 + _y ** 2)
                pawn.Velocity = ((_x / mag) * 200, (_y / mag) * 200, 0)
            return True

        pawn.Velocity = self.DASH_DIR
        return True

    def enable(
            self
    ) -> None:
        unrealsdk.RegisterHook(
            "WillowGame.WillowPlayerController.PlayerTick",
            "EternalDash",
            lambda c, f, p: self.tick_dash(c, f, p)
        )
        unrealsdk.RegisterHook(
            "WillowGame.WillowPlayerInput.SprintPressed",
            "EternalDashInput",
            lambda c, f, p: self.wants_to_dash(c, f, p)
        )

    def disable(
            self
    ) -> None:
        unrealsdk.RemoveHook("WillowGame.WillowPlayerController.PlayerTick", "EternalDash")
        unrealsdk.RemoveHook("WillowGame.WillowPlayerInput.SprintPressed", "EternalDashInput")


dash = Dash()
