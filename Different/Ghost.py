'''   Szklarski Adrian 06.2022

How much must the poor ghost evaporate and how much heat must it supply
to the castle room so that by 1 a.m. when it disappears the air returns
to its initial state i.e. temperature tp = 20 °C and relative humidity
φp = 70%. Outside air conditions: t0 = 0 oC and φ0 = 80%.

    Returns:      - Amount of evaporated from ghost water;
                  - Amount of additional heat input;
                  - The entire process is characterized by simple directionality.

    Parameters:   - Data of task: V, %, tp, fi_w, t0, fi_z;
                  - Chart data: xw, iw, x2, iz;
                  - Point M: tM, fiM, fi.

'''
# data of task: V, %, tp, fi_w, t0, fi_z
data_of_task = [60, 25, 20, 70, 0, 80]
# chart data: xw, iw, x2, iz
data = [10.4, 47, 3.1, 8]
# point M: tM, fiM, fi
pointM = [15, 0.87, 1.21]


def ghost(Data, Data_of_task):
    sum_air = (Data_of_task[1] + (100 - Data_of_task[1]))
    iM = (Data_of_task[1] * Data[3] + ((100 - Data_of_task[1]) * Data[1])) / sum_air
    xM = (Data_of_task[1] * Data[2] + ((100 - Data_of_task[1]) * Data[0])) / sum_air
    m_room = Data_of_task[0] * pointM[2]
    h2o = round(m_room * (Data[0] - xM), 2)
    Qg = round(m_room * (Data[1] - iM), 2)
    charakteristic = round((1000 * Qg) / h2o, 2)
    return h2o, Qg, charakteristic


hear = ghost(data, data_of_task)
print('       Amount of evaporated from ghost water: ', hear[0], '[g]', '\n\
       Amount of additional heat input: ', hear[1], '[kJ/h]', '\n\
       The entire process is characterized by simple directionality: ', hear[2], '[kJ/kg]')
