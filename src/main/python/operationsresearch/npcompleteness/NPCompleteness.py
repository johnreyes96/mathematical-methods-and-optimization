import numpy as np


def upperTriangularMatrixWithMainDiagonalAtZero(adjacencyMatrix):
    return np.triu(adjacencyMatrix, 1)


def bruteForceSearch(adjacencyMatrix):
    return adjacencyMatrix


a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = upperTriangularMatrixWithMainDiagonalAtZero(a)
print(b)

for i in b:
    for j in i:
        if j > 0:
            print(j)
