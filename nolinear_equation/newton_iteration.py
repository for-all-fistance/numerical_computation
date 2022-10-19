# newton_iteration

def f(x):
    return pow(x, 3) - 2 * pow(x, 2) - 4 * x - 7


def f_(x):
    return 3 * pow(x, 2) - 4 * x - 4


def g(x):
    return x - f(x) / f_(x)


epsilon = 1e-5
seed = 4

if __name__ == "__main__":
    while abs(g(seed) - seed) >= epsilon:
        print(seed)
        seed = g(seed)
    print("the answer is ", g(seed))
