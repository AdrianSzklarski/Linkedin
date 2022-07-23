import math


def tank(a, b, p_max):
    """ Calculation of stresses in the barrel of the Abrams M1A2 tank.
        Input data pressure and diameters, output data - stresses. """
    # r = a
    sigma_r_a = round((p_max*math.pow(a, 2)/(math.pow(b, 2)-math.pow(a, 2)))*(1-math.pow(b, 2)/math.pow(a, 2)), 1)
    sigma_t_a = round((p_max*math.pow(a, 2)/(math.pow(b, 2)-math.pow(a, 2)))*(1+math.pow(b, 2)/math.pow(a, 2)), 1)

    # r = b
    sigma_r_b = round((p_max*math.pow(a, 2)/(math.pow(b, 2)-math.pow(a, 2)))*(1-math.pow(b, 2)/math.pow(b, 2)), 1)
    sigma_t_b = round((p_max*math.pow(a, 2)/(math.pow(b, 2)-math.pow(a, 2)))*(1+math.pow(b, 2)/math.pow(b, 2)), 1)

    return sigma_r_a, sigma_t_a, sigma_r_b, sigma_t_b

hear = tank(120, 160, 520)
print(' sigma_r_a: ', hear[0], 'MPa\n', 'sigma_t_a: ', hear[1], 'MPa\n', 'sigma_r_b: ', hear[2], 'MPa\n', 'sigma_t_b: ', hear[3], 'MPa')