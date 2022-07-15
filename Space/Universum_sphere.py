import math


def sphere(p_alpha, Fi_alpha, Fi_alpha_new):
    L = round((math.pi / 8) * (p_alpha / Fi_alpha) * (math.pow(Fi_alpha_new, 4) - math.pow(Fi_alpha, 4)) * 1000, 2) / 1E120
    DU = round((5 / 2) * (math.pi / 6) * p_alpha * math.pow(Fi_alpha, 3) * (math.pow((Fi_alpha_new / Fi_alpha), 4) - 1) * 1000, 2) / 1E120
    Q = DU + L
    return L, Q


print(' Thermodynamic work: ',  sphere(8.8E24, 8.8E26, 9.2E29)[0], '[kJ]\n', 'Thermodynamic heat: ', sphere(8.8E24, 8.8E26, 9.2E29)[1],
      '[kJ]\n')
