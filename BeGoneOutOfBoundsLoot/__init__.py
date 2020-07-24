import bl2sdk

class BGOOBL(bl2sdk.BL2MOD):
    Name = "Be Gone Out Of Bounds Loot"
    Description = "Adds a keybind option to the game that allows you to teleport all loot on the ground to your current location. By default the key is binded to ENTER."
    Author = "Juso"


    def GetPlayerController(self):
        return bl2sdk.GetEngine().GamePlayers[0].Actor

    def GameInputRebound(self, name, key):
        pass

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
        self.RegisterGameInput("Teleport Loot To Me", "Enter")

    def Disable(self):
        self.UnregisterGameInput("Teleport Loot To Me")



BGOOBLInstance = BGOOBL()
bl2sdk.Mods.append(BGOOBLInstance)


