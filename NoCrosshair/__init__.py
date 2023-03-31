import unrealsdk  # type: ignore

from Mods.ModMenu import Hook, RegisterMod, SDKMod


class Crosshair(SDKMod):
    Name = "No Crosshair"
    Description = "Removes the crosshairs."
    Author = "juso"
    Version = "1.0"

    def __init__(self) -> None:
        super().__init__()
        self.zoomed: bool = False

    @Hook("WillowWeapon.Active.BeginState")
    def disable_crosshair(
        self,
        caller: unrealsdk.UObject,
        function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ) -> bool:
        if not self.zoomed:
            caller.bCrosshairEnabled = False
            caller.bSuppressCrosshair = True
        else:
            caller.bCrosshairEnabled = True
            caller.bSuppressCrosshair = False
        return True

    @Hook("WillowGame.WillowWeapon.SetZoomState")
    def handle_zooming(
        self,
        caller: unrealsdk.UObject,
        function: unrealsdk.UFunction,
        params: unrealsdk.FStruct,
    ) -> bool:
        if params.NewZoomState == 2:
            self.zoomed = True
            caller.bCrosshairEnabled = True
        else:
            self.zoomed = False
            caller.bCrosshairEnabled = False
        return True


CrosshairInstance = Crosshair()
RegisterMod(CrosshairInstance)
