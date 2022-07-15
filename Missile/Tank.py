"""   Adrian Szklarski 07.2022  """

import math


class Prom:

    def __init__(self, data):
        self.data = data


    def stresses(self):
        Simga_r = (math.pow(self.data[0], 2) / (math.pow(self.data[1], 2) - math.pow(self.data[0], 2))) * (
                1 - (math.pow(self.data[1], 2) / math.pow(self.data[0], 2)))
        Simga_Theta = (math.pow(self.data[0], 2) / (math.pow(self.data[1], 2) - math.pow(self.data[0], 2))) * (
                1 + (math.pow(self.data[1], 2) / math.pow(self.data[0], 2)))
        Simga_z = (math.pow(self.data[0], 2) / (math.pow(self.data[1], 2) - math.pow(self.data[0], 2)))
        Simga_derated = round(math.sqrt(0.5 * self.data[0]), 2)

        if Simga_derated < data[4]:
            p = self.data[4] / Simga_derated
            self.Simga_r = round(Simga_r * p, 2)
            self.Simga_Theta = round(Simga_Theta * p, 2)
            self.Simga_z = round(Simga_z * p, 2)
        else:
            exit(0)
            return f'The condition for reduced stresses is not met'
        return self.Simga_r, self.Simga_Theta, self.Simga_z

    def deformations(self):
        self.E_r = round((1 / self.data[2]) * (self.Simga_r - (self.data[3] * self.Simga_Theta)) - (
                self.data[3] * self.Simga_z / self.data[2]), 5)
        self.E_Theta = round((1 / self.data[2]) * (self.Simga_Theta - (self.data[3] * self.Simga_r)) - (
                self.data[3] * self.Simga_z / self.data[2]), 5)
        C2 = round((self.Simga_r / self.data[2]) * (1 + self.data[3]) * (
                (math.pow(self.data[0], 2) * math.pow(self.data[1], 2)) / (
                math.pow(self.data[0], 2) - math.pow(self.data[1], 2))) * 100, 2)
        C1 = round((C2 / math.pow(self.data[1] * 10, 2)) * ((1 - self.data[3]) / (1 + self.data[3])), 5)
        return C1, C2

    def radius_change(self):
        C1, C2 = self.deformations()
        self.delta_ra = round((C1 * self.data[0] * 10) + C2 / (self.data[0] * 10), 2)
        self.delta_rb = round((C1 * self.data[1] * 10) + C2 / (self.data[1] * 10), 2)
        return self.delta_ra, self.delta_rb

    def __str__(self):
        return f'Changing the radius: ra = {self.delta_ra} [mm],  rb = {self.delta_rb} [mm]'


if __name__ == '__main__':
    data = [
        'a=', 67.0, 'cm',
        'b=', 77.0, 'cm',
        'E=', 2E5, 'MPa',
        'n=', 0.3,
        'N=', 100.0, 'MPa'
    ]
    hear = Prom(list(filter(lambda x: type(x) is float, data)))
    # hear.stresses(), hear.deformations(), hear.radius_change()
    # print(hear)
    print(hear.radius_change())
