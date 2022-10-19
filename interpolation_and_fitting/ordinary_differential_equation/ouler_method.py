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
        y = yi[i] + h * f(xi, yi[i])
        yi.append(y)
    print(yi)
