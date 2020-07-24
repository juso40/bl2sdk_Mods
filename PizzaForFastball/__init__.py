import bl2sdk

class Pizza(bl2sdk.BL2MOD):
    Name = "Pizza Time"
    Description = "It's Pizza Time!\nReplaces the Fastball with a Pizza.\nWritten by Juso"

    def ForceLoad(self):
        bl2sdk.LoadPackage("SanctuaryAir_Dynamic")
        bl2sdk.KeepAlive(bl2sdk.FindObject("StaticMesh", "Prop_Details.Meshes.Pizza"))

    def ChangeVisuals(self):
        Mesh = bl2sdk.FindObject("StaticMeshComponent", "GD_GrenadeMods.Projectiles.Grenade_Fastball:StaticMeshComponent_21")
        Mesh.StaticMesh = bl2sdk.FindObject("StaticMesh", "Prop_Details.Meshes.Pizza")
    def ChangeVisuals(self):
        Mesh = bl2sdk.FindObject("StaticMeshComponent", "GD_GrenadeMods.Projectiles.Grenade_Fastball:StaticMeshComponent_21")
        Mesh.StaticMesh = bl2sdk.FindObject("StaticMesh", "FX_WEP_Shared.Meshes.RL_Rocket_Child")

    def Enable(self):
        self.ForceLoad()
        self.ChangeVisuals()
    def Disable(self):
        self.RevertVisuals()

PizzaInstance = Pizza()
bl2sdk.Mods.append(PizzaInstance)