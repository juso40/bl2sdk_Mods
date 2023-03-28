# uemath
A library for various math functions related to UE3 Vectors and Rotators.

Inclueds wrapper classes for FVector and FRotator to make them more usable in python.

Example:
```python
from Mods.uemath import Vector, Rotator, look_at

pc = unrealsdk.GetEngine().GamePlayers[0].Actor

# tp player 1000 units forward
pc_forward_vec = Vector(pc.Rotator)  # Get the players forward vector directly from its Rotator
pc.Pawn.Location = (Vector(pc.Pawn.Location) + pc_forward_vec*1000).to_tuple()

# make the player look at (0, 0, 0)
look_at(pc, (0, 0, 0))
# or use:
pc.Rotation = Rotator(pc.Rotation).look_at(Vector()).to_tuple()
```

