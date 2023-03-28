from math import pi

__all__ = [
    "PI",
    "URU_360",
    "URU_180",
    "URU_90",
    "URU_45",
    "URU_1",
    "URU_TO_RADIANS",
    "RADIANS_TO_URU",
]


PI = pi

# In UnrealScript, rotations are neither expressed in degrees nor radians.
# They are expressed in Unreal Units (URUs), which run from 0 to 65536 (2^16).
# https://docs.unrealengine.com/udk/Two/CoreUnrealScriptObjects.html#Structures
URU_360 = 65536
URU_180 = 32768
URU_90 = URU_180 // 2  # 16384
URU_45 = URU_180 // 4  # 8192
URU_1 = URU_360 // 360  # ~182

URU_TO_RADIANS = PI / URU_180  # Multiply by this to convert from Uru to radians
RADIANS_TO_URU = (
    URU_180 / PI
)  # Multiply by this to convert from radians to Uru  value is
