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


