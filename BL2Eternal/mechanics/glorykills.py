import unrealsdk


class GloryKill:
    glory_killed = []

    GLORY_KILL_AK_EVENT1 = "Ake_UI.UI_Shields.Ak_Play_UI_Shield_Roid_Buff_Hit"
    GLORY_KILL_AK_EVENT2 = "Ake_UI.UI_HUD.Ak_Play_UI_PVP_Duel_End"
    GLORY_KILL_MARKER1 = "FX_GOR_Particles.Particles.DeathFX.Part_FireDeath_Small"
    GLORY_KILL_MARKER2 = "FX_GOR_Particles.Particles.DeathFX.Part_ShockDeath_Large"
    GLORY_KILL_KILLED_PARTICLE = "FX_WEP_Explosions.Particles.Default.Part_ExplosiveExplosion_Small"

    def on_take_damage(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        if not caller.IsInjured():
            return True
        if not params.Pipeline or "Melee" not in caller.PathName(params.Pipeline.ImpactDefinition):
            return True

        emitter_pool = unrealsdk.GetEngine().GetCurrentWorldInfo().MyEmitterPool

        hit_loc = params.HitLocation
        hit_loc = (hit_loc.X, hit_loc.Y, hit_loc.Z)

        emitter_pool.SpawnEmitter(
            unrealsdk.FindObject("ParticleSystem", self.GLORY_KILL_KILLED_PARTICLE),
            hit_loc,
        )

        instigator = params.InstigatedBy
        instigator.PlayAkEvent(unrealsdk.FindObject("AkEvent", self.GLORY_KILL_AK_EVENT1))
        instigator.PlayAkEvent(unrealsdk.FindObject("AkEvent", self.GLORY_KILL_AK_EVENT2))
        if instigator.Pawn:
            instigator.Pawn.SetHealth(instigator.Pawn.GetMaxHealth())
        self.glory_killed.append(caller.PathName(caller))
        caller.SetHealth(1)
        return True

    def enter_glory_kill_state(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        if not caller.MyWillowPawn.IsInjured():
            return True

        emitter_pool = unrealsdk.GetEngine().GetCurrentWorldInfo().MyEmitterPool
        emitter_pool.SpawnEmitterMeshAttachment(
            unrealsdk.FindObject("ParticleSystem", self.GLORY_KILL_MARKER1),
            caller.MyWillowPawn.Mesh,
            "root"
        )
        emitter_pool.SpawnEmitterMeshAttachment(
            unrealsdk.FindObject("ParticleSystem", self.GLORY_KILL_MARKER2),
            caller.MyWillowPawn.Mesh,
            "root"
        )

        return True

    def drop_loot_on_death(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        try:
            self.glory_killed.remove(caller.PathName(caller))
            unrealsdk.Log("Dop some loot")
            for _ in range(9):
                caller.DropLootOnDeath(params.Killer, params.DamageType, params.DamageTypeDefinition)
        except ValueError:
            pass
        return True

    def enable(
            self
    ) -> None:
        unrealsdk.RegisterHook(
            "WillowGame.WillowAIPawn.TakeDamage",
            "GloryKillTakeDamage",
            lambda c, f, p: self.on_take_damage(c, f, p)
        )
        unrealsdk.RegisterHook(
            "WillowGame.WillowMind.NotifyAttackedBy",
            "GloryKillState",
            lambda c, f, p: self.enter_glory_kill_state(c, f, p)
        )
        unrealsdk.RegisterHook(
            "WillowGame.WillowPawn.DropLootOnDeath",
            "GloryKillLoot",
            lambda c, f, p: self.drop_loot_on_death(c, f, p)
        )

    def disable(
            self
    ) -> None:
        unrealsdk.RemoveHook("WillowGame.WillowAIPawn.TakeDamage", "GloryKillTakeDamage")
        unrealsdk.RemoveHook("WillowGame.WillowMind.NotifyAttackedBy", "GloryKillState")
        unrealsdk.RemoveHook("WillowGame.WillowPawn.DropLootOnDeath", "GloryKillLoot")


glory_kill = GloryKill()
