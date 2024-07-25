from math import sqrt
from src.constants import TWO_PI, G, MU_SUN
from src.tools.astrodynamics import solve_ellipse_semi_major_axis

Sun = {
    'name'            : 'Sun',
    'ID'              : 000,
    'mass'            : 1.989e30,
    'mu'              : 1.989e30 * G,
    'radius'          : 695510.0
}


# main planets
Mercury = {
    'name'            : 'Mercury',
    'ID'              : 100,
    'mass'            : 3.301e23,
    'mu'              : 3.301e23 * G,
    'radius'          : 2440.5,
    'sma'             : 57909e6,  # km
    'SOI'             : 1.1241e5  # km
}

Venus = {
    'name'            : 'Venus',
    'ID'              : 200,
    'mass'            : 4.867e24,
    'mu'              : 3.2485859200000006E+05,
    'radius'          : 6051.8,
    'sma'             : 108209e6,   # km
    'SOI'             : 617183.2511  # km

}

Earth = {
    'name'            : 'Earth',
    'ID'              : 300,
    'mass'            : 5.972e24,
    'mu'              : 5.972e24 * G,
    'radius'          : 6378.0,
    'J2'              : 1.081874e-3,
    'sma'             : 149598e6,  # km
    'SOI'             : 926006.6608  # km
}

Mars = {
    'name'            : 'Mars',
    'ID'              : 400,
    'mass'            : 6.4171e23,
    'mu'              : 6.4171e23 * G,
    'radius'          : 3389.5,
    'sma'             : 227956e6,  # km
    'SOI'             : 0.578e6   # km
}

Jupiter = {
    'name'            : 'Jupiter',
    'ID'              : 500,
    'mass'            : 1.8982e27,
    'mu'              : 1.8982e27 * G,
    'radius'          : 71490.0,
    'sma'             : 778570e6,  # km
    'SOI'             : 48.2e6    # km
}

Saturn = {
    'name'            : 'Saturn',
    'ID'              : 600,
    'mass'            : 5.6834e26,
    'mu'              : 5.6834e26 * G,
    'radius'          : 60270,
    'sma'             : 1433531e6,  # km
    'SOI'             : 54.787e6    # km
}

Uranus = {
    'name'            : 'Uranus',
    'ID'              : 700,
    'mass'            : 8.6811e24,
    'mu'              : 8.6811e24 * G,
    'radius'          : 25560,
    'sma'             : 2867043e6,  # km
    'SOI'             : 5.1785e7  # km
}

Neptune = {
    'name'            : 'Neptune',
    'ID'              : 800,
    'mass'            : 1.0241e25,
    'mu'              : 1.0241e25 * G,
    'radius'          : 24760,
    'sma'             : 4514953e6,  # km
    'SOI'             : 8.6589e7  # km
}

Pluto = {
    'name'            : 'Pluto',
    'ID'              : 900,
    'mass'            : 1.3029e21,
    'mu'              : 1.3029e21 * G,
    'radius'          : 1188,   # km
    'sma'             : 5869656e6  # km
}


#moons
Moon = {
    'name'            : 'Moon',
    'ID'              : 301,
    'mass'            : 7.342e22,
    'mu'              : 7.342e22 * G,
    'radius'          : 1737.4,
    'J2'              : 1.081874e-3,
    'sma'             : 149596e6,  # km
    'SOI'             : 926006.6608  # km
}

Io = {
    'name'            : 'Io',
    'ID'              : 501,
    'mass'            : 1.898e27,
    'mu'              : 5.959916033410404E+03,
    'radius'          : 1821.6,
    'sma'             : 778725e6
}

Europa = {
    'name'            : 'Europa',
    'ID'              : 502,
    'mu'              : 3.202738774922892E+03,
    'radius'          : 1560.8,
    'sma'             : 778.969e6
}

Ganymede = {
    'name'            : 'Ganymede',
    'ID'              : 503,
    'mu'              : 9.887834453334144E+03,
    'radius'          : 2631.2,
    'sma'             : 779377e6
}

Callisto = {
    'name'            : 'Callisto',
    'ID'              : 504,
    'mu'              : 7.179289361397270E+03,
    'radius'          : 2410.3,
    'sma'             : 780182e6
}

bodies = [
    Sun,
    Mercury,
    Venus,
    Earth, Moon,
    Mars,
    Jupiter, Io, Europa, Ganymede, Callisto,
    Saturn,
    Neptune,
    Uranus,
    Pluto
]


for body in bodies:
    body['radius_meters'] = body['radius'] * 1000
    body['g0'] = body['mu'] / body['radius_meters']**2
    body['period'] = TWO_PI * sqrt(body['sma']**3 / MU_SUN) / 86400 if body['ID'] != 000 else None
