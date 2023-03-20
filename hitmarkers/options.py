from Mods.ModMenu import Options


class Markers:
    show_marker_in_menu = Options.Boolean("Marker Example", "Show markers continuously.", StartingValue=False)
    fade_out = Options.Boolean("Fade Out", "Fade out the hitmarkers over time.", StartingValue=True)
    grow_out = Options.Boolean("Grow", "Grow the hitmarkers over time.", StartingValue=True)
    inner_offset = Options.Slider(
        "Inner Offset", "Offset from the center of the screen.", MinValue=0, MaxValue=100, StartingValue=10, Increment=1
    )
    size = Options.Slider("Size", "Size of the marker.", MinValue=5, MaxValue=50, StartingValue=5, Increment=1)
    thickness = Options.Slider(
        "Thickness", "Thickness of the marker.", MinValue=1, MaxValue=20, StartingValue=3, Increment=1
    )
    lifetime = Options.Slider(
        "Lifetime", "Lifetime of the marker in milliseconds.", MinValue=100, MaxValue=1000, StartingValue=450,
        Increment=50
    )
    nested = Options.Nested(
        "Markers", "General settings for the hitmarkers.", Children=[
            show_marker_in_menu, fade_out, grow_out, inner_offset, size, thickness, lifetime
        ]
    )


class NormalMarkers:
    color_r = Options.Slider("Red", "Red color value.", MinValue=0, MaxValue=255, StartingValue=180, Increment=1)
    color_g = Options.Slider("Green", "Green color value.", MinValue=0, MaxValue=255, StartingValue=180, Increment=1)
    color_b = Options.Slider("Blue", "Blue color value.", MinValue=0, MaxValue=255, StartingValue=180, Increment=1)
    color_a = Options.Slider("Alpha", "Alpha color value.", MinValue=0, MaxValue=255, StartingValue=255, Increment=1)
    nested = Options.Nested(
        "Normal Markers", "Settings for normal hitmarkers.", Children=[
            color_r, color_g, color_b, color_a
        ]
    )


class CritMarkers:
    color_r = Options.Slider("Red", "Red color value.", MinValue=0, MaxValue=255, StartingValue=255, Increment=1)
    color_g = Options.Slider("Green", "Green color value.", MinValue=0, MaxValue=255, StartingValue=150, Increment=1)
    color_b = Options.Slider("Blue", "Blue color value.", MinValue=0, MaxValue=255, StartingValue=25, Increment=1)
    color_a = Options.Slider("Alpha", "Alpha color value.", MinValue=0, MaxValue=255, StartingValue=255, Increment=1)
    nested = Options.Nested(
        "Crit Markers", "Settings for crit hitmarkers.", Children=[
            color_r, color_g, color_b, color_a
        ]
    )


class KillMarkers:
    enabled = Options.Boolean("Enabled", "Enable kill markers.", StartingValue=True)
    color_r = Options.Slider("Red", "Red color value.", MinValue=0, MaxValue=255, StartingValue=205, Increment=1)
    color_g = Options.Slider("Green", "Green color value.", MinValue=0, MaxValue=255, StartingValue=10, Increment=1)
    color_b = Options.Slider("Blue", "Blue color value.", MinValue=0, MaxValue=255, StartingValue=10, Increment=1)
    color_a = Options.Slider("Alpha", "Alpha color value.", MinValue=0, MaxValue=255, StartingValue=255, Increment=1)
    nested = Options.Nested(
        "Kill Markers", "Settings for kill markers.", Children=[
            enabled, color_r, color_g, color_b, color_a
        ]
    )


options = [Markers.nested, NormalMarkers.nested, CritMarkers.nested, KillMarkers.nested]
