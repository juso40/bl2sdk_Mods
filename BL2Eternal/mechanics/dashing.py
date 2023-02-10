from math import sqrt

import unrealsdk

from Mods.coroutines import TickCoroutine, Time, WaitForSeconds, WaitWhile, start_coroutine_tick


def _wait_for_pawn_on_ground() -> bool:
    pc = unrealsdk.GetEngine().GamePlayers[0].Actor
    pawn = pc.Pawn
    return pc.IsPaused() or not pawn.IsOnGroundOrShortFall()


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
        self.b_dash_particles = True
        self.enabled = False

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
            self.dash(pc)
        return True

    def dash(self, pc: unrealsdk.UObject) -> None:
        pawn = pc.Pawn

        x, y = pawn.Acceleration.X, pawn.Acceleration.Y
        mag = sqrt(x ** 2 + y ** 2)
        if mag == 0:  # No directional input, so don't dash
            return

        def impl():
            if self.b_dash_particles:
                self.add_screen_particles(pc)
            pawn.PlayAkEvent(unrealsdk.FindObject("AkEvent", self.DASH_SOUND1))
            pawn.PlayAkEvent(unrealsdk.FindObject("AkEvent", self.DASH_SOUND2))
            self.dash_duration = 0.15
            self.dash_dir = ((x / mag) * 6500, (y / mag) * 6500, 0)
            start_coroutine_tick(self.coroutine_tick_dash())

        if not self.first_dash:  # Dash once
            self.first_dash = True
            self.dash_cooldown = 1.5  # Dash cooldown starts after initial dash
            impl()
            start_coroutine_tick(self.coroutine_tick_cooldown())
        elif not self.second_dash and self.dash_duration <= 0:  # Dash the second time after first dash is done
            self.second_dash = True
            impl()

    def coroutine_tick_cooldown(self) -> TickCoroutine:
        yield WaitForSeconds(self.dash_cooldown)  # Wait for dash cooldown
        yield WaitWhile(_wait_for_pawn_on_ground)  # Reset once the player is on ground
        self.dash_cooldown = 0
        self.first_dash = False
        self.second_dash = False
        return None

    def coroutine_tick_dash(self) -> TickCoroutine:
        while True:
            # Wait for pause menu to close
            yield WaitWhile(lambda: unrealsdk.GetEngine().GamePlayers[0].Actor.IsPaused())
            self.dash_duration -= Time.delta_time
            pc = unrealsdk.GetEngine().GamePlayers[0].Actor
            pawn = pc.Pawn
            unrealsdk.CallPostEdit(False)
            pawn.Velocity = self.dash_dir

            # Break this coroutine if our dash duration is over
            if self.dash_duration <= 0:
                self.dash_duration = 0
                self.remove_screen_particles(pc)
                _x, _y = pawn.Velocity.X, pawn.Velocity.Y
                mag = sqrt(_x ** 2 + _y ** 2)
                pawn.Velocity = ((_x / mag) * 200, (_y / mag) * 200, -10)  # Slight Downward velocity because of TPS
                unrealsdk.CallPostEdit(True)
                return None
            unrealsdk.CallPostEdit(True)

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
            "WillowGame.WillowPlayerInput.SprintPressed",
            "EternalDashInput",
            lambda c, f, p: self.wants_to_dash(c, f, p)
        )

        if self.b_dash_particles:
            unrealsdk.LoadPackage("GD_Assassin_Streaming_SF")
            unrealsdk.KeepAlive(unrealsdk.FindObject("ParticleSystem", self.SCREEN_PARTICLE))

    def disable(
            self
    ) -> None:
        unrealsdk.RemoveHook("WillowGame.WillowPlayerInput.SprintPressed", "EternalDashInput")

    def enable_dash_particle(self, val: bool) -> None:
        self.b_dash_particles = val
        if val:
            unrealsdk.LoadPackage("GD_Assassin_Streaming_SF")
            unrealsdk.KeepAlive(unrealsdk.FindObject("ParticleSystem", self.SCREEN_PARTICLE))


dash = Dash()
