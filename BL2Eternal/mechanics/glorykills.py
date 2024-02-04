import unrealsdk  # type: ignore

BLACKLIST = [
    "bugmorph",
    "snowminion",
]


class GloryKill:
    HEALTH_THRESHOLD = 0.15  # less than 15% health required to be in glory kill state
    GLORY_KILL_AK_EVENT1 = "Ake_UI.UI_Shields.Ak_Play_UI_Shield_Roid_Buff_Hit"
    GLORY_KILL_AK_EVENT2 = "Ake_UI.UI_HUD.Ak_Play_UI_PVP_Duel_End"
    GLORY_KILL_MARKER1 = "FX_GOR_Particles.Particles.DeathFX.Part_FireDeath_Small"
    GLORY_KILL_MARKER2 = "FX_GOR_Particles.Particles.DeathFX.Part_ShockDeath_Large"
    GLORY_KILL_KILLED_PARTICLE = "FX_WEP_Explosions.Particles.Default.Part_ExplosiveExplosion_Small"

    def __init__(self) -> None:
        self.glory_killed = set()
        self.glory_kill_state = {}

    @property
    def emitter_pool(self) -> unrealsdk.UObject:
        return unrealsdk.GetEngine().GetCurrentWorldInfo().MyEmitterPool

    def check_glory_kill_state(self, pawn: unrealsdk.UObject) -> bool:
        if pawn.GetHealth() > 0 and pawn.GetMaxHealth() > 0 and (pawn.GetHealth() / pawn.GetMaxHealth()) < self.HEALTH_THRESHOLD:
            pawn_path_name = pawn.PathName(pawn)
            self.glory_kill_state.setdefault(pawn_path_name, 5)  # Stay 5 seconds in glory kill state
            return self.glory_kill_state[pawn_path_name] > 0  # Only first 5 seconds in glory kill state
        return False

    def on_take_damage(
        self,
        caller: unrealsdk.UObject,
        _function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ) -> bool:
        if not self.check_glory_kill_state(caller):
            return True

        pc = unrealsdk.GetEngine().GamePlayers[0].Actor
        instigator = params.InstigatedBy
        # We only allow Melee damage to kill Pawns in glory kill state
        if not (instigator == pc and "melee" in params.DamageType.Name.lower()):
            return True

        # Store the location the Pawn was hit
        hit_loc = params.HitLocation
        hit_loc = (hit_loc.X, hit_loc.Y, hit_loc.Z)

        # Spawn the glory killed particle to the hit location
        self.emitter_pool.SpawnEmitter(
            unrealsdk.FindObject("ParticleSystem", self.GLORY_KILL_KILLED_PARTICLE),
            hit_loc,
        )

        # Add the sound effects
        instigator = params.InstigatedBy
        instigator.PlayAkEvent(unrealsdk.FindObject("AkEvent", self.GLORY_KILL_AK_EVENT1))
        instigator.PlayAkEvent(unrealsdk.FindObject("AkEvent", self.GLORY_KILL_AK_EVENT2))

        # The instigator gains all it's health back for this glory kill.
        if instigator.Pawn:
            instigator.Pawn.SetHealth(instigator.Pawn.GetMaxHealth())

        # Add the killed Pawn to the set of killed Pawns to later increase the dropped loot.
        self.glory_killed.add(caller.PathName(caller))
        # Set health of Pawn to 1 to kill him with melee damage and not cause soft locks.
        caller.SetHealth(1)
        caller.SetShieldStrength(0)
        return True

    def enter_glory_kill_state(
        self,
        caller: unrealsdk.UObject,
        _function: unrealsdk.UFunction,
        _params: unrealsdk.FStruct,
    ) -> bool:
        if not self.check_glory_kill_state(caller.MyWillowPawn):
            return True

        # Don't allow glory kills on blacklisted enemies
        enemy_name = caller.PathName(caller.MyWillowPawn.AIClass).lower()
        for blacklisted in BLACKLIST:
            if blacklisted in enemy_name:
                return True

        self.emitter_pool.SpawnEmitterMeshAttachment(
            unrealsdk.FindObject("ParticleSystem", self.GLORY_KILL_MARKER1),
            caller.MyWillowPawn.Mesh,
            "root",
        )
        self.emitter_pool.SpawnEmitterMeshAttachment(
            unrealsdk.FindObject("ParticleSystem", self.GLORY_KILL_MARKER2),
            caller.MyWillowPawn.Mesh,
            "root",
        )

        return True

    def drop_loot_on_death(
        self,
        caller: unrealsdk.UObject,
        _function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ) -> bool:
        try:
            self.glory_killed.remove(caller.PathName(caller))
            # Only drop additional loot if the Pawn got glory killed
            for _ in range(4):
                caller.DropLootOnDeath(params.Killer, params.DamageType, params.DamageTypeDefinition)
        except KeyError:
            pass
        return True

    def tick_glory_states(
        self,
        _caller: unrealsdk.UObject,
        _function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ) -> bool:
        # Enemies will stay 5 seconds in glory kill state and then are immune to glory kills for 10 seconds
        for p, t in list(self.glory_kill_state.items()):
            self.glory_kill_state[p] = t - params.DeltaTime  # Decrease the glory kill state timer
            if t < -10:  # 10 seconds immunity to glory kill state
                del self.glory_kill_state[p]  # Remove if time is up
        return True

    def enable(self) -> None:
        unrealsdk.RegisterHook(
            "WillowGame.WillowAIPawn.TakeDamage",
            "GloryKillTakeDamage",
            lambda c, f, p: self.on_take_damage(c, f, p),
        )
        unrealsdk.RegisterHook(
            "WillowGame.WillowMind.NotifyAttackedBy",
            "GloryKillState",
            lambda c, f, p: self.enter_glory_kill_state(c, f, p),
        )
        unrealsdk.RegisterHook(
            "WillowGame.WillowPawn.DropLootOnDeath",
            "GloryKillLoot",
            lambda c, f, p: self.drop_loot_on_death(c, f, p),
        )
        unrealsdk.RegisterHook(
            "WillowGame.WillowPlayerController.PlayerTick",
            "GloryKillStateTick",
            lambda c, f, p: self.tick_glory_states(c, f, p),
        )

    def disable(self) -> None:
        unrealsdk.RemoveHook("WillowGame.WillowAIPawn.TakeDamage", "GloryKillTakeDamage")
        unrealsdk.RemoveHook("WillowGame.WillowMind.NotifyAttackedBy", "GloryKillState")
        unrealsdk.RemoveHook("WillowGame.WillowPawn.DropLootOnDeath", "GloryKillLoot")
        unrealsdk.RemoveHook("WillowGame.WillowPlayerController.PlayerTick", "GloryKillStateTick")


glory_kill = GloryKill()
