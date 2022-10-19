# jacobi_iteration
import numpy as np
import sys

M = np.array([[1, -2, 2],
              [-1, 1, -1],
              [-2, -2, 1]], dtype=np.float32)

b = np.array([[-12],
              [0],
              [10]])

epsilon = 1e-3


# calc the infinite norm of vector xk+1-xk
def inf_norm(x):
    m = 0
    a, b = x.shape
    for i in range(0, a):
        if abs(x[i][0]) >= m:
            m = abs(x[i][0])
    return m


if __name__ == "__main__":
    A, B = M.shape
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
    J = np.matmul(-np.linalg.inv(D), (L + U))
    Fj = np.matmul(np.linalg.inv(D), b)
    print("L: ", L, "\nU: ", U, "\nD: ", D, "\nJ: ", J, "\nFj: ", Fj)

    # convergent or not?
    eigenvalue = np.linalg.eigvals(J)
    print("eigenvalues: ", eigenvalue)
    for i in range(0, A):
        if abs(eigenvalue[i]) >= 1:
            sys.exit()

    x0 = np.zeros((A, 1), dtype=np.float32)
    x1 = np.matmul(J, x0) + Fj
    while inf_norm(x1 - x0) >= epsilon:
        x0 = x1
        x1 = np.matmul(J, x0) + Fj
        print(x1)
    print("x = ", x1)
