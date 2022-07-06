from math import sqrt

import unrealsdk


class Dash:
    DASH_SOUND1: str = "Ake_Wep_SMGs.SMG_Tediore.Ak_Play_Wep_SMG_Tediore_Shot_Release"
    DASH_SOUND2: str = "Ake_Wep_Sniper_Rifle.Sniper_Hyperion.Ak_Play_Wep_Sniper_Hyperion_Reload_Back"

    SCREEN_PARTICLE: str = "FX_INT_Screen.Particles.Char_Assassin.Part_Assassin_Screen_Dash"

    def __init__(self):
        self.first_dash = False
        self.second_dash = False
        self.dash_cooldown = 0
        self.dash_duration = 0
        self.dash_dir = (0, 0, 0)
        self.b_needs_stop_dash = False

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

        def impl():
            self.add_screen_particles(pc)
            pawn.PlayAkEvent(unrealsdk.FindObject("AkEvent", self.DASH_SOUND1))
            pawn.PlayAkEvent(unrealsdk.FindObject("AkEvent", self.DASH_SOUND2))
            self.b_needs_stop_dash = True
            self.dash_duration = 0.15
            self.dash_dir = ((_x / mag) * 6500, (_y / mag) * 6500, 0)

        if not self.first_dash:  # Dash once
            self.first_dash = True
            self.dash_cooldown = 1.5  # Dash cooldown starts after initial dash
            impl()
        elif not self.second_dash and self.dash_duration <= 0:  # Dash the second time after first dash is done
            self.second_dash = True
            impl()

    def tick_dash(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        pawn = caller.Pawn
        if pawn is None:
            return True
        unrealsdk.CallPostEdit(False)

        self.dash_cooldown -= params.DeltaTime
        self.dash_duration -= params.DeltaTime

        # Check for dash cooldown
        if self.dash_cooldown <= 0:
            self.dash_cooldown = 0
            if pawn.IsOnGroundOrShortFall and pawn.IsOnGroundOrShortFall():  # Reset dash on ground only
                self.first_dash = False
                self.second_dash = False

        if self.dash_duration <= 0:
            self.dash_duration = 0
            if self.b_needs_stop_dash:
                self.b_needs_stop_dash = False
                self.remove_screen_particles(caller)
                _x, _y = pawn.Velocity.X, pawn.Velocity.Y
                mag = sqrt(_x ** 2 + _y ** 2)
                pawn.Velocity = ((_x / mag) * 200, (_y / mag) * 200, 0)
            return True
        pawn.Velocity = self.dash_dir
        unrealsdk.CallPostEdit(True)
        return True

    def add_screen_particles(self, pc: unrealsdk.UObject) -> None:
        particle_params = (
            unrealsdk.FindObject("ParticleSystem", self.SCREEN_PARTICLE),  # Template
            [],  # ScreenParticleModifiers
            None,  # TemplateScreenParticleMaterial
            "",  # MatParamName
            True,  # bHideWhenFinished
            "",  # ParticleTag
            (16, 9),  # ContentDims
            20,  # ParticleDepth
            4,  # ScalingMode
            (),  # StopParamsOT
            True  # bOnlyOwnerSee
        )
        pc.ShowScreenParticle(particle_params)

    def remove_screen_particles(self, pc: unrealsdk.UObject) -> None:
        pc.HideScreenParticle(unrealsdk.FindObject("ParticleSystem", self.SCREEN_PARTICLE), "", False)

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

        unrealsdk.LoadPackage("GD_Assassin_Streaming_SF")
        unrealsdk.KeepAlive(unrealsdk.FindObject("ParticleSystem", self.SCREEN_PARTICLE))

    def disable(
            self
    ) -> None:
        unrealsdk.RemoveHook("WillowGame.WillowPlayerController.PlayerTick", "EternalDash")
        unrealsdk.RemoveHook("WillowGame.WillowPlayerInput.SprintPressed", "EternalDashInput")


dash = Dash()
