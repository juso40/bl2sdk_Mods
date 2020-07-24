from unrealsdk import *
import unrealsdk

from . import bl2tools


class FPDriver(unrealsdk.BL2MOD):
    Name = "First Person Driver"
    Version = "1.0"
    Description = f"Experience all vehicles in first person. Toggle between 3rd and 1st person using '5'\n\nVersion: " \
                  f"{Version}"
    Author = "Juso"
    Types = [unrealsdk.ModTypes.Gameplay]

    def __init__(self):
        self.is_first_person = True
        self.Keybinds = [["Driver Cam", "Five"], ]
        self.settings = {
            "mercenary": {"GD_Runner_Streaming.CameraDefs.Camera_DriverSeat": ["CameraOffset 0",
                                                                               "CameraPitchDownOffset -20",
                                                                               "CameraPitchUpOffset 50",
                                                                               "BaseCameraPosition (Z=65)",
                                                                               "bScaleDistanceWithSpeed False",
                                                                               ],
                          "GD_BanditTechnical.CameraDefs.Camera_DriverSeat": ["CameraPitchDownOffset -10",
                                                                              "BaseCameraPosition (X=-1,Y=0,Z=70)",
                                                                              "CameraPitchUpOffset 50",
                                                                              "CameraOffset 0",
                                                                              "bScaleDistanceWithSpeed False",
                                                                              ],
                          "GD_Sage_FanBoat.CameraDefs.Camera_DriverSeat": ["CameraOffset 0",
                                                                           "CameraPitchDownOffset -50",
                                                                           "CameraPitchUpOffset 45",
                                                                           "BaseCameraPosition (X=15,Y=-3,Z=60)",
                                                                           "bScaleDistanceWithSpeed False",
                                                                           ],
                          "GD_Orchid_Hovercraft.CameraDefs.Camera_DriverSeat": ["CameraOffset 0",
                                                                                "CameraPitchDownOffset 0",
                                                                                "CameraPitchUpOffset 45",
                                                                                "BaseCameraPosition (X=10,Y=0,Z=75)",
                                                                                "bScaleDistanceWithSpeed False",
                                                                                ]},

            "assassin": {"GD_Runner_Streaming.CameraDefs.Camera_DriverSeat": ["CameraOffset 0",
                                                                              "CameraPitchDownOffset -20",
                                                                              "CameraPitchUpOffset 50",
                                                                              "BaseCameraPosition (Z=65)",
                                                                              "bScaleDistanceWithSpeed False",
                                                                              ],
                         "GD_BanditTechnical.CameraDefs.Camera_DriverSeat": ["CameraPitchDownOffset -10",
                                                                             "BaseCameraPosition (X=-1,Y=0,Z=70)",
                                                                             "CameraPitchUpOffset 50",
                                                                             "CameraOffset 0",
                                                                             "bScaleDistanceWithSpeed False",
                                                                             ],
                         "GD_Sage_FanBoat.CameraDefs.Camera_DriverSeat": ["CameraOffset 0",
                                                                          "CameraPitchDownOffset -50",
                                                                          "CameraPitchUpOffset 45",
                                                                          "BaseCameraPosition (X=15,Y=-3,Z=60)",
                                                                          "bScaleDistanceWithSpeed False",
                                                                          ],
                         "GD_Orchid_Hovercraft.CameraDefs.Camera_DriverSeat": ["CameraOffset 0",
                                                                               "CameraPitchDownOffset 0",
                                                                               "CameraPitchUpOffset 45",
                                                                               "BaseCameraPosition (X=10,Y=0,Z=75)",
                                                                               "bScaleDistanceWithSpeed False",
                                                                               ]},

            "lilac": {"GD_Runner_Streaming.CameraDefs.Camera_DriverSeat": ["CameraOffset 0",
                                                                           "CameraPitchDownOffset -20",
                                                                           "CameraPitchUpOffset 50",
                                                                           "BaseCameraPosition (Z=65)",
                                                                           "bScaleDistanceWithSpeed False",
                                                                           ],
                      "GD_BanditTechnical.CameraDefs.Camera_DriverSeat": ["CameraPitchDownOffset -10",
                                                                          "BaseCameraPosition (X=-1,Y=0,Z=70)",
                                                                          "CameraPitchUpOffset 50",
                                                                          "CameraOffset 0",
                                                                          "bScaleDistanceWithSpeed False",
                                                                          ],
                      "GD_Sage_FanBoat.CameraDefs.Camera_DriverSeat": ["CameraOffset 0",
                                                                       "CameraPitchDownOffset -50",
                                                                       "CameraPitchUpOffset 45",
                                                                       "BaseCameraPosition (X=15,Y=-3,Z=60)",
                                                                       "bScaleDistanceWithSpeed False",
                                                                       ],
                      "GD_Orchid_Hovercraft.CameraDefs.Camera_DriverSeat": ["CameraOffset 0",
                                                                            "CameraPitchDownOffset 0",
                                                                            "CameraPitchUpOffset 45",
                                                                            "BaseCameraPosition (X=10,Y=0,Z=75)",
                                                                            "bScaleDistanceWithSpeed False",
                                                                            ]},

            "siren": {"GD_Runner_Streaming.CameraDefs.Camera_DriverSeat": ["CameraOffset 0",
                                                                           "CameraPitchDownOffset -20",
                                                                           "CameraPitchUpOffset 50",
                                                                           "BaseCameraPosition (Z=65)",
                                                                           "bScaleDistanceWithSpeed False",
                                                                           ],
                      "GD_BanditTechnical.CameraDefs.Camera_DriverSeat": ["CameraPitchDownOffset -10",
                                                                          "BaseCameraPosition (X=-1,Y=0,Z=70)",
                                                                          "CameraPitchUpOffset 50",
                                                                          "CameraOffset 0",
                                                                          "bScaleDistanceWithSpeed False", ],
                      "GD_Sage_FanBoat.CameraDefs.Camera_DriverSeat": ["CameraOffset 0",
                                                                       "CameraPitchDownOffset -50",
                                                                       "CameraPitchUpOffset 45",
                                                                       "BaseCameraPosition (X=15,Y=-3,Z=60)",
                                                                       "bScaleDistanceWithSpeed False",
                                                                       ],
                      "GD_Orchid_Hovercraft.CameraDefs.Camera_DriverSeat": ["CameraOffset 0",
                                                                            "CameraPitchDownOffset 0",
                                                                            "CameraPitchUpOffset 45",
                                                                            "BaseCameraPosition (X=10,Y=0,Z=80)",
                                                                            "bScaleDistanceWithSpeed False",
                                                                            ]},

            "soldier": {"GD_Runner_Streaming.CameraDefs.Camera_DriverSeat": ["CameraOffset 0",
                                                                             "CameraPitchDownOffset -20",
                                                                             "CameraPitchUpOffset 50",
                                                                             "BaseCameraPosition (Z=65)",
                                                                             "bScaleDistanceWithSpeed False",
                                                                             ],
                        "GD_BanditTechnical.CameraDefs.Camera_DriverSeat": ["CameraPitchDownOffset -10",
                                                                            "BaseCameraPosition (X=-1,Y=0,Z=70)",
                                                                            "CameraPitchUpOffset 50",
                                                                            "CameraOffset 0",
                                                                            "bScaleDistanceWithSpeed False",
                                                                            ],
                        "GD_Sage_FanBoat.CameraDefs.Camera_DriverSeat": ["CameraOffset 0",
                                                                         "CameraPitchDownOffset -50",
                                                                         "CameraPitchUpOffset 45",
                                                                         "BaseCameraPosition (X=15,Y=-3,Z=60)",
                                                                         "bScaleDistanceWithSpeed False",
                                                                         ],
                        "GD_Orchid_Hovercraft.CameraDefs.Camera_DriverSeat": ["CameraOffset 0",
                                                                              "CameraPitchDownOffset 0",
                                                                              "CameraPitchUpOffset 45",
                                                                              "BaseCameraPosition (X=10,Y=0,Z=75)",
                                                                              "bScaleDistanceWithSpeed False",
                                                                              ]},

            "tulip": {"GD_Runner_Streaming.CameraDefs.Camera_DriverSeat": ["CameraOffset 0",
                                                                           "CameraPitchDownOffset -20",
                                                                           "CameraPitchUpOffset 50",
                                                                           "BaseCameraPosition (Z=65)",
                                                                           "bScaleDistanceWithSpeed False",
                                                                           ],
                      "GD_BanditTechnical.CameraDefs.Camera_DriverSeat": ["CameraPitchDownOffset -10",
                                                                          "BaseCameraPosition (X=-1,Y=0,Z=70)",
                                                                          "CameraPitchUpOffset 50",
                                                                          "CameraOffset 0",
                                                                          "bScaleDistanceWithSpeed False",
                                                                          ],
                      "GD_Sage_FanBoat.CameraDefs.Camera_DriverSeat": ["CameraOffset 0",
                                                                       "CameraPitchDownOffset -50",
                                                                       "CameraPitchUpOffset 45",
                                                                       "BaseCameraPosition (X=15,Y=-3,Z=60)",
                                                                       "bScaleDistanceWithSpeed False",
                                                                       ],
                      "GD_Orchid_Hovercraft.CameraDefs.Camera_DriverSeat": ["CameraOffset 0",
                                                                            "CameraPitchDownOffset 0",
                                                                            "CameraPitchUpOffset 45",
                                                                            "BaseCameraPosition (X=10,Y=0,Z=75)",
                                                                            "bScaleDistanceWithSpeed False",
                                                                            ]},
            "default": {"GD_Runner_Streaming.CameraDefs.Camera_DriverSeat": ["CameraOffset -800",
                                                                             "CameraPitchDownOffset 0",
                                                                             "CameraPitchUpOffset 0",
                                                                             "BaseCameraPosition (Z=200)",
                                                                             "bScaleDistanceWithSpeed True",
                                                                             ],
                        "GD_BanditTechnical.CameraDefs.Camera_DriverSeat": ["CameraPitchDownOffset 0",
                                                                            "BaseCameraPosition (X=40,Y=0,Z=300)",
                                                                            "CameraPitchUpOffset 100",
                                                                            "CameraOffset -1300",
                                                                            "bScaleDistanceWithSpeed True",
                                                                            ],
                        "GD_Sage_FanBoat.CameraDefs.Camera_DriverSeat": ["CameraOffset -1100",
                                                                         "CameraPitchDownOffset 0",
                                                                         "CameraPitchUpOffset -250",
                                                                         "BaseCameraPosition (X=0,Y=0,Z=300)",
                                                                         "bScaleDistanceWithSpeed True",
                                                                         ],
                        "GD_Orchid_Hovercraft.CameraDefs.Camera_DriverSeat": ["CameraOffset -1100",
                                                                              "CameraPitchDownOffset 0",
                                                                              "CameraPitchUpOffset -250",
                                                                              "BaseCameraPosition (X=0,Y=0,Z=300)",
                                                                              "bScaleDistanceWithSpeed True",
                                                                              ]}
        }

    def Enable(self):
        def EndLoad(caller: UObject, function: UFunction, params: FStruct) -> bool:
            self.calc_driver_cam()
            return True

        unrealsdk.RegisterHook("WillowGame.VehicleSpawnStationTerminal.UnlockForOtherUsers", "LoadCar",
                               EndLoad)

    def Disable(self):
        unrealsdk.RemoveHook("WillowGame.VehicleSpawnStationTerminal.UnlockForOtherUsers", "LoadCar")

    def GameInputPressed(self, input):
        if input.Name == "Driver Cam":
            self.is_first_person = not self.is_first_person
            self.calc_driver_cam()

    def calc_driver_cam(self):
        pc = bl2tools.get_player_controller()
        if pc and pc.Pawn:
            vh = bl2tools.get_obj_path_name(pc.CharacterClass).lower()
            if not self.is_first_person:
                vh = "default"
            for char, data in self.settings.items():
                if char not in vh:
                    continue
                for cam, attrs in data.items():
                    if not unrealsdk.FindObject("PassengerCameraDefinition", cam):
                        continue
                    for att in attrs:
                        bl2tools.console_command(f"set {cam} {att}")


unrealsdk.RegisterMod(FPDriver())
