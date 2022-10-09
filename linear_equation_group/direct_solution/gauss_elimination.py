# gauss_elimination
import numpy as np
import sys


# matrix to solve
M = np.array([[31., -13., 0., 0., 0., -10., 0., 0., 0., -15.],
             [-13., 35., -9., 0., -11., 0., 0., 0., 0., 27.],
             [0., -9., 31., -10., 0., 0., 0., 0., 0., -23.],
             [0., 0., -10., 79., -30., 0., 0., 0., -9., 0.],
             [0., 0., 0., -30., 57., -7., 0., -5., 0., -20.],
             [0., 0., 0., 0., -7., 47., -30., 0., 0., 12.],
             [0., 0., 0., 0., 0., -30., 41., 0., 0., -7.],
              [0., 0., 0., 0., -5., 0., 0., 27., -2., 7.],
              [0., 0., 0., -9., 0., 0., 0., -2., 29., 10.]])

A, B = M.shape
rank = np.linalg.matrix_rank(M)
if rank < A and rank < B:
    print("the rank is ", rank, " matrix do not have unique solution")
    sys.exit()
else:
    print("the rank is ", rank)


def SPE(mat, n):  # search for pivot element
    max = 0
    max_p = 0
    for i in range(n, A):
        if abs(mat[i, n]) > max:
            max_p = i
            max = mat[n, i]
    if max == 0:
        print("no pivot element!")
        sys.exit()
    mat[[max_p, n], :] = mat[[n, max_p], :]


def trans_R(mat, a, b, m):  # mat[][a]+=m*mat[][b]    transformation in row
    for i in range(0, B):
        mat[a, i] += m * mat[b, i]


b = M[0:A, B - 1:B]
a = M[0:B - 1, 0:B - 1]
print("correct answer is: \n", np.linalg.solve(a, b), "\n")

# elimination
for i in range(0, A):
    SPE(M, i)
    for j in range(i + 1, A):
        trans_R(M, j, i, -M[j, i] / M[i, i])

# back-substitution
for i in range(0, B - 1):
    for j in range(0, A - i - 1):
        trans_R(M, j, A - i - 1, -M[j, A - i - 1] / M[A - i - 1, A - i - 1])
    M[A - i - 1, B - 1] /= M[A - i - 1, A - i - 1]
print("my answer is: \n", M[0:A, B - 1:B])
