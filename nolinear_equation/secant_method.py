# speed_up_secant_method
import math

def f(x):
    return x - math.exp(-x)



def g(x0, x1):
    return x1 - (x1 - x0)*f(x1)/(f(x1) - f(x0))


epsilon = 1e-5
x0 = 0.5
x1 = 0.6
while abs(x1 - x0) >= epsilon:
    x2 = g(x0, x1)
    x0 = x1
    x1 = x2
    print(x0)
print("the answer is ", x1)
