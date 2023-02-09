from typing import Optional, Any

import unrealsdk

from ..ModMenu import EnabledSaveType, SDKMod, RegisterMod, ModTypes, KeybindManager


class Photo(SDKMod):
    Name = "Photomode"
    Version = "1.2"
    Types = ModTypes.Utility
    Description = """Simple Photo Mode for BL2.
'Mousewheel Up/Down' to change the active modifier.
Hold 'Shift' while scrolling to change the camera movement speed.
Hold 'R' while scrolling to change the camera rotation.
Hold 'F' while scrolling to change the camera FOV.
"""
    Author = "Juso"
    SaveEnabledState = EnabledSaveType.LoadWithSettings

    Keybinds = [
        KeybindManager.Keybind("Photomode", "P", IsRebindable=True),
        KeybindManager.Keybind("Modifier +", "MouseScrollUp", IsRebindable=False),
        KeybindManager.Keybind("Modifier -", "MouseScrollDown", IsRebindable=False),
        KeybindManager.Keybind("Camera Speed", "LeftShift", IsRebindable=False),
        KeybindManager.Keybind("Roll (Camera Rotation)", "R", IsRebindable=False),
        KeybindManager.Keybind("FOV", "F", IsRebindable=False),
    ]

    def __init__(self):
        self.in_photomode: bool = False
        self.pawn_backup: Optional[unrealsdk.UObject] = None
        self.active_camera_modifier: callable = lambda x: None
        self.last_modifier_name: str = ""

    @property
    def pc(self) -> unrealsdk.UObject:
        return unrealsdk.GetEngine().GamePlayers[0].Actor

    def toggle_photo_mode(self, enable: bool) -> None:
        world_info: unrealsdk.UObject = unrealsdk.GetEngine().GetCurrentWorldInfo()
        if enable:
            self.pawn_backup = self.pc.Pawn
            self.pc.Unpossess()
            self.pc.HideHUD()
            self.pc.ServerSpectate()
            world_info.bPlayersOnly = True
            self.in_photomode = True
        else:
            self.pc.Possess(self.pawn_backup, True)
            self.pc.DisplayHUD()
            world_info.bPlayersOnly = False
            self.pc.Rotation.Roll = 0
            self.pc.SetFOV(self.pc.DefaultFOV)
            self.in_photomode = False

    def GameInputPressed(self, bind: KeybindManager.Keybind, event: KeybindManager.InputEvent) -> None:
        if event == KeybindManager.InputEvent.Released:

            if bind.Name == "Photomode":
                world_info: unrealsdk.UObject = unrealsdk.GetEngine().GetCurrentWorldInfo()
                if world_info.GetStreamingPersistentMapName() == "menumap":
                    return
                self.toggle_photo_mode(
                    not (self.in_photomode and world_info.bPlayersOnly)
                )
            elif bind.Name == "Modifier +":
                self.active_camera_modifier(1)
            elif bind.Name == "Modifier -":
                self.active_camera_modifier(-1)

            if bind.Name == self.last_modifier_name:
                self.last_modifier_name = ""
                self.active_camera_modifier = lambda x: None

        elif event == KeybindManager.InputEvent.Pressed and self.in_photomode:

            if bind.Name == "Camera Speed":
                self.active_camera_modifier = self.camera_speed_modifier
                self.last_modifier_name = bind.Name
            elif bind.Name == "Roll (Camera Rotation)":
                self.active_camera_modifier = self.camera_roll_modifier
                self.last_modifier_name = bind.Name
            elif bind.Name == "FOV":
                self.active_camera_modifier = self.camera_fov_modifier
                self.last_modifier_name = bind.Name

    def camera_roll_modifier(self, x: int) -> None:
        self.pc.Rotation.Roll += x * 128

    def camera_speed_modifier(self, x: int) -> None:
        speed: float = self.pc.SpectatorCameraSpeed
        # clamp between 50 and 10000
        speed = max(min(speed + x * 50, 10000), 50)

        self.pc.SpectatorCameraSpeed = speed

    def camera_fov_modifier(self, x: int) -> None:
        fov: int = self.pc.FOVAngle
        # clamp between 4 and 180
        fov = max(min(fov + x, 180), 4)
        self.pc.SetFOV(fov)


RegisterMod(Photo())
