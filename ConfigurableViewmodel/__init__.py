import json
import os

import unrealsdk
from unrealsdk import *

from ..ModMenu import EnabledSaveType, OptionManager, SDKMod, Hook


def get_pc():
    return unrealsdk.GetEngine().GamePlayers[0].Actor


class Viewmodel(SDKMod):
    Name = "CVM"
    Description = "<B><U><font size='18' color='#e8131d'>Configurable Viewmodel</font></U></B>\n" \
                  "A mod that allows you to set your viewmodel the way you like it!"
    Author = "Juso"
    Version = "2.1"
    SaveEnabledState = EnabledSaveType.LoadWithSettings
    Options = [
        OptionManager.Options.Spinner("Save current type to file", "Save the current configuration for"
                                                                   " the current WeaponType", "Save", ["Save", "Save"]),
        OptionManager.Options.Spinner("Save same type to file", "Save the current configuration for"
                                                                " all the same WeaponTypes", "Save All",
                                      ["Save All", "Save All"]),
        OptionManager.Options.Spinner("Load from files", "Loads your previously saved configs.", "Load",
                                      ["Load", "Load"]),

        OptionManager.Options.Slider("FirstPersonMeshFOV", "Change the FirstPersonMeshFOV", 45, 0, 100, 1),
        OptionManager.Options.Slider("PlayerViewOffset.X", "Change the PlayerViewOffset X Value", 20, -100, 100, 1),
        OptionManager.Options.Slider("PlayerViewOffset.Y", "Change the PlayerViewOffset Y Value", 4, -100, 100, 1),
        OptionManager.Options.Slider("PlayerViewOffset.Z", "Change the PlayerViewOffset Z Value", 2, -100, 100, 1),
    ]

    PATH = os.path.dirname(os.path.realpath(__file__))

    def Enable(self):
        super().Enable()

    def Disable(self):
        super().Disable()

    @Hook("WillowGame.WillowHUD.CreateWeaponScopeMovie")
    def apply_settings(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct):
        self.load_from_files()
        return True

    def change_MeshFOV(self, value, WT):
        if not WT:
            return
        WT.FirstPersonMeshFOV = value
        get_pc().UpdateForegroundFOV()

    def change_ViewOffset(self, xyz, value, WT):
        if xyz == "PlayerViewOffset.X":
            WT.PlayerViewOffset.X = value
        elif xyz == "PlayerViewOffset.Y":
            WT.PlayerViewOffset.Y = value
        elif xyz == "PlayerViewOffset.Z":
            WT.PlayerViewOffset.Z = value
        pawn = get_pc().Pawn
        pawn.SetArmPosition()

    saved_settings = {}

    def save_to_json(self, obj):
        self.saved_settings.clear()
        for _option in self.Options[3:8]:
            self.saved_settings[_option.Caption] = _option.CurrentValue
        with open(os.path.join(self.PATH, str(obj) + ".json"), "w") as file:
            json.dump(self.saved_settings, file)
        self.saved_settings.clear()
        with open(os.path.join(self.PATH, "SkeletalMeshSocket.json"), "w") as file:
            json.dump(self.saved_settings, file)

    def ModOptionChanged(self, option, new_value):
        if option in self.Options:
            if not get_pc() or not get_pc().Pawn or not get_pc().Pawn.Weapon:
                return

            WeaponType = get_pc().Pawn.Weapon.DefinitionData.WeaponTypeDefinition
            if option.Caption == "FirstPersonMeshFOV":
                self.change_MeshFOV(new_value, WeaponType)

            elif option.Caption == "PlayerViewOffset.X":
                self.change_ViewOffset(option.Caption, new_value, WeaponType)
            elif option.Caption == "PlayerViewOffset.Y":
                self.change_ViewOffset(option.Caption, new_value, WeaponType)
            elif option.Caption == "PlayerViewOffset.Z":
                self.change_ViewOffset(option.Caption, new_value, WeaponType)

            elif option.Caption == "Save current type to file":
                self.save_to_json(WeaponType)

            elif option.Caption == "Save same type to file":
                for wt in unrealsdk.FindAll("WeaponTypeDefinition"):
                    if wt.BodyWeaponHoldName == WeaponType.BodyWeaponHoldName:
                        self.save_to_json(wt)

            elif option.Caption == "Load from files":
                self.load_from_files()

    def load_from_files(self):
        for root, dirs, files in os.walk(self.PATH):
            for file in files:
                if file.endswith(".json"):
                    if len(file.split()) > 1:
                        cls = str(file.split()[0])
                        obj = os.path.splitext(str(file.split()[1]))[0]
                        WeaponType = unrealsdk.FindObject(cls, obj)
                        with open(os.path.join(root, file), "r") as f:
                            settings = json.load(f)
                            self.change_MeshFOV(settings["FirstPersonMeshFOV"], WeaponType)
                            for attr, value in settings.items():
                                try:
                                    self.change_ViewOffset(attr, value, WeaponType)
                                except:
                                    pass


unrealsdk.RegisterMod(Viewmodel())

# IronsightsRotation (Pitch=425,Yaw=-603,Roll=-128) WillowPlayerPawn
# Use this for an inspection mod
