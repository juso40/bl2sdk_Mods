from math import cos, pi, sin, sqrt
from typing import Callable


def linear(t: float) -> float:
    return t


def quad_in(t: float) -> float:
    return t * t


def quad_out(t: float) -> float:
    return t * (2 - t)


def quad_in_out(t: float) -> float:
    if t < 0.5:
        return 2 * t * t

    return -1 + (4 - 2 * t) * t


def cubic_in(t: float) -> float:
    return t * t * t


def cubic_out(t: float) -> float:
    t -= 1
    return t * t * t + 1


def cubic_in_out(t: float) -> float:
    if t < 0.5:
        return 4 * t * t * t

    t -= 1
    return 4 * t * t * t + 1


def quart_in(t: float) -> float:
    return t * t * t * t


def quart_out(t: float) -> float:
    t -= 1
    return 1 - t * t * t * t


def quart_in_out(t: float) -> float:
    if t < 0.5:
        return 8 * t * t * t * t

    t -= 1
    return 1 - 8 * t * t * t * t


def quint_in(t: float) -> float:
    return t * t * t * t * t


def quint_out(t: float) -> float:
    t -= 1
    return 1 + t * t * t * t * t


def quint_in_out(t: float) -> float:
    if t < 0.5:
        return 16 * t * t * t * t * t

    t -= 1
    return 1 + 16 * t * t * t * t * t


def sine_in(t: float) -> float:
    return 1 - cos(t * pi / 2)


def sine_out(t: float) -> float:
    return sin(t * pi / 2)


def sine_in_out(t: float) -> float:
    return 0.5 * (1 - cos(pi * t))


def expo_in(t: float) -> float:
    return 0 if t == 0 else pow(2, 10 * t - 10)


def expo_out(t: float) -> float:
    return 1 if t == 1 else 1 - pow(2, -10 * t)


def expo_in_out(t: float) -> float:
    if t == 0:
        return 0

    if t == 1:
        return 1

    if t < 0.5:
        return 0.5 * pow(2, (20 * t) - 10)

    return -0.5 * pow(2, (-20 * t) + 10) + 1


def circ_in(t: float) -> float:
    return 1 - sqrt(1 - t * t)


def circ_out(t: float) -> float:
    t -= 1
    return sqrt(1 - t * t)


def circ_in_out(t: float) -> float:
    if t < 0.5:
        return 0.5 * (1 - sqrt(1 - 4 * t * t))

    return 0.5 * (sqrt(-((2 * t) - 3) * ((2 * t) - 1)) + 1)


def back_in(t: float) -> float:
    return t * t * t - t * sin(t * pi)


def back_out(t: float) -> float:
    t -= 1
    return 1 + t * t * t + t * sin(t * pi)


def back_in_out(t: float) -> float:
    if t < 0.5:
        return 0.5 * (2 * t * t * t - t * sin(t * pi))

    t -= 1
    return 0.5 * (2 * t * t * t + t * sin(t * pi)) + 1


def elastic_in(t: float) -> float:
    return sin(13 * pi / 2 * t) * pow(2, 10 * (t - 1))


def elastic_out(t: float) -> float:
    return sin(-13 * pi / 2 * (t + 1)) * pow(2, -10 * t) + 1


def elastic_in_out(t: float) -> float:
    if t < 0.5:
        return 0.5 * sin(13 * pi / 2 * (2 * t)) * pow(2, 10 * ((2 * t) - 1))

    return 0.5 * (sin(-13 * pi / 2 * ((2 * t - 1) + 1)) * pow(2, -10 * (2 * t - 1)) + 2)


def bounce_in(t: float) -> float:
    return 1 - bounce_out(1 - t)


def bounce_out(t: float) -> float:
    if t < 4 / 11.0:
        return (121 * t * t) / 16.0
    if t < 8 / 11.0:
        return (363 / 40.0 * t * t) - (99 / 10.0 * t) + 17 / 5.0
    if t < 9 / 10.0:
        return (4356 / 361.0 * t * t) - (35442 / 1805.0 * t) + 16061 / 1805.0
    return (54 / 5.0 * t * t) - (513 / 25.0 * t) + 268 / 25.0


def bounce_in_out(t: float) -> float:
    if t < 0.5:
        return 0.5 * bounce_in(t * 2)

    return 0.5 * bounce_out(t * 2 - 1) + 0.5


def ease(
    alpha: float,
    start=0,
    end=1,
    duration: float = 1,
    transition_function: Callable[[float], float] = linear,
) -> float:
    t: float = alpha / duration
    a: float = transition_function(t)
    return end * a + start * (1 - a)
