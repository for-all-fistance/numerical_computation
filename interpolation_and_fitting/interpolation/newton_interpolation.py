# newton interpolation
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from functools import reduce

x = np.array([-2, 0, 1, 3],)
y = np.array([1, -1, 2, 4])
f1 = interpolate.interp1d(x, y, kind='linear')
print(f1(0))

