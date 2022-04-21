from builtins import len

import numpy as np


def upperTriangularMatrixWithMainDiagonalAtZero(adjacencyMatrix):
    return np.triu(adjacencyMatrix, 1)


def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


num = 5
print("Factorial de", num, "es", factorial(num))


def bruteForceSearch(adjacencyMatrix, count=0):
    for index in range(adjacencyMatrix):
        if adjacencyMatrix == 1 and index == 0:
            count += 1
            # print(str(count)+"-"+str(adjacencyMatrix)+"-"+str(index))
        count = bruteForceSearch(adjacencyMatrix - 1, count)
    return count


# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a = np.array([[0, 5, 9, 7], [0, 0, 4, 10], [0, 0, 0, 12], [7, 0, 0, 0]])
b = upperTriangularMatrixWithMainDiagonalAtZero(a)
print(a)
print("cantidad de ciclos hamiltonianos: " + str(bruteForceSearch(len(a))))
