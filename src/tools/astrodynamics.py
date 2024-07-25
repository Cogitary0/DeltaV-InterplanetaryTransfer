from src.constants import *
from math import sqrt

number = float | int


def transfer(body: dict,
             height_start_orbit: number,
             height_end_orbit: number
             ) -> dict[str, number]:
    MU = body['mu']
    R0 = height_start_orbit
    R1 = height_start_orbit + height_end_orbit
    SUM_R = R0 + R1

    v0 = sqrt(MU / R0)
    v1 = sqrt(MU / R1)

    dV0 = v0 * (SQRT_2 * sqrt(R1 / SUM_R) - 1)
    dV1 = v1 * (1 - sqrt(2 * R0 / SUM_R))

    return {"v0": v0,
            "v1": v1,
            "dV0": dV0,
            "dV1": dV1,
            "total": dV0 + dV1}


def c3(body: dict, speed_spacecraft: number):
    return (0.5 * speed_spacecraft ** 2) - (body['mu'] / body['radius_meters'])


def solve_ellipse_semi_major_axis(ap: number, pe: number) -> float:
    rmax, rmin = max(ap, pe), min(ap, pe)
    return (rmax + rmin) / 2


def solve_ellipse_semi_minor_axis(ap: number, pe: number) -> float:
    rmax, rmin = max(ap, pe), min(ap, pe)
    return sqrt(rmax * rmin)


def energy(body: dict,
           mass_spacecraft: number,
           sma: number) -> float:
    return (-body['mu'] * mass_spacecraft) / 2 * sma


def orbital_period(body: dict, ellipse_semi_major_axis: number) -> number:
    return TWO_PI * sqrt(ellipse_semi_major_axis ** 3 / body['mu']) / 1000


def parabolic_speed(body, height) -> float:
    return (2 * body["mu"] / (body['radius_meters'] + height)) ** 0.5


def escape_velocity(body: dict) -> float:
    return SQRT_2 * sqrt(body["g0"] * body["radius_meters"])
