def f(x, y):
    return 3 * y / (1 + x)


h = 0.2
y0 = 1
begin = 0
end = 1


if __name__ == "__main__":
    yi = [y0]
    for i in range(int((end - begin) / h)):
        xi = i * h +begin
        k1 = f(xi, yi[i])
        k2 = f(xi + h / 2, yi[i] + h * k1 / 2)
        k3 = f(xi + h / 2, yi[i] + h * k2 / 2)
        k4 = f(xi + h, yi[i] + h * k3)
        y = yi[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        yi.append(y)
    print(yi)
