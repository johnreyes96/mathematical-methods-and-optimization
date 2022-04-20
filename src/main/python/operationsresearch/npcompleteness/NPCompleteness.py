from builtins import enumerate
from math import factorial

import numpy as np


def upperTriangularMatrixWithMainDiagonalAtZero(adjacencyMatrix):
    return np.triu(adjacencyMatrix, 1)


def bruteForceSearch(adjacencyMatrix):
    nodesCount = len(adjacencyMatrix)
    initialNode = None
    previousHamiltonianPath = None
    hamiltonianPath = None
    weight = None
    indexMatrix = None
    hamiltonianCycles = None
    print(factorial(nodesCount))
    for indexRow, row in enumerate(adjacencyMatrix):
        initialNode = indexRow
        for indexColumn, column in enumerate(row):
            if column == 0:
                hamiltonianPath = str(indexColumn)
                weight = 0
            elif column > 0:
                if previousHamiltonianPath is None:
                    hamiltonianPath += "-" + str(indexColumn)
                    weight += adjacencyMatrix[indexColumn-1, indexColumn]
                    if indexColumn == 3:
                        hamiltonianPath += "-" + str(initialNode)
                        weight += adjacencyMatrix[indexColumn, initialNode]
                # elif (nodesCount - len(indexMatrix)) < 3:
                #     hamiltonianPath += "-" + str(indexColumn)
                #     indexMatrix = indexColumn
                #     weight += column  # adjacencyMatrix[indexRow, indexColumn]
                # print(column)
        if previousHamiltonianPath is None or previousHamiltonianPath < 2:
            print("Primer ciclo hamiltoniano: " + str(hamiltonianPath))
            print("Peso del primer ciclo hamiltoniano: " + str(weight))
        previousHamiltonianPath = indexRow + 1
    return hamiltonianCycles


# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a = np.array([[0, 5, 9, 7], [0, 0, 4, 10], [0, 0, 0, 12], [7, 0, 0, 0]])
b = upperTriangularMatrixWithMainDiagonalAtZero(a)
print(a)
print(bruteForceSearch(a))
