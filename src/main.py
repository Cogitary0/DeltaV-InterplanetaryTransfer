from constants import G, G_KM
from data.data_planet import Earth
from tools.astrodynamics import Orbit


def main():
    orbit = Orbit(False)

    height = 100

    print(orbit.transfer(Earth,
                         Earth['radius'],
                         Earth['radius']+height))


if __name__ == "__main__":
    main()
