import numpy as np


def upperTriangularMatrixWithMainDiagonalAtZero(matrixNxN):
    UpperTriangleMatrix = np.triu(matrixNxN, 1)
    return UpperTriangleMatrix + UpperTriangleMatrix.T - np.diag(np.diag(UpperTriangleMatrix))


def getNearestNeighbor(adjacencyMatrix, hamiltonianCycle, currentRow):
    flag = True
    count = 0
    nodeToCompare = None
    while flag:
        nodeToCompare = np.where(adjacencyMatrix[currentRow] == np.sort(adjacencyMatrix[currentRow])[count])[0][0]
        if nodeToCompare in hamiltonianCycle:
            count += 1
        elif hamiltonianCycle[0] == nodeToCompare:
            count += 1
        else:
            flag = False
    return nodeToCompare


def nearestNeighbor(adjacencyMatrix):
    for indexRow, row in enumerate(adjacencyMatrix):
        currentRow = indexRow
        hamiltonianCycle = [np.where(adjacencyMatrix[currentRow] == [row[currentRow]])[0][0]]
        for node in range(len(adjacencyMatrix) - 1):
            currentRow = getNearestNeighbor(adjacencyMatrix, hamiltonianCycle, currentRow)
            hamiltonianCycle.append(currentRow)
        hamiltonianCycle.append(hamiltonianCycle[0])
        print(*hamiltonianCycle, sep="-")


def runNearestNeighborAlgorithm():
    matrix7x7 = np.array(
        [[0, 10, 8, 5, 7, 20, 15],
         [0, 0, 12, 16, 9, 13, 4],
         [0, 0, 0, 18, 22, 30, 25],
         [0, 0, 0, 0, 13, 14, 24],
         [0, 0, 0, 0, 0, 32, 36],
         [0, 0, 0, 0, 0, 0, 50],
         [0, 0, 0, 0, 0, 0, 0]]
    )
    adjacencyMatrix = upperTriangularMatrixWithMainDiagonalAtZero(matrix7x7)
    print(str(adjacencyMatrix)+"\n")
    nearestNeighbor(adjacencyMatrix)


runNearestNeighborAlgorithm()
