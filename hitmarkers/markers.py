from typing import Tuple

from Mods.canvaslib import Canvas, relative_to_screen_coordinates
from Mods.coroutines import PostRenderCoroutine, Time
from .options import CritMarkers, KillMarkers, Markers, NormalMarkers


def draw_hitmarker(was_crit: bool = False) -> PostRenderCoroutine:
    total_duration = Markers.lifetime.CurrentValue / 1000
    remaining_duration = Markers.lifetime.CurrentValue / 1000
    width = Markers.thickness.CurrentValue

    # Set the initial color and alpha values
    marker_options = CritMarkers if was_crit else NormalMarkers
    color = (marker_options.color_b.CurrentValue,
             marker_options.color_g.CurrentValue,
             marker_options.color_r.CurrentValue)
    start_alpha = marker_options.color_a.CurrentValue

    size = Markers.size
    offset = Markers.inner_offset  # cache the offset value
    while True:
        yield None
        canvas = yield
        cx, cy = relative_to_screen_coordinates(canvas, 0.5, 0.5)

        progress = remaining_duration / total_duration

        # fade out the marker over time
        alpha = int(start_alpha * progress) if Markers.fade_out.CurrentValue else start_alpha
        col = color + (alpha,)

        if Markers.grow_out.CurrentValue:
            # mave the markers bounds outwards over time
            # Scales out by up to 100% of the size
            inner_offset = offset.CurrentValue + offset.CurrentValue * (1 - progress)
        else:
            inner_offset = offset.CurrentValue
        outer_offset = inner_offset + size.CurrentValue

        with Canvas(canvas) as c:
            draw_marker(c, cx, cy, inner_offset, outer_offset, width, col)
        remaining_duration -= Time.unscaled_delta_time
        if remaining_duration <= 0:
            break


def draw_killmarker() -> PostRenderCoroutine:
    total_duration = Markers.lifetime.CurrentValue / 1000
    remaining_duration = Markers.lifetime.CurrentValue / 1000
    width = Markers.thickness.CurrentValue * 1.5

    # Set the initial color and alpha values
    color = (KillMarkers.color_b.CurrentValue,
             KillMarkers.color_g.CurrentValue,
             KillMarkers.color_r.CurrentValue)
    start_alpha = KillMarkers.color_a.CurrentValue

    size = Markers.size
    offset = Markers.inner_offset  # cache the offset value
    while True:
        yield None
        canvas = yield
        cx, cy = relative_to_screen_coordinates(canvas, 0.5, 0.5)

        progress = remaining_duration / total_duration

        # fade out the marker over time
        alpha = int(start_alpha * progress) if Markers.fade_out.CurrentValue else start_alpha
        col = color + (alpha,)

        # Killmarkers start at the end of the normal markers
        _end = offset.CurrentValue + size.CurrentValue
        if Markers.grow_out.CurrentValue:
            inner_offset = _end * 1.5 + offset.CurrentValue * (1 - progress)
        else:
            inner_offset = _end * 1.5
        outer_offset = inner_offset + size.CurrentValue * 2

        with Canvas(canvas) as c:
            draw_marker(c, cx, cy, inner_offset, outer_offset, width, col)
        remaining_duration -= Time.unscaled_delta_time
        if remaining_duration <= 0:
            break


def draw_marker(
        c: Canvas,
        cx: float,
        cy: float,
        inner_offset: float,
        outer_offset: float,
        width: float,
        col: Tuple[int, int, int, int]
) -> None:
    c.draw_line(  # top left to bottom right
        x1=cx - inner_offset, y1=cy - inner_offset,
        x2=cx - outer_offset, y2=cy - outer_offset,
        width=width, color=col
    )
    c.draw_line(  # top right to bottom left
        x1=cx - inner_offset, y1=cy + inner_offset,
        x2=cx - outer_offset, y2=cy + outer_offset,
        width=width, color=col
    )
    c.draw_line(  # bottom left to top right
        x1=cx + inner_offset, y1=cy - inner_offset,
        x2=cx + outer_offset, y2=cy - outer_offset,
        width=width, color=col
    )
    c.draw_line(  # bottom right to top left
        x1=cx + inner_offset, y1=cy + inner_offset,
        x2=cx + outer_offset, y2=cy + outer_offset,
        width=width, color=col
    )
