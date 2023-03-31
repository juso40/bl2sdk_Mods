import unrealsdk  # type: ignore

from Mods.ModMenu import RegisterMod, SDKMod


class Pizza(SDKMod):
    Name = "Pizza Time"
    Description = "It's Pizza Time!\nReplaces the Fastball with a Pizza."
    Author = "juso"
    Version = "1.0"

    def load_pizza_mesh(self) -> None:
        unrealsdk.LoadPackage("SanctuaryAir_Dynamic")
        unrealsdk.KeepAlive(
            unrealsdk.FindObject("StaticMesh", "Prop_Details.Meshes.Pizza")
        )

    def change_mesh(self) -> None:
        mesh = unrealsdk.FindObject(
            "StaticMeshComponent",
            "GD_GrenadeMods.Projectiles.Grenade_Fastball:StaticMeshComponent_21",
        )
        mesh.StaticMesh = unrealsdk.FindObject(
            "StaticMesh", "Prop_Details.Meshes.Pizza"
        )

    def revert_mesh(self) -> None:
        mesh = unrealsdk.FindObject(
            "StaticMeshComponent",
            "GD_GrenadeMods.Projectiles.Grenade_Fastball:StaticMeshComponent_21",
        )
        mesh.StaticMesh = unrealsdk.FindObject(
            "StaticMesh", "FX_WEP_Shared.Meshes.RL_Rocket_Child"
        )

    def Enable(self) -> None:  # noqa: N802
        self.load_pizza_mesh()
        self.change_mesh()

    def Disable(self) -> None:  # noqa: N802
        self.revert_mesh()


PizzaInstance = Pizza()
RegisterMod(PizzaInstance)
