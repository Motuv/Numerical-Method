import math
import numpy as np

coord_x = [-10, -1.23, 9.87, -2]
coord_y = [-4, 12.5, 10.13, 0]

weight = [1, 1]
point = [-0.5773502692, 0.5773502692]
fun_shape = np.zeros((2, 2, 4))
deriv_ksi = np.zeros((2, 4))
deriv_ni = np.zeros((2, 4))
fun_detj = np.zeros((2, 2))

for i in range(0, 2):
    for j in range(0, 2):
        fun_shape[i][j][0] = 0.25 * (1 - point[i]) * (1 - point[j])
        fun_shape[i][j][1] = 0.25 * (1 + point[i]) * (1 - point[j])
        fun_shape[i][j][2] = 0.25 * (1 + point[i]) * (1 + point[j])
        fun_shape[i][j][3] = 0.25 * (1 - point[i]) * (1 + point[j])

        deriv_ksi[j][0] = -0.25 * (1 - point[j])
        deriv_ksi[j][1] = 0.25 * (1 - point[j])
        deriv_ksi[j][2] = 0.25 * (1 + point[j])
        deriv_ksi[j][3] = -0.25 * (1 + point[j])
        deriv_ni[i][0] = -0.25 * (1 - point[i])
        deriv_ni[i][1] = -0.25 * (1 + point[i])
        deriv_ni[i][2] = 0.25 * (1 + point[i])
        deriv_ni[i][3] = 0.25 * (1 - point[i])

for i in range(0, 2):
    for j in range(0, 2):
        dxdksi = deriv_ksi[j][0] * coord_x[0] + deriv_ksi[j][1] * coord_x[1] + deriv_ksi[j][2] * coord_x[2] + \
                 deriv_ksi[j][3] * coord_x[3]
        dydksi = deriv_ksi[j][0] * coord_y[0] + deriv_ksi[j][1] * coord_y[1] + deriv_ksi[j][2] * coord_y[2] + \
                 deriv_ksi[j][3] * coord_y[3]
        dxdni = deriv_ni[j][0] * coord_x[0] + deriv_ni[j][1] * coord_x[1] + deriv_ni[j][2] * coord_x[2] + \
                deriv_ni[j][3] * coord_x[3]
        dydni = deriv_ni[j][0] * coord_y[0] + deriv_ni[j][1] * coord_y[1] + deriv_ni[j][2] * coord_y[2] + \
                deriv_ni[j][3] * coord_y[3]
        fun_detj[i][j] = dxdksi * dydni - dxdni * dydksi

area = 0.0
for i in range(0, 2):
    for j in range(0, 2):
        area += math.fabs(fun_detj[i][j]) * weight[i] * weight[j]

print("Area: %.5f" % area)
