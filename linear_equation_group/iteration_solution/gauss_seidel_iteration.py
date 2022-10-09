# gauss seidel iteration
import numpy as np
import sys

M = np.array([[4, 3, 0],
              [3, 4, -1],
              [0, -1, 4]], dtype=np.float32)

A, B = M.shape

b = np.array([[24],
              [30],
              [-24]])

epsilon = 0.5e-3

U = np.zeros((A, B), dtype=np.float32)
L = np.zeros((A, B), dtype=np.float32)
D = np.zeros((A, B), dtype=np.float32)

# initialize
for i in range(0, A):
    for j in range(0, B):
        if i > j:
            L[i][j] = M[i][j]
        elif i < j:
            U[i][j] = M[i][j]
    D[i][i] = M[i][i]
G = -np.matmul(np.linalg.inv(D+L), U)
Fg = np.matmul(np.linalg.inv(D+L), b)
print("L: ", L, "\nU: ", U, "\nD: ", D, "\nG: ", G, "\nFg: ", Fg)


# convergent or not?
eigenvalue = np.linalg.eigvals(G)
print("eigenvalues: ", eigenvalue)
for i in range(0, A):
    if abs(eigenvalue[i]) >= 1:
        sys.exit()


# calc the infinite norm of vector xk+1-xk
def inf_norm(x):
    m = 0
    a, b = x.shape
    for i in range(0, a):
        if abs(x[i][0]) >= m:
            m = abs(x[i][0])
    return m


x0 = np.zeros((A, 1), dtype=np.float32)
x1 = np.matmul(G, x0) + Fg
time = 1
while inf_norm(x1 - x0) >= epsilon:
    x0 = x1
    x1 = np.matmul(G, x0) + Fg
    time += 1
    print(x1)
print(time, "generation")
print("x = ", x1)
