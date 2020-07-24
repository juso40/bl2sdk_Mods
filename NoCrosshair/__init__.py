import bl2sdk


class Crosshair(bl2sdk.BL2MOD):
    Name = "No Crosshair"
    Description = "Removes the crosshairs."
    Author = "Juso"

    bZoomed = False

    def disable_crosshair(self, caller, function, params):
        if not self.bZoomed:
            caller.bCrosshairEnabled = False
            caller.bSuppressCrosshair = True
        else:
            caller.bCrosshairEnabled = True
            caller.bSuppressCrosshair = False

    def handle_zooming(self, caller, function, params):
        if params.NewZoomState == 2:
            self.bZoomed = True
            caller.bCrosshairEnabled = True
        else:
            self.bZoomed = False
            caller.bCrosshairEnabled = False

    crosshair_hook = "WillowWeapon.Active.BeginState"
    zoom_hook = "WillowGame.WillowWeapon.SetZoomState"

    def Enable(self):
        bl2sdk.RegisterHook(self.crosshair_hook, "CrosshairHook", CrosshairHook)
        bl2sdk.RegisterHook(self.zoom_hook, "ZoomHook", IsZoomingHook)

    def Disable(self):
        bl2sdk.RemoveHook(self.crosshair_hook, "CrosshairHook")
        bl2sdk.RemoveHook(self.zoom_hook, "ZoomHook")


CrosshairInstance = Crosshair()


def CrosshairHook(caller: bl2sdk.UObject, function: bl2sdk.UFunction, params: bl2sdk.FStruct) -> bool:
    CrosshairInstance.disable_crosshair(caller, function, params)
    return True


def IsZoomingHook(caller: bl2sdk.UObject, function: bl2sdk.UFunction, params: bl2sdk.FStruct) -> bool:
    CrosshairInstance.handle_zooming(caller, function, params)
    return True

bl2sdk.Mods.append(CrosshairInstance)
