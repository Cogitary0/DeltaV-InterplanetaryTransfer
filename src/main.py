from constants import G
from data.data_planet import Mercury

# from data.data_planet_ksp import DATA_PLANET as planet


def main():
    print(round(Mercury['g0'], 4))


if __name__ == "__main__":
    main()
