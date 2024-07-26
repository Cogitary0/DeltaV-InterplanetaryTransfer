from constants import G
from data.data_planet import *
from tools.astrodynamics import *


def main():
    height = 100_000

    print(transfer(Earth,
                   Earth['radius_meters'],
                   Earth['radius_meters'] + height))

    print(orbit_velocity(Earth, 6704490.9953, 6437215.67127))

    print(orbital_period(Earth,solve_ellipse_semi_major_axis(6704490.9953, 6437215.67127)))
    print(period(Earth, solve_ellipse_semi_major_axis(6704490.9953, 6437215.67127)))


if __name__ == "__main__":
    main()
