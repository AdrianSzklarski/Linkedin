"""     Adrian SZKLARSKI, 06.2022r,
        A game of guessing numbers:
Calculation of aerodynamic coefficients for a rectangular airfoil.
    Returns:      elements of mechanics of flight
    Parameters:   span B = 12m, chord = 1.5 and aspect ratio = 5
    Error:        ValueError or NameError
"""

import matplotlib.pyplot as plt
from scipy.interpolate import splrep, splev
import numpy as np
import math

alpha = [-4, 0, 4, 8, 12, 16, 20]
Cz = [-0.05, 0.24, 0.51, 0.78, 1.05, 1.3, 1.4]
Cx = [0.015, 0.017, 0.03, 0.055, 0.087, 0.198, 0.202]

class Aero:


    def __init__(self, alpha, Cz, Cx):
        self.alpha = alpha
        self.Cx = Cx
        self.Cz = Cz

    # calculate cz/cx
    def cz_cx(self):
        cz = np.array(self.Cz)
        cx = np.array(self.Cx)
        self.div = (cz / cx).round(5)
        return self.div

    # converting degrees to radians
    def rad(self):
        self.deg_rad = np.array(self.alpha) * (math.pi / 180)
        return self.deg_rad.round(5)

    # angle change
    def delta_alpha(self):
        self.da = -0.026 * np.array(self.Cz)
        return self.da.round(5)

    # cz^2
    def czarecz(self):
        self.Cz2 = np.array(self.Cz) * np.array(self.Cz)
        return self.Cz2.round(5)

    # cxi change
    def deltaCxi(self):
        self.Cxi = (-0.0235 * np.array(self.Cz) * np.array(self.Cz))
        return self.Cxi.round(4)

    # cx for aspect ratio = 8
    def Cx8(self):
        self.Cx8 = np.array(self.Cx)
        return self.Cx8.round(5)

    # cz/cx for aspect ratio = 8
    def CzCx8(self):
        self.CzCx = (np.array(self.Cz) / np.array(self.Cx))
        return self.CzCx.round(5)

    def __str__(self):
        return f'{self.div}, {self.deg_rad}, {self.da}, \
                 {self.Cz2}, {self.Cxi}, {self.Cx8}, {self.CzCx8}'


if __name__ == '__main__':
    a = Aero(alpha, Cz, Cx)
    print(' Cz/Cx(5)   : ', a.cz_cx(), '\n alpha[rad] : ', a.rad(), '\n delta_alpha: ', a.delta_alpha(), '\n'
                                                                                                         ' Cz^2       : ',
          a.czarecz(), '\n delta Cxi  : ', a.deltaCxi(), '\n Cx(8)      : ', Cx, '\n'
                
                                                                                     ' Cz/Cx(8)   : ', a.CzCx8())

    # plot Cz = f(alpha)
    plt.title('Cz = f(alpha)', fontsize=16)
    bspl = splrep(alpha, Cz, s=5)
    bspl_y = splev(alpha, bspl)
    plt.plot(alpha, Cz)
    plt.plot(alpha, bspl_y)
    plt.xlabel('alpha', fontsize=16)
    plt.ylabel('Cz', fontsize=16)
    plt.grid(True)
    plt.show()

    # plot Cx = f(alpha)
    plt.title('Cx= f(alpha)', fontsize=16)
    bspl = splrep(alpha, Cx, s=5)
    bspl_y = splev(alpha, bspl)
    plt.plot(alpha, Cx)
    plt.plot(alpha, bspl_y)
    plt.xlabel('alpha', fontsize=16)
    plt.ylabel('Cx', fontsize=16)
    plt.grid(True)
    plt.show()

    # plot Cz = f(Cx)
    plt.title('Cz= f(Cx)', fontsize=16)
    bspl = splrep(Cx, Cz, s=5)
    bspl_y = splev(Cx, bspl)
    plt.plot(Cx, Cz)
    plt.plot(Cx, bspl_y)
    plt.xlabel('Cx', fontsize=16)
    plt.ylabel('Cz', fontsize=16)
    plt.grid(True)
    plt.show()

    # plot Cz/Cx = f(alpha)
    plt.title('Cz/Cx= f(alpha)', fontsize=16)
    bspl = splrep(alpha, a.CzCx8(), s=3)
    bspl_y = splev(alpha, bspl)
    plt.plot(alpha, a.CzCx8())
    plt.plot(alpha, bspl_y)
    plt.xlabel('alpha', fontsize=16)
    plt.ylabel('Cz/Cx', fontsize=16)
    plt.grid(True)
    plt.show()
