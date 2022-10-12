# newton integration
import numpy as np


def trapezoid(f, a, b):  # trapezoid(n=1)
    return (b - a) * (f(b) + f(a)) / 2


def simpson(f, a, b):  # simpson(n=2)
    t = (a + b) / 2
    val = (b - a) * (f(a) + 4 * f(t) + f(b)) / 6
    return val


def compositeInt(f, a, b, n, mode='trapezoid'):
    h = (b - a) / n
    val = 0
    eps = 1e-10
    if mode == 'trapezoid':
        for k in range(n):
            xk = a + k * h + eps
            xk1 = xk + h
            val += trapezoid(f, xk, xk1)
    if mode == 'simpson':
        for k in range(n):
            xk = a + k * h + eps
            xk1 = xk + h
            val += simpson(f, xk, xk1)
    return val


if __name__ == '__main__':
    a = 0
    b = 1
    f = lambda x: np.sin(x) / x
    print('====== trapezoid: newton-cotes(1st-order) ======')
    val = compositeInt(f, a, b, 8)
    print('trapezoid: %.7f' % (val))
    print('====== simpson: newton-cotes(2nd-order) ======')
    val = compositeInt(f, a, b, 4, 'simpson')
    print('simpson: %.7f' % (val))



