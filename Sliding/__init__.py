from typing import ClassVar

import unrealsdk

from ..ModMenu import SDKMod, Hook, EnabledSaveType, ModTypes

class Sliding(SDKMod):
    Name: str = "Sliding"
    Description: str = "Sliding in BL2."
    Author: str = "Juso"
    Version: str = "2.1"
    Types: ModTypes = ModTypes.Gameplay
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadWithSettings

    PACKAGE_NAME: ClassVar[str] = "Sliding"
    ATTR_PREFIX: ClassVar[str] = "Attr_"
    MODIFIER_PREFIX: ClassVar[str] = "Modifier_"
    MOVE_SPEED_SUFFIX: ClassVar[str] = "MoveSpeed"

    MOVE_SPEED_ATTRIBUTE_NAME: ClassVar[str] = "D_Attributes.GameplayAttributes.FootSpeed"

    def __init__(self):
        self.slide_duration = 2.0
        self.slide_speed = 2.2
        self.old_z = 0
        self.speed_modifier = None
        self.speed_attribute = None

    def Enable(self) -> None:
        super().Enable()
        self.create_objects()

    def create_objects(self) -> None:
        # Thanks to apples Mario mod for figuring out how to do this
        package = unrealsdk.FindObject("Package", self.PACKAGE_NAME)
        if package is None:
            package = unrealsdk.ConstructObject(
                Class="Package",
                Outer=None,
                Name=self.PACKAGE_NAME,
            )
            unrealsdk.KeepAlive(package)

        # Find MoveSpeed AttributeDefinition
        self.speed_attribute: unrealsdk.UObject = unrealsdk.FindObject(
            "AttributeDefinition",
            self.MOVE_SPEED_ATTRIBUTE_NAME
        )

        # Find or create SlideSpeed AttributeModifer
        self.speed_modifier: unrealsdk.UObject = unrealsdk.FindObject(
            "AttributeModifier",
            f"{self.PACKAGE_NAME}.Modifier_SlideSpeed"
        )
        if self.speed_modifier is None:
            self.speed_modifier = unrealsdk.ConstructObject(
                Class="AttributeModifier",
                Outer=package,
                Name="Modifier_SlideSpeed"
            )
            unrealsdk.KeepAlive(self.speed_modifier)
            self.speed_modifier.Type = 0  # MT_Scale
            self.speed_modifier.Value = self.slide_speed

    def update_speed_modifier(self) -> None:
        self.speed_modifier.Value = self.slide_speed

    @Hook("WillowGame.WillowPlayerController.PlayerWalking.PlayerMove")
    def handle_move(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct):
        pc = caller
        # Remove the modifier. Each Tick is a bit too much, but eh. Don't really care
        self.speed_attribute.RemoveAttributeModifier(pc.Pawn, self.speed_modifier)

        slope_delta = pc.Pawn.Location.Z - self.old_z
        if pc.Pawn.Acceleration.X == 0.0 and pc.Pawn.Acceleration.Y == 0.0:  # turn off sliding
            self.slide_duration = 0.0

        if (slope_delta * params.DeltaTime) > 0.0005:  # sliding up
            self.slide_duration -= (params.DeltaTime * 1.3)
            self.slide_speed -= (0.5 * params.DeltaTime)

        elif (slope_delta * params.DeltaTime) < -0.0005:  # down
            self.slide_duration -= (params.DeltaTime / 5)

        else:
            self.slide_duration -= params.DeltaTime
            self.slide_speed -= (0.3 * params.DeltaTime)

        # We are only sliding while we are ducked on the ground and moving
        if pc.bDuck and self.slide_duration > 0. and pc.Pawn.IsOnGroundOrShortFall():
            pc.Rotation.Roll = int(self.slide_duration * 700)  # Calculate Rotation Roll

            # While sliding re add the Attribute
            self.update_speed_modifier()
            self.speed_attribute.AddAttributeModifier(pc.Pawn, self.speed_modifier)
            self.slide_duration -= params.DeltaTime  # Remove time from max slide duration

        else:  # stopped duck or time over
            pc.Rotation.Roll = max(0, int(pc.Rotation.Roll - 3 * 700 * params.DeltaTime))  # Calculate Rotation Roll

        self.old_z = pc.Pawn.Location.Z
        return True

    @Hook("WillowGame.WillowPlayerInput.DuckPressed")
    def handle_duck(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct):
        pc = caller.Outer
        self.old_z = pc.Pawn.Location.Z
        if pc.bInSprintState:
            self.slide_duration = 2.0  # Reset slide duration
            self.slide_speed = 2.2  # Reset slide speed
        return True


unrealsdk.RegisterMod(Sliding())
