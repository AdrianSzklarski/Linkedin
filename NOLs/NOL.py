"""     Adrian SZKLARSKI, 06.2022r,
        An unidentified flying :
We will determine the coefficient of resistance of the NOL to its chord, for a given velocity Ma
    Returns:      Ma - Mach
                  cx'- coefficient of resistance
    Parameters:   AB - flight distance
                  t  - flight time
                  L  - length of the NOL height
                  T  - air temperature
"""
import math


class NOL:

    def __init__(self, AB, t, T, L):
        self.AB = AB
        self.t = t
        self.T = T
        self.L = L

    def Mach(self):
        tab_of_speed = [306.5, 312.9, 319.3, 325.6, 331.8, 337.8, 340.3, 343.8, 349.6, 355.3]
        indx = tab_of_temp.index(self.T)
        ind = tab_of_speed.pop(indx)
        self.mach = (self.AB / self.t) / ind
        return round(self.mach, 2)

    def cxP(self):
        h_down = 0.01 * self.L
        self.h_up = 2 * h_down
        a = h_down / self.L
        self.cx_prim = 40 * ((math.pow(a, 2)) / math.sqrt(math.pow(nol.Mach(), 2) - 1))
        return round(self.cx_prim, 8), self.h_up

    def __str__(self):
        return f'{self.mach}, {self.cx_prim}'


if __name__ == '__main__':
    tab_of_temp = [-40, -30, -20, -10, 0, 10, 20, 30, 40]
    while True:
        try:
            AB = float(input('Enter flight distance [m]: '))
            t = float(input('Enter flight time [s]: '))
            L = float(input('Specify the length of the NOL height [m]: '))
            T = int(input('choose the air temperature from the list: \n\
            -40, -30, -20, -10, 0, 10, 20, 30, 40: '))
            a = [element for element in tab_of_temp if T == element]
            if a:
                nol = NOL(AB, t, T, L)
                print("Mach:", nol.Mach(), " cx': ", nol.cxP()[0])
                break
        except ValueError:
            print('You have entered a value from outside the table, try again')
