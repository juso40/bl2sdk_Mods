import unrealsdk
from unrealsdk import *
from ..OptionManager import Options
import json
import os


class Viewmodel(BL2MOD):
    Name = "CVM"
    Description = "<B><U><font size='18' color='#e8131d'>Configurable Viewmodel</font></U></B>\n" \
                  "A mod that allows you to set your viewmodel the way you like it!"
    Author = "Juso"
    Options = [
        Options.Spinner("Save current type to file", "Save the current configuration for"
                                              " the current WeaponType", "Save", ["Save", "Save"]),
        Options.Spinner("Save same type to file", "Save the current configuration for"
                                              " all the same WeaponTypes", "Save All", ["Save All", "Save All"]),
        Options.Spinner("Load from files", "Loads your previously saved configs.", "Load", ["Load", "Load"]),

        Options.Slider("FirstPersonMeshFOV", "Change the FirstPersonMeshFOV", 45, 0, 100, 1),
        Options.Slider("PlayerViewOffset.X", "Change the PlayerViewOffset X Value", 20, -100, 100, 1),
        Options.Slider("PlayerViewOffset.Y", "Change the PlayerViewOffset Y Value", 4, -100, 100, 1),
        Options.Slider("PlayerViewOffset.Z", "Change the PlayerViewOffset Z Value", 2, -100, 100, 1),

        Options.Slider("RelativeRotation.Pitch", "Change the Pitch of the Weapon", 0, -32768, 32768, 182),
        Options.Slider("RelativeRotation.Yaw", "Change the Yaw of the Weapon", 16384, -32768, 32768, 182),
        Options.Slider("RelativeRotation.Roll", "Change the Roll of the Weapon", 0, -32768, 32768, 182),
    ]

    PATH = os.path.dirname(os.path.realpath(__file__))

    def get_pc(self):
        return GetEngine().GamePlayers[0].Actor

    def Enable(self):
        pass

    def Disable(self):
        pass

    def change_MeshFOV(self,  value, WT):
        WT.FirstPersonMeshFOV = value
        self.get_pc().UpdateForegroundFOV()

    def change_ViewOffset(self, xyz, value, WT):
        if xyz == "PlayerViewOffset.X":
            WT.PlayerViewOffset.X = value
        elif xyz == "PlayerViewOffset.Y":
            WT.PlayerViewOffset.Y = value
        elif xyz == "PlayerViewOffset.Z":
            WT.PlayerViewOffset.Z = value
        pawn = self.get_pc().Pawn
        pawn.SetArmPosition()

    def change_RelativeRotation(self, rot, value):
        if self.get_pc() and self.get_pc().Pawn:
            pawn = self.get_pc().Pawn
            hands = pawn.Arms.SkeletalMesh
            if rot == "RelativeRotation.Pitch":
                hands.Sockets[0].RelativeRotation.Pitch = int(value)
            elif rot == "RelativeRotation.Yaw":
                hands.Sockets[0].RelativeRotation.Yaw = int(value)
            elif rot == "RelativeRotation.Roll":
                hands.Sockets[0].RelativeRotation.Roll = int(value)
            pawn.SetArmPosition()
            self.get_pc().UpdateForegroundFOV()

    saved_settings = {}

    def save_to_json(self, obj):
        self.saved_settings.clear()
        for _option in self.Options[3:8]:
            self.saved_settings[_option.Caption] = _option.CurrentValue
        with open(os.path.join(self.PATH, str(obj) + ".json"), "w") as file:
            json.dump(self.saved_settings, file)
        self.saved_settings.clear()
        for _option in self.Options[8:]:
            self.saved_settings[_option.Caption] = _option.CurrentValue
        with open(os.path.join(self.PATH, "SkeletalMeshSocket.json"), "w") as file:
            json.dump(self.saved_settings, file)

    def ModOptionChanged(self, option, newValue):
        if option in self.Options:
            if not self.get_pc() or not self.get_pc().Pawn or not self.get_pc().Pawn.Weapon:
                return

            WeaponType = self.get_pc().Pawn.Weapon.DefinitionData.WeaponTypeDefinition
            if option.Caption == "FirstPersonMeshFOV":
                self.change_MeshFOV(newValue, WeaponType)

            elif option.Caption == "PlayerViewOffset.X":
                self.change_ViewOffset(option.Caption, newValue, WeaponType)
            elif option.Caption == "PlayerViewOffset.Y":
                self.change_ViewOffset(option.Caption, newValue, WeaponType)
            elif option.Caption == "PlayerViewOffset.Z":
                self.change_ViewOffset(option.Caption, newValue, WeaponType)

            elif option.Caption == "RelativeRotation.Pitch":
                self.change_RelativeRotation(option.Caption, newValue)
            elif option.Caption == "RelativeRotation.Yaw":
                self.change_RelativeRotation(option.Caption, newValue)
            elif option.Caption == "RelativeRotation.Roll":
                self.change_RelativeRotation(option.Caption, newValue)

            elif option.Caption == "Save current type to file":
                self.save_to_json(WeaponType)

            elif option.Caption == "Save same type to file":
                for wt in FindAll("WeaponTypeDefinition"):
                    if wt.BodyWeaponHoldName == WeaponType.BodyWeaponHoldName:
                        self.save_to_json(wt)

            elif option.Caption == "Load from files":
                for root, dirs, files in os.walk(self.PATH):
                    for file in files:
                        if file.endswith(".json"):
                            if len(file.split()) > 1:
                                cls = str(file.split()[0])
                                obj = os.path.splitext(str(file.split()[1]))[0]
                                WeaponType = FindObject(cls, obj)
                                with open(os.path.join(root, file), "r") as f:
                                    settings = json.load(f)
                                    self.change_MeshFOV(settings["FirstPersonMeshFOV"], WeaponType)
                                    for attr, value in settings.items():
                                        try:
                                            self.change_ViewOffset(attr, value, WeaponType)
                                        except:
                                            pass
                            else:
                                with open(os.path.join(root, file), "r") as f:
                                    settings = json.load(f)
                                    for attr, value in settings.items():
                                        try:
                                            self.change_RelativeRotation(attr, value)
                                        except:
                                            pass



unrealsdk.RegisterMod(Viewmodel())

# IronsightsRotation (Pitch=425,Yaw=-603,Roll=-128) WillowPlayerPawn
# Use this for an inspection mod
