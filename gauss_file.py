#!/usr/local/bin/python3
import numpy as np

A = np.loadtext("testmatrix.txt", delimiter= '\s+', dtype=int)
print('Initial matrix is:', A)

num_rows = len(A)
num_cols = len(A[0])

if num_rows == num_cols:
    for k in range(0, 2):
        for i in range(k+1, 3):
            pivot = A[i][k]/A[k][k]
            for j in range(0, 4):
                A[i][j] = A[i][j] - pivot * A[k][j]

    print("Reduced matrix is: ", A)
else:
    print('Not a squre matrix')
