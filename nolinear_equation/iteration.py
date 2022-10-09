# iteration
import math

def f(x):
    return pow(x+1, 1/3)


epsilon = 1e-5


seed = 1.5
while seed - f(seed) >= epsilon:
    seed = f(seed)
    print(seed)
print("the answer is ", seed)