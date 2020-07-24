import bl2sdk
import webbrowser


class Poke(bl2sdk.BL2MOD):
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
        bl2sdk.LoadPackage("Orchid_WormBelly_Dynamic")
        bl2sdk.LoadPackage("DamTop_Dynamic")
        turret = bl2sdk.FindObject("Object", "GD_RolandNPC.Projectiles.Projectile_RolandTurret_DamTop:"
                                             "BehaviorProviderDefinition_0.Behavior_SpawnFromPopulationSystem_39."
                                             "PopulationFactoryBalancedAIPawn_0")
        rakkhive = bl2sdk.FindObject("AIPawnBalanceDefinition", "GD_Orchid_Pop_RakkHive.Character."
                                                                "PawnBalance_Orchid_RakkHive")
        pawn_rakkhive = bl2sdk.FindObject("WillowAIPawn", "GD_Orchid_RakkHive.Character.Pawn_RakkHive")
        bl2sdk.KeepAlive(turret)
        bl2sdk.KeepAlive(rakkhive)
        bl2sdk.KeepAlive(pawn_rakkhive)

    def get_pc(self):
        return bl2sdk.GetEngine().GamePlayers[0].Actor

    def HandleKill(self, caller, function, params):
        if params.Killer == self.get_pc():
            spawn = bl2sdk.FindObject("Object", "GD_Orchid_RakkHive.Animation.Anim_RakkHive_Shake:"
                                               "BehaviorProviderDefinition_0.Behavior_AISpawn_43")
            for popdef in bl2sdk.FindAll("WillowPopulationDefinition"):
                for i in popdef.ActorArchetypeList:
                    try:
                        WillowAiPawn = i.SpawnFactory.PawnBalanceDefinition.AIPawnArchetype
                        if WillowAiPawn.BodyClass == caller.BodyClass:
                            spawn.PopDef = popdef
                            break
                    except:
                        continue
            desc = bl2sdk.FindObject("Object", "GD_GrenadeMods.Delivery.Delivery_NastySurprise:"
                                               "AttributePresentationDefinition_4")
            desc.Description = "Catch 'em all!<br>Currently holding: " + str(caller.CurrentNameTag.NameTag)
        return True

    KillHook = "WillowGame.WillowAIPawn.Died"

    def Enable(self):
        self.initial_setup()
        bl2sdk.RegisterHook(self.KillHook, "KillHook", KilledHook)

    def Disable(self):
        bl2sdk.RemoveHook(self.KillHook, "KillHook")


PokeInstance = Poke()


def KilledHook(caller: bl2sdk.UObject, function: bl2sdk.UFunction, params: bl2sdk.FStruct) -> bool:
    PokeInstance.HandleKill(caller, function, params)
    return True


bl2sdk.Mods.append(PokeInstance)
