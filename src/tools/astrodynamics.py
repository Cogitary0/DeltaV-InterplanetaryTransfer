from src.constants import G, SQRT_2
from math import sqrt


def transfer(body: dict,
             height_start_orbit: float | int,
             height_end_orbit: float | int
             ) -> dict[str, float]:

    MU = body['mu']
    R0 = height_start_orbit
    R1 = height_start_orbit + height_end_orbit
    SUM_R = R0 + R1

    v0 = sqrt(MU / R0)
    v1 = sqrt(MU / R1)

    dV0 = sqrt(MU / R0) * (SQRT_2 * sqrt(R1 / SUM_R) - 1)
    dV1 = v1 * (1 - sqrt(2 * R0 / SUM_R))

    return {"v0": v0,
            "v1": v1,
            "dV0": dV0,
            "dV1": dV1}


def c3(body: dict, speed_spacecraft: float | int):
    return (0.5 * speed_spacecraft**2) - (body['mu']/body['radius_meters'])

def solve_ellipse_semi_major_axis(ap: float | int, pe: float | int) -> float: #sMa
    rmax, rmin = max(ap, pe), min(ap, pe)
    return (rmax + rmin) / 2

def solve_ellipse_semi_minor_axis(ap: float | int, pe: float | int) -> float: #sma
    rmax, rmin = max(ap, pe), min(ap, pe)
    return sqrt(rmax * rmin)
def energy(body: dict,
           mass_spacecraft: float | int,
           sma: float | int) -> float:
    return (-body['mu'] * mass_spacecraft) / 2 * sma


def parabolic_speed(body, height) -> float:
    return (2 * body["mu"] / (body['radius_meters'] + height)) ** 0.5

