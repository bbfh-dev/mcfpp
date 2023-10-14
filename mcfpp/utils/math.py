import math


def clamp(value: float, min_value: float, max_value: float):
    return max(min_value, min(value, max_value))


def vec2quat(x: float, y: float, z: float) -> tuple[float, float, float, float]:
    angle = max(x, y, z)
    vec = [
        clamp(x, -angle, angle) / angle,
        clamp(y, -angle, angle) / angle,
        clamp(z, -angle, angle) / angle,
    ]
    rad_angle = ((math.pi * angle) / 180) / 2
    return (
        round(vec[0] * math.sin(rad_angle), 3),
        round(vec[1] * math.sin(rad_angle), 3),
        round(vec[2] * math.sin(rad_angle), 3),
        round(math.cos(rad_angle), 3),
    )
