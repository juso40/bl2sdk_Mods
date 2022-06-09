from typing import List
import os

import unrealsdk

from ..ModMenu import EnabledSaveType, SDKMod, Hook, Game, OptionManager, ModTypes


def _get_pc() -> unrealsdk.UObject:
    return unrealsdk.GetEngine().GamePlayers[0].Actor


# noinspection PyUnusedLocal
class PP(SDKMod):
    Name = "Big Particle Party"
    Description = "Big PP allows you to increase/decrease the amount of some particles."
    Author = "Juso"
    Version = "1.0"
    Types = ModTypes.Utility
    SaveEnabledState = EnabledSaveType.LoadOnMainMenu
    SupportedGames = Game.BL2

    def __init__(self):
        super().__init__()
        self.PATH = os.path.dirname(os.path.realpath(__file__))
        self.Options: List[OptionManager.Options.Nested] = []
        self.particle_filters = ["BulletImpacts", "WEP", "GOR", "Explosions", "MuzzleFlash", "Trails",
                                 "Enemies", "CREA", "Shield", "ENV",
                                 ]
        for f in self.particle_filters:
            nested = OptionManager.Options.Nested(
                Caption=f,
                Description=f"Change settings related to {f} particles.",
                Children=[
                    OptionManager.Options.Slider(
                        Caption="Min Particles",
                        Description="Minimum number of particles to spawn.",
                        StartingValue=0,
                        MinValue=-1,
                        MaxValue=100,
                        Increment=1
                    ),
                    OptionManager.Options.Slider(
                        Caption="Max Particles",
                        Description="Maximum number of particles to spawn.",
                        StartingValue=0,
                        MinValue=-1,
                        MaxValue=100,
                        Increment=1
                    )
                ]
            )
            self.Options.append(nested)

    @Hook("WillowGame.WillowHUD.CreateWeaponScopeMovie")
    def apply_particles(
            self,
            caller: unrealsdk.UObject,
            function: unrealsdk.UFunction,
            params: unrealsdk.FStruct
    ) -> bool:
        return self.update_particles()

    def update_particles(self) -> bool:
        particles = unrealsdk.FindAll("ParticleSpriteEmitter")

        if not particles:
            return True

        # Keeping the following particles would cause too much pollution
        particles = [p for p in particles if "smoke" not in p.EmitterName.lower()]
        particles = [p for p in particles if "plume" not in p.EmitterName.lower()]
        particles = [p for p in particles if "specs" not in p.EmitterName.lower()]

        particles = [lod for p in particles for lod in p.LODLevels]
        filter_particles = {k: [p for p in particles if k in str(p)] for k in self.particle_filters}
        for filter_option in self.Options:
            min_val = filter_option.Children[0].CurrentValue
            max_val = filter_option.Children[1].CurrentValue
            for p in filter_particles[filter_option.Caption]:
                p.PeakActiveParticles = 5000
                p.RequiredModule.MaxDrawCount = 100000000  # Increase max draw count for particles

                p = p.SpawnModule
                bl = p.BurstList
                bl = p.BurstList
                try:
                    bl[0].Count = max_val
                    bl[0].CountLow = min_val
                except IndexError:
                    pass
        return True

    def Enable(self):
        super().Enable()

        def update_nested(nested_option):
            if isinstance(nested_option, OptionManager.Options.Value):
                self.ModOptionChanged(nested_option, nested_option.CurrentValue)
            elif isinstance(nested_option, OptionManager.Options.Nested):
                for child in nested_option.Children:
                    update_nested(child)

        for option in self.Options:
            update_nested(option)

    def Disable(self):
        super().Disable()


unrealsdk.RegisterMod(PP())
