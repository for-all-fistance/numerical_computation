# lagrange_interpolation
import numpy as np
import math


# basis function
def l(x, k, num):
    m = 1
    n = num.shape
    for i in range(0, k):
        m *= x - num[i]
        m /= num[k] - num[i]
    for j in range(k+1, n[0]):
        m *= x - num[j]
        m /= num[k] - num[j]
    return m


def L(x, y, num):
    s = 0
    n = num.shape
    for i in range(0, n[0]):
        s += l(x, i, num) * y[i]
    return s


_x = np.array([-1, 0, 1])
_y = np.array([0.3679, 1.0000, 2.7182])
x = float(input())
print(L(x, _y, _x))
