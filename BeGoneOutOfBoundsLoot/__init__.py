import unrealsdk


class BGOOBL(unrealsdk.BL2MOD):
    Name = "Be Gone Out Of Bounds Loot"
    Version = "1.1"
    Type = [unrealsdk.ModTypes.Utility]
    Description = "Adds a keybind option to the game that allows you to teleport all loot on the ground to your " \
                  f"current location. By default the key is binded to ENTER.\n\n{Version}"
    Author = "Juso"

    Keybinds = [["Teleport Loot To Me", "Enter"]]

    def GetPlayerController(self):
        return unrealsdk.GetEngine().GamePlayers[0].Actor

    def GameInputPressed(self, input):
        if input.Name == "Teleport Loot To Me":
            Pawn = self.GetPlayerController().Pawn
            Location = (Pawn.Location.X, Pawn.Location.Y, Pawn.Location.Z)
            for Pickup in self.GetPlayerController().GetWillowGlobals().PickupList:
                Pickup.Location = Location
                Pickup.AdjustPickupPhysicsAndCollisionForBeingDropped()
                lst = list(Location)
                lst[2] += 10
                Location = tuple(lst)

    def Enable(self):
        pass

    def Disable(self):
        pass


unrealsdk.RegisterMod(BGOOBL())
