from unrealsdk import *

import os

from . import travel
from . import betterspawns
from Mods.ModMenu import SDKMod, EnabledSaveType, Keybind

class Main(SDKMod):
    Name: str = "BSABT"
    Description: str = "<B><U><font size='14' color='#e8131d'>Better Spawns and Better Travel</font></U></B>\n" \
                  "This Mod reimplements some of the BL3 QoL features, such as spawning at the last respawn station " \
                  "you triggered in game, allowing you to open the FT list form anywhere and directly spawning in " \
                  "your car or near a FT Station directly from the map menu. To teleport in your car or near a FT " \
                  "simply place and remove a waypoint near the car/FT on your map. To open the FT menu press the (by " \
                  "default) F1 key."
    Author: str = "Juso"
    
    Types: ModTypes = ModTypes.Utility
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadWithSettings

    Keybinds = [Keybind("Show FT", "F1")]

    def __init__(self):
        super().__init__()

        self.FILE_PATH = os.path.dirname(os.path.realpath(__file__))
        self.Travel = travel.MapFT()
        self.Spawns = betterspawns.Spawns(self.FILE_PATH)

    def GameInputPressed(self, input):
        self.Travel.GameInputPressed(input)

    def Enable(self):
        self.Travel.Enable()
        self.Spawns.Enable()

    def Disable(self):
        self.Travel.Disable()
        self.Spawns.Disable()


if __name__.startswith("Mods"):
    RegisterMod(Main())
