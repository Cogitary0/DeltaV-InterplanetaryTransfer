from constants import G
from data.data_planet import *
from tools.astrodynamics import *


def main():
    height = 100_000

    print(transfer(Earth,
                   Earth['radius_meters'],
                   height))

    print(Pluto['period'])


if __name__ == "__main__":
    main()