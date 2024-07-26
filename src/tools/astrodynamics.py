from src.constants import *
from math import sqrt

number  =   float | int
data    =   dict[str, float]

def transfer(body: dict,
             start_radius: number,
             end_radius: number) -> data:
    MU_SQRT = sqrt(body['mu'])
    R0 = start_radius
    R1 = end_radius
    SUM_R = R0 + R1

    v0 = MU_SQRT / sqrt(R0)
    v1 = MU_SQRT / sqrt(R1)

    dv0 = v0 * (SQRT_2 * sqrt(R1 / SUM_R) - 1)
    dv1 = v1 * (1 - SQRT_2 * (R0 / SUM_R))

    return {"v0": v0,
            "v1": v1,
            "dv0": dv0,
            "dv1": dv1,
            "total": dv0 + dv1}


def c3(body: dict, vel_spacecraft: number) -> float:
    return (0.5 * vel_spacecraft ** 2) - (body['mu'] / body['radius_meters'])


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

def period(body: dict, semi_major_axis: number) -> number:
    return TWO_PI / sqrt(body['mu'] * semi_major_axis ** 1.5)

def parabolic_velocity(body, height) -> float:
    return (2 * body["mu"] / (body['radius_meters'] + height)) ** 0.5


def escape_velocity(body: dict) -> float:
    return SQRT_2 * sqrt(body["g0"] * body["radius_meters"])

def orbit_velocity(body: dict, radius_max: number, radius_min: number) -> data:
    MU_SQRT = sqrt(body['mu'])
    INV_SMA = 1 / solve_ellipse_semi_major_axis(radius_max, radius_min)
    return {"ap_vel" : MU_SQRT * sqrt((2 / radius_max) - INV_SMA),
            "pe_vel" : MU_SQRT * sqrt((2 / radius_min) - INV_SMA)}


def ecc(ap: number, pe: number) -> number:
    return (ap - pe) / (ap + pe)


def angular_momentum(body: dict, ap:number, ep: number) -> number:
    semimajor_axis = solve_ellipse_semi_major_axis(ap, ep)
    return sqrt(body['mu'] * semimajor_axis * (1 - ecc(ap, ep)**2))
