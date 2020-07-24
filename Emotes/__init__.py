import bl2sdk

class Emotes(bl2sdk.BL2MOD):
    Name = "Emotes"
    Description = """Adds emotes to the game that the player can use.
    'Up' = Play Emote
    'Down' = Stop Emote
    'Left'/'Right' = Change Emote
    
    Original idea and method by OurLordAndSaviorGabeNewell"""
    Author = "Juso"

    #Loads the Package requierd for the Animations
    def ForceLoad(self):
        #Needed for the cool Katana moves
        bl2sdk.LoadPackage("GD_Assassin_Streaming_SF")
        bl2sdk.KeepAlive(bl2sdk.FindObject("WillowAnimDefinition", "GD_Assassin_Hologram.SpecialMove.SpecialMove_HologramScrewAround"))
        bl2sdk.KeepAlive(bl2sdk.FindObject("AnimSet", "Anim_Assassin.Base_Assassin"))
        #We dont want these animations to unload
        Objects = [
                "GD_NPCShared.Perches.Perch_NPC_ArmsCrossedForever:SpecialMove_PerchLoop_0",
                "GD_NPCShared.Perches.Perch_NPC_BangOnSomething:SpecialMove_PerchLoop_0",
                "GD_NPCShared.Perches.Perch_NPC_BarrelSitForever:SpecialMove_PerchLoop_0",
                "GD_NPCShared.Perches.Perch_NPC_ChairSitForever:SpecialMove_PerchLoop_0",
                "GD_NPCShared.Perches.Perch_NPC_DartsHit:SpecialMove_PerchLoop_0",
                "GD_NPCShared.Perches.Perch_NPC_KickGround:SpecialMove_PerchLoop_0",
                "GD_NPCShared.Perches.Perch_NPC_LeanOnCounterForever:SpecialMove_PerchLoop_0",
                "GD_NPCShared.Perches.Perch_NPC_LeanOnWallNonRandom:SpecialMove_PerchLoop_0",
                "GD_NPCShared.Perches.Perch_NPC_LookAtGround:SpecialMove_PerchLoop_0",
                "GD_NPCShared.Perches.Perch_NPC_PeerUnder:SpecialMove_PerchLoop_0",
                "GD_Moxxi.Perches.Perch_Moxxi_Dance:SpecialMove_PerchLoop_0",
                "GD_Moxxi.Perches.Perch_Moxxi_WipeBar:SpecialMove_PerchLoop_0",
                "GD_TannisNPC.Perches.Perch_Tannis_HandsOnHips:SpecialMove_PerchLoop_0",
                "GD_BrickNPC.Perches.Perch_Brick_Pushups:SpecialMove_PerchLoop_0"

            ]
        bl2sdk.LoadPackage("SanctuaryAir_Dynamic")
        for Object in Objects:
            x = bl2sdk.FindObject("SpecialMove_PerchLoop", Object)
            bl2sdk.KeepAlive(x)
        #This are our Particles that can be used
        Particles = [
                "FX_ENV_Misc.Particles.Part_Confetti",
                "FX_Distillery.Particles.PS_Hearts_Looping_8-Bit",
                "FX_CHAR_Merc.Particles.Part_Merc_MoneyShotImpact",
                "FX_Distillery.Particles.PS_Nast_Drunk_Thresher"
                ]
        bl2sdk.LoadPackage("Distillery_Dynamic")
        bl2sdk.LoadPackage("Distillery_Mission")
        bl2sdk.LoadPackage("GD_Mercenary_Streaming_SF")
        for Particle in Particles:
            x = bl2sdk.FindObject("ParticleSystem", Particle)
            bl2sdk.KeepAlive(x)

    #Returns the name of the Animation thats played
    _animation = 0
    def ChooseAnimation(self):     
        Animations = [
                "Perch_CoyoteUglyDance_Loop",
                "Perch_WipeBarTop_Loop",
                "Perch_HandsOnHips_Loop",
                "Perch_Pushups_Loop",
                "Perch_MockPunching_Loop",
                "Perch_Sittingonbarrel_Loop",
                "Perch_ThrowDarts_Loop",
                "Kick_Object_on_Ground",
                "Perch_WallLean_Loop",
                "Perch_InspectGround_Loop",
                "Perch_CounterTopLean_Loop",
                "Kick_Object_on_Ground",
                "Perch_PeerUnder_Loop",
                "Perch_ChairSit_Loop",
                "Perch_BangOnWall_Loop",
                "Perch_ArmsCrossed_Loop",
                "Hologram_Kata",
                "FX_ENV_Misc.Particles.Part_Confetti",
                "FX_Distillery.Particles.PS_Hearts_Looping_8-Bit",
                "FX_CHAR_Merc.Particles.Part_Merc_MoneyShotImpact",
                "FX_Distillery.Particles.PS_Nast_Drunk_Thresher"
                ]
        self._animation = self._animation % len(Animations) 
        return Animations[self._animation]
    #Returns the current PlayerController
    def GetPlayerController(self):
        return bl2sdk.GetEngine().GamePlayers[0].Actor
    #Gives Feedback on what animation is choosed
    def FeedbackEmote(self):
        if self.GetPlayerController() != None:
            HUD = self.GetPlayerController().GetHUDMovie()
            HUD.ClearTrainingText()
            HUD.AddTrainingText(self.ChooseAnimation(), "Emote", 3.000000, (), "", False, 0, self.GetPlayerController().PlayerReplicationInfo, True)

    def PlayEmote(self):
        #up to and including index 16 are animations only, after that come ParticleSystems
        if self._animation < 17:
            #We are going to change the animations that are played on melee to play our emotes instead
            SpecialMoves = [
                        "GD_Assassin_Streaming.Anims.WeaponAnim_Melee",
                        "GD_Lilac_Psycho_Streaming.Anims.WeaponAnim_Melee",
                        "GD_Mercenary_Streaming.Anims.WeaponAnim_Melee",
                        "GD_PlayerShared.Anims.WeaponAnim_Melee_WeaponBlade",
                        "GD_Siren_Streaming.Anims.WeaponAnim_Melee",
                        "GD_Soldier_Streaming.Anims.WeaponAnim_Melee",
                        "GD_Tulip_Mechro_Streaming.Anims.WeaponAnim_Melee"
                ]
        
            PC = self.GetPlayerController()
            for Move in SpecialMoves:
                if bl2sdk.FindObject("SpecialMove_WeaponAction", Move) != None:
                    PC.ConsoleCommand("set "+ Move + " AnimName " + self.ChooseAnimation(), 0)
                    PC.ConsoleCommand("set "+ Move + " EndingCondition EC_Loop", 0)
                    #The first 2 animations are Moxxie only
                    if self._animation in (0, 1):
                        PC.ConsoleCommand("set "+ Move + " AnimSet AnimSet'Anim_Moxxi.Anim_Moxxi'", 0)
                    #Index 2 is Tannis only
                    elif self._animation == 2:
                        PC.ConsoleCommand("set "+ Move + " AnimSet AnimSet'Anim_Tannis.Anim_Tannis'", 0)
                    #Index 3, 4 is Brick only
                    elif self._animation in (3, 4):
                        PC.ConsoleCommand("set "+ Move + " AnimSet AnimSet'Anim_Brick.Anim_Brick'", 0)
                        
                    elif self._animation == 16:
                        PC.ConsoleCommand("set "+ Move + " AnimSet AnimSet'Anim_Assassin.Base_Assassin'", 0)
                    else:
                        PC.ConsoleCommand("set "+ Move + " AnimSet AnimSet'Anim_Generic_NPC.Anim_Generic_NPC'", 0)
            PC.ConsoleCommand("camera 3rd", 0)
            PC.Behavior_Melee()
        else:
            PlayerMesh = self.GetPlayerController().Pawn.Mesh
            Particle = bl2sdk.FindObject("ParticleSystem", self.ChooseAnimation())
            self.GetPlayerController().ConsoleCommand("camera 3rd", 0)
            bl2sdk.GetEngine().GetCurrentWorldInfo().MyEmitterPool.SpawnEmitterMeshAttachment(Particle, PlayerMesh, "head")


    #Reverse the changes of PlayEmote()
    def StopEmote(self):
        SpecialMoves = [
                    "GD_Assassin_Streaming.Anims.WeaponAnim_Melee",
                    "GD_Lilac_Psycho_Streaming.Anims.WeaponAnim_Melee",
                    "GD_Mercenary_Streaming.Anims.WeaponAnim_Melee",
                    "GD_PlayerShared.Anims.WeaponAnim_Melee_WeaponBlade",
                    "GD_Siren_Streaming.Anims.WeaponAnim_Melee",
                    "GD_Soldier_Streaming.Anims.WeaponAnim_Melee",
                    "GD_Tulip_Mechro_Streaming.Anims.WeaponAnim_Melee"
            ]
        
        PC = self.GetPlayerController()
        for Move in SpecialMoves:
            if bl2sdk.FindObject("SpecialMove_WeaponAction", Move) != None:
                PC.ConsoleCommand("set "+ Move + " AnimName Melee", 0)
                PC.ConsoleCommand("set "+ Move + " EndingCondition EC_OnBlendOut", 0)
                PC.ConsoleCommand("set "+ Move + " AnimSet None", 0)
        
        PC.ConsoleCommand("camera 1st", 0)
        PC.Behavior_Melee()
        bl2sdk.GetEngine().GetCurrentWorldInfo().MyEmitterPool.ClearAllPoolComponents()

    def GameInputRebound(self, name, key):
        pass

    def GameInputPressed(self, input):
        if input.Name == "Next Emote":
            self._animation += 1
            self.FeedbackEmote()
        elif input.Name == "Previous Emote":
            self._animation -= 1
            self.FeedbackEmote()
        if input.Name == "Play Emote":
            self.PlayEmote()
        if input.Name == "Stop Emote":
            self.StopEmote()


    def HandleEmotes(self, caller, function, params):
        print(params)


    def Enable(self):
        self.ForceLoad()
        self.RegisterGameInput("Play Emote", "Up")
        self.RegisterGameInput("Next Emote", "Right")
        self.RegisterGameInput("Previous Emote", "Left")
        self.RegisterGameInput("Stop Emote", "Down")
    def Disable(self):
        self.UnregisterGameInput("Play Emote")
        self.UnregisterGameInput("Next Emote")
        self.UnregisterGameInput("Previous Emote")
        self.UnregisterGameInput("Stop Emote")


EmoteInstance = Emotes()
bl2sdk.Mods.append(EmoteInstance)


