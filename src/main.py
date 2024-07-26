from constants import G
from data.data_planet import *
from tools.astrodynamics import *


def main():
    height = 100_000

    print(transfer(Earth,
                   6.5e6,
                   13e6))

    print(orbit_velocity(Earth, 6.5e6, 13e6))

    print(angle_transfer(6704490.9953, 6437215.67127) * RAD2DEG)

    print(time_transfer(Earth, 6704490.9953, 6437215.67127))

if __name__ == "__main__":
    main()
