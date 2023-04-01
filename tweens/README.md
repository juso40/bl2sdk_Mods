# tweens
*A tweening library*  

This is a library, it does not add any functionality on its own. 

## Quick start
```python
from Mods.tweens import Tween, cubic_out


pawn = unrelsdk.GetEngine().GamePlayers[0].Actor.Pawn

# Create a tween
tween: Tween = Tween()
# Add a property to tween
tween.tween_property(
    pawn.Location,    # the object to tween
    "Z",              # the property to tween
    final_value=500,  # the final value of the property
    duration=5        # how long the tween should take
).as_relative(        # make the final value relative to the current value
).transition(         # add a transition function
    cubic_out         # the transition function
)
# Start the tween
tween.start()
...
# Kill the tween object manually, this will stop all animations
tween.kill()
```

## Advanced usage
### Sequential tweens
```python
from Mods.tweens import Tween, cubic_out

pawn = unrelsdk.GetEngine().GamePlayers[0].Actor.Pawn

# Sequential tweens
tween: Tween = Tween()
tween.tween_property(  # move the pawn 500 units up
    pawn.Location,
    "Z", 
    final_value=500, 
    duration=5
).as_relative().transition(cubic_out)
# After 5 seconds move the pawn 500 units on the X axis
tween.tween_property(
    pawn.Location,
    "X", 
    final_value=500, 
    duration=5
).as_relative().transition(cubic_out)
tween.start()
```

### Parallel tweens
```python
from Mods.tweens import Tween, cubic_out

pawn = unrelsdk.GetEngine().GamePlayers[0].Actor.Pawn

tween: Tween = Tween()
tween.tween_property(  # move the pawn 500 units up
    pawn.Location,
    "Z", 
    final_value=500, 
    duration=5
).as_relative().transition(cubic_out)
tween.tween_property(  # move the pawn 500 units on the X axis
    pawn.Location,
    "X", 
    final_value=500, 
    duration=5
).as_relative().transition(cubic_out)
tween.set_parallel(True)  # Set the tween to run the animations in parallel
tween.start()
```
### Tweening Skins
```python
import unrealsdk  # type: ignore

from Mods.ModMenu import EnabledSaveType, Game, ModTypes, RegisterMod, SDKMod
from Mods.tweens import (
    Tween,
    elastic_out,
)


class SkinAnim(SDKMod):
    Name: str = "SkinAnim"
    Description: str = "Animate skins."
    Author: str = "juso"
    Version: str = "1.0"
    Types: ModTypes = ModTypes.Content
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadWithSettings
    SupportedGames: Game = Game.BL2

    def __init__(self):
        self.skin: str = (
            "Common_GunMaterials.Materials.SMG.Mati_Hyperion_UniqueSMG_Commerce"
        )
        self.tweener: Tween = Tween()

    def Enable(self) -> None:
        self.tween_skin()

    def Disable(self) -> None:
        if self.tweener.is_running():
            self.tweener.kill()

    def tween_skin(self) -> None:
        if self.tweener.is_running():
            self.tweener.kill()
        material: unrealsdk.UObject = unrealsdk.FindObject(
            "MaterialInstanceConstant", self.skin
        )
        if not material:
            return
        self.tweener = Tween()
        t = self.tweener
        t.tween_callable(
            self.change_skin,
            start_value=(0, 1, 4, 1),
            final_value=(2, 4, 8, 1),
            duration=0.2,
        ).transition(elastic_out)
        t.tween_timer(0.2)
        t.tween_callable(
            self.change_skin,
            start_value=(2, 4, 8, 1),
            final_value=(0, 1, 4, 1),
            duration=0.4,
        ).transition(elastic_out)
        t.set_loops(-1)
        t.start()

    def change_skin(self, value: tuple) -> None:
        mat = unrealsdk.FindObject("MaterialInstanceConstant", self.skin)
        if not mat:
            return
        mat.SetVectorParameterValue("p_DecalColor", value)


RegisterMod(SkinAnim())
```

![Borderlands2_gFf64WABEF](https://user-images.githubusercontent.com/39841117/229279066-21b420b8-0880-4c3a-9dc7-39e706ddca8e.gif)

Note, this library was not made with animating skins in mind. Interpolating between colors (tuples), probably wont yield
your expected results in many cases.