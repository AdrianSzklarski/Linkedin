''' Adrian Szklarski 07.2022'''

print('Describe parameters of Saturn V:')
print('Mass fuel of I stage = 2279 T')
print('Mass fuel of II stage = 481 T')
print('Mass fuel of III stage = 107 T')
print('Mass empty of I stage = 130.4 T')
print('Mass empty of II stage = 36.5 T')
print('Mass empty of III stage = 11.3 T')
print('Rocket engine thrust of I stage = 34.02 MN')
print('Rocket engine thrust of II stage = 5 MN')
print('Rocket engine thrust of III stage = 1 MN')
print('Range flight of I stage = 67 km \n')


class Missile:

    def __init__(self, LkI, bI, MI, mu, kI, caI):
        self.LkI = LkI
        self.bI = bI
        self.MI = MI
        self.mu = mu
        self.kI = kI
        self.caI = caI

    def liqid(self):
        self.calc = ((1 - self.MI - (self.bI / self.LkI)) - (1 + self.kI) * self.caI)
        self.mI = self.mu / self.calc
        return round(self.mI)

    def solid(self):
        pass

    def __str__(self):
        return f'{self.mI}'


if __name__ == '__main__':
    data = [2077, 456.1, 107.8, 137, 40.1, 15.2, 67]
    sum_mass_fuel = data[0] + data[1] + data[2]
    sum_mass_empty = data[3] + data[4] + data[5]
    sum_mass = sum_mass_fuel + sum_mass_empty
    mu = 118  # T

    MI = data[4] / sum_mass
    bI = data[0] / sum_mass
    LkI = data[6]

    kI = 1.477
    caI = 0.37

    hear = Missile(LkI, bI, MI, mu, kI, caI)
    print('Mass of stage I: ', hear.liqid() * 1000, 'kg')
