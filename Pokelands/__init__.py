import unrealsdk
import webbrowser


class Poke(unrealsdk.BL2MOD):
    Name = "Pokelands"
    Description = "Turns the Nasty Suprise into a Pokeball." \
                  " After Killing an enemy your Pokeball will be able to spawn that enemy as and friendly NPC." \
                  " Pawn Grenade Mod requierd, get it on Nexus Mods or GitHub." \
                  "Credits to Our Lord and Saviour Gabe Newell for figuring out how to spawn enemies."
    SettingsInputs = {"Enter": "Enable", "H": "Nexus Mods"}
    Author = "Juso"

    def SettingsInputPressed(self, name):
        if name == "Enable":
            self.Status = "Enabled"
            self.SettingsInputs = {"Enter": "Disable"}
            self.Enable()
        elif name == "Disable":
            self.Status = "Disabled"
            self.SettingsInputs = {"Enter": "Enable"}
            self.Disable()
        elif name == "Nexus Mods":
            webbrowser.open("https://www.nexusmods.com/borderlands2/mods/234")

    def initial_setup(self):
        unrealsdk.LoadPackage("Orchid_WormBelly_Dynamic")
        unrealsdk.LoadPackage("DamTop_Dynamic")
        turret = unrealsdk.FindObject("Object", "GD_RolandNPC.Projectiles.Projectile_RolandTurret_DamTop:"
                                                "BehaviorProviderDefinition_0.Behavior_SpawnFromPopulationSystem_39."
                                                "PopulationFactoryBalancedAIPawn_0")
        rakkhive = unrealsdk.FindObject("AIPawnBalanceDefinition", "GD_Orchid_Pop_RakkHive.Character."
                                                                   "PawnBalance_Orchid_RakkHive")
        pawn_rakkhive = unrealsdk.FindObject("WillowAIPawn", "GD_Orchid_RakkHive.Character.Pawn_RakkHive")
        unrealsdk.KeepAlive(turret)
        unrealsdk.KeepAlive(rakkhive)
        unrealsdk.KeepAlive(pawn_rakkhive)

    def get_pc(self):
        return unrealsdk.GetEngine().GamePlayers[0].Actor

    def HandleKill(self, caller, function, params):
        if params.Killer == self.get_pc():
            spawn = unrealsdk.FindObject("Object", "GD_Orchid_RakkHive.Animation.Anim_RakkHive_Shake:"
                                                   "BehaviorProviderDefinition_0.Behavior_AISpawn_43")
            for popdef in unrealsdk.FindAll("WillowPopulationDefinition"):
                for i in popdef.ActorArchetypeList:
                    try:
                        WillowAiPawn = i.SpawnFactory.PawnBalanceDefinition.AIPawnArchetype
                        if WillowAiPawn.BodyClass == caller.BodyClass:
                            spawn.PopDef = popdef
                            break
                    except:
                        continue

            self.get_pc().ConsoleCommand(
                f"set GD_GrenadeMods.Delivery.Delivery_NastySurprise:AttributePresentationDefinition_4 Description "
                f"Catch 'em all!<br>Currently holding: {caller.CurrentNameTag.NameTag}",
                False)
        return True

    def Enable(self):
        def KilledHook(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            self.HandleKill(caller, function, params)
            return True

        self.initial_setup()
        unrealsdk.RegisterHook("WillowGame.WillowAIPawn.Died", "KillHook", KilledHook)
        self.get_pc().ConsoleCommand("set GD_GrenadeMods.Title.Title_NastySurprise PartName Pokeball", False)
        self.get_pc().ConsoleCommand(
            f"set GD_GrenadeMods.Delivery.Delivery_NastySurprise:AttributePresentationDefinition_4 Description "
            f"Catch 'em all!", False)

    def Disable(self):
        unrealsdk.RemoveHook(self.KillHook, "KillHook")


unrealsdk.RegisterMod(Poke())
