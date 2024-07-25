from src.constants import G, G_KM, SQRT_2
from math import sqrt


class Orbit:
    def __init__(self, q_convert_to_system_si: bool = True):
        self.q_convert_to_system_si = q_convert_to_system_si if q_convert_to_system_si else False

    def default_orbit_speed(self, body, height) -> float:
        return ((2 * body["mu"] / (body['radius_meters'] + height)) ** 0.5) / (
            1000 if self.q_convert_to_system_si else 1)

    def orbit_speed(self, body, height):
        ...

    def transfer(self,
                 body: dict,
                 height_start_orbit: float | int,
                 height_end_orbit: float | int
                 ) -> dict[str, float]:

        CONVERT_FACTOR = 1000 if self.q_convert_to_system_si else 1

        MU = body['mass'] * G_KM
        R0 = height_start_orbit
        R1 = height_end_orbit

        v0 = (MU / R0) ** 0.5
        v1 = (MU / R1) ** 0.5

        dV0 = sqrt(MU / R0) * (SQRT_2 * sqrt(R1 / (R0 + R1)) - 1)
        dV1 = v1 * (1 - sqrt(2 * R0 / (R0 + R1)))

        return {"v0": v0 / CONVERT_FACTOR,
                "v1": v1 / CONVERT_FACTOR,
                "dV0": dV0 / CONVERT_FACTOR,
                "dV1": dV1 / CONVERT_FACTOR}
