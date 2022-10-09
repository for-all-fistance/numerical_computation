# ordinary least squares
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

_x = np.array([19, 25, 31, 38, 44])
_y = np.array([19.0, 32.3, 49.0, 73.3, 97.8])


def fun(x, a, b):
    return a + b * x ** 2


popt, pcov = curve_fit(fun, _x, _y)
# args = np.polyfit(_x, _y, 2)  # 用最小二乘法找到最佳的一组系数
# g = np.poly1d(popt)  # 用这组系数生成方程g(x)
# loss = np.sum(np.square(fun(_x, popt[0], popt[1]) - _y))  # 计算i次多项式拟合的误差
print(popt, "\n", pcov)
