from unrealsdk import *

from . import bl2tools


class Photo(BL2MOD):
    Name = "Photomode"
    Version = "1.0"
    Types = [ModTypes.Utility]
    Description = "Simple Photo Mode for BL2."
    Author = "Juso"

    Keybinds = []
    def __init__(self):
        self.b_photo = False
        self.pawn = None
        self.Keybinds = [["Photomode", "P"],
                         ["Photomode Roll+", "MouseScrollUp"],
                         ["Photomode Roll-", "MouseScrollDown"]]

    def GameInputPressed(self, input):
        if input.Name == "Photomode":
            pc = bl2tools.get_player_controller()
            world_info = GetEngine().GetCurrentWorldInfo()
            if world_info.GetStreamingPersistentMapName() != "menumap":
                if self.b_photo and world_info.bPlayersOnly:
                    pc.Possess(self.pawn, True)
                    pc.DisplayHUD()
                    world_info.bPlayersOnly = False
                    pc.Rotation.Roll = 0
                    self.b_photo = False
                else:
                    self.pawn = pc.Pawn
                    pc.Unpossess()
                    pc.HideHUD()
                    pc.ServerSpectate()
                    world_info.bPlayersOnly = True
                    self.b_photo = True
        elif input.Name == "Photomode Roll+":
            if self.b_photo:
                bl2tools.get_player_controller().Rotation.Roll += 128
        elif input.Name == "Photomode Roll-":
            if self.b_photo:
                bl2tools.get_player_controller().Rotation.Roll -= 128

    def Enable(self):
        self.Keybinds = [("Photomode", "P"),
                         ("Photomode Roll+", "MouseScrollUp"),
                         ("Photomode Roll-", "MouseScrollDown")]

    def Disable(self):
        self.Keybinds = []

RegisterMod(Photo())
