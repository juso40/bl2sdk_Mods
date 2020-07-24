import unrealsdk
from . import bl2tools

from math import sqrt


class MapFT(unrealsdk.BL2MOD):

    def __init__(self):
        self.RemovedMarker = False
        self.MapObjects = []
        self.ObjectDelta = []

    def get_location(self, caller, function, params):
        if self.RemovedMarker:
            self.ObjectDelta.clear()
            pawn = bl2tools.get_player_controller().Pawn
            for i in caller.MapObjects:
                if i.CustomObjectLoc.X != 0.0:  # Get our newest Marker
                    MarkerLoc = (i.CustomObjectLoc.X, i.CustomObjectLoc.Y)

            for objs in self.MapObjects:
                MapObjLoc = (objs.Location.X, objs.Location.Y)
                delta = sqrt((MapObjLoc[0] - MarkerLoc[0]) ** 2 + (MapObjLoc[1] - MarkerLoc[1]) ** 2)
                self.ObjectDelta.append(delta)

            temp = self.ObjectDelta.index(min(self.ObjectDelta))
            if self.ObjectDelta[temp] <= 500:
                if "vehicle" in bl2tools.get_obj_path_name(self.MapObjects[temp]).lower() and \
                        "spawnstation" not in bl2tools.get_obj_path_name(self.MapObjects[temp]).lower():
                    if self.MapObjects[temp].CanEnterVehicle(pawn):
                        self.MapObjects[temp].DriverEnter(pawn, True)

                elif "fasttravel" in bl2tools.get_obj_path_name(self.MapObjects[temp]).lower():
                    dest_loc = self.MapObjects[temp].TeleportDest.ExitPoints[0]
                    pawn.Location = (dest_loc.Location.X, dest_loc.Location.Y, dest_loc.Location.Z + 50)
                    pawn.Controller.Rotation = (dest_loc.Rotation.Pitch, dest_loc.Rotation.Yaw, dest_loc.Rotation.Roll)

            self.MapObjects.clear()
            self.RemovedMarker = False
            return True
        else:
            for i in caller.MapObjects:
                if i.ClientInteractiveObject is not None:
                    self.MapObjects.append(i.ClientInteractiveObject)
                if i.Vehicle is not None:
                    self.MapObjects.append(i.Vehicle)
            self.RemovedMarker = True
            return True

    def GameInputPressed(self, input):
        if input.Name == "Show FT":
            pc = bl2tools.get_player_controller()
            pc.PlayGfxMovieDefinition("UI_FastTravelStation.FastTravelStation_ThirdPerson_Definition")

    def Enable(self):
        def Teleport(caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
            return self.get_location(caller, function, params)
        unrealsdk.RegisterHook("WillowGame.StatusMenuMapGFxObject.PlaceCustomObjective", "MarkerHook", Teleport)

    def Disable(self):
        unrealsdk.RemoveHook("WillowGame.StatusMenuMapGFxObject.PlaceCustomObjective", "MarkerHook")

