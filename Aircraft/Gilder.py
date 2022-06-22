"""     Adrian SZKLARSKI, 06.2022r,
        A game of guessing numbers:
A glider takes off from the airport in April. The glider is towed on a rope by a
small aircraft during takeoff. Rope in the initial length had a heat capacity of.
The tensile force is given by the equation . The rope length at the start is.
The ambient temperature is. After which, when unhooked at altitude it turned
out that the glider had broken down and had to land. Glider's rate of descent .
During the flight, however, it encountered an "air current stack" with an
ascending vertical velocity and was in it for 6min.
    Returns:      - the temperature of the rope under adiabatic stretching;
                  - after what time will the glider reach the ground?
    Parameters:   k, L, Ls, C, T, h, w, v, min
"""
import math


class glider:

    def __init__(self, k, L, Ls, C, T, h, w, v, min):
        self.k = k
        self.L = L
        self.Ls = Ls
        self.C = C
        self.T = T
        self.h = h
        self.w = w
        self.v = v
        self.min = min

    def line(self):
        T2_1 = (self.k / (self.C * self.L))
        T2_2 = (math.pow(self.Ls, 2) / (2 * self.L)) + (math.pow(self.L, 2) / self.Ls)
        T2_3 = (math.pow(self.L, 2) / (2 * self.L)) + (math.pow(self.L, 2) / self.L)
        self.T2 = (self.T + 273.15) * math.exp(T2_1 * (T2_2 + T2_3))
        return self.T2

    def time(self):
        self.t0 = (((self.v * (60 * self.min)) + self.h) / self.w) // 60
        self.t1 = (((self.v * (60 * self.min)) + self.h) / self.w) % 60
        return int(self.t0), round(self.t1)

    def __str__(self):
        return f'{self.T2}, {self.t0}, {self.t1}'


if __name__ == '__main__':
    k = 0.02  # N/K
    L = 15  # m
    Ls = 32  # m
    C = 1.2  # J/mK
    T = 17  # oC
    h = 2000  # m
    w = 0.85  # m/s
    v = 1.2  # m/s
    min = 6  # min
    hear = glider(k, L, Ls, C, T, h, w, v, min)
    print('Line temperature in adiabatic tension: ', round(hear.line(), 2), 'K\n' \
          'flight time to Earth: ', hear.time()[0], 'min', hear.time()[1], 'sek')
