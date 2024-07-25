from constants import G
from data.data_planet import Earth
from tools.astrodynamics import transfer


def main():
    height = 100_000

    print(transfer(Earth,
                   Earth['radius_meters'],
                   height))


if __name__ == "__main__":
    main()
