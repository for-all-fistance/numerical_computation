# LU_decomposition
import numpy as np
import sys

M = np.array([[5., 7., 9., 10., 1.],
              [6., 8., 20., 9., 1.],
              [7., 10., 8., 7., 1.],
              [5., 7., 6., 5., 1.]])

if __name__ == "__main__":
    A, B = M.shape
    rank = np.linalg.matrix_rank(M)
    if rank < A and rank < B:
        print("the rank is ", rank, " matrix do not have unique solution")
        sys.exit()
    else:
        print("the rank is ", rank)
    for i in range(1, A):
        for j in range(0, B - 1):
            if i <= j:
                s = 0
                for k in range(0, i):
                    s += M[i, k] * M[k, j]
                M[i, j] -= s  # uij=aij-∑lik*ukj
            elif M[j, j] != 0:
                s = 0
                for k in range(0, j):
                    s += M[i, k] * M[k, j]
                M[i, j] = (M[i, j] - s) / M[j, j]  # uij=(aij-∑lik*ukj)/ujj
    np.set_printoptions(precision=3, suppress=True)
    print(M)
