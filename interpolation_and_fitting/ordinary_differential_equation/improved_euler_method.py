def f(x, y):
    return x ** 2 - 2 * y


h = 0.1
y0 = 1
begin = 0
end = 0.5


if __name__ == "__main__":
    yi = [y0]
    for i in range(int((end - begin) / h)):
        xi = h * i + begin
        k1 = f(xi, yi[i])
        k2 = f(xi + h, yi[i] + h * k1)
        y = yi[i] + h / 2 * (k1 + k2)
        yi.append(y)
    print(yi)
