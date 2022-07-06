'''  Adrian Szklarski 07.2020

Three unidentified flying objects were seen in the sky.
The objects were cube-shaped. After a few moments they disappeared.
The secret service recorded a lot of data but a certain group of hackers
managed to steal some information and make it public. The most important
data are summarized in a table. Based on the data, calculate t
he size of the objects.

'''

import math


class Data:

    def __init__(self):
        self.nol_ep_int = 0

    def data(self):
        nol = ['NOL_1', 3.5, 'NOL_2', 2.0, 'NOL_3', 1.15]
        self.nol_ep_int = list(map(lambda x: x * 2, list(filter(lambda x: type(x) is float, nol))))
        return self.nol_ep_int


class Calc(Data):
    def __init__(self, ep, pt):
        super().__init__()
        self.cube = None
        self.ep = ep
        self.pt = pt

    def nols(self):
        self.tab = []
        cube = (round(math.pow((self.ep[i] / (self.pt[i] * clas.data()[i] * 1000)), 1 / 3), 2) for i in range(0, 3))
        for i in range(0, 3):
            self.tab.append(next(cube))
        return self.tab

    def __str__(self):
        return f'{self.cube}'


if __name__ == '__main__':
    clas = Data()
    hear = Calc([4800, 7800, 8950], [200, 365, 414])
    print('NOL_1 Length of side', hear.nols()[0], '[m]', 'so the dimensions are: ', hear.nols()[0], 'x', hear.nols()[0], 'x', hear.nols()[0], '[m]\n'
          'NOL_2 Length of side', hear.nols()[1], '[m]', 'so the dimensions are: ', hear.nols()[1], 'x', hear.nols()[1], 'x', hear.nols()[1], '[m]\n'
          'NOL_3 Length of side', hear.nols()[2], '[m]', 'so the dimensions are: ', hear.nols()[2], 'x', hear.nols()[2], 'x', hear.nols()[2], '[m]')
