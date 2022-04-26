import numpy as np


def upperTriangularMatrixWithMainDiagonalAtZero(matrixNxN):
    UpperTriangleMatrix = np.triu(matrixNxN, 1)
    return UpperTriangleMatrix + UpperTriangleMatrix.T - np.diag(np.diag(UpperTriangleMatrix))


def NearestNeighbor(nodesCount):
    for index in range(nodesCount):
        print(index)


def runNearestNeighborAlgorithm():
    print(str(adjacencyMatrix)+"\n")
    NearestNeighbor(nodesTotal)


matrix7x7 = np.array([[0, 10, 8, 5, 7, 20, 15], [0, 0, 12, 16, 9, 13, 4], [0, 0, 0, 18, 22, 30, 25], [0, 0, 0, 0, 13, 14, 24], [0, 0, 0, 0, 0, 32, 36], [0, 0, 0, 0, 0, 0, 50], [0, 0, 0, 0, 0, 0, 0]])
adjacencyMatrix = upperTriangularMatrixWithMainDiagonalAtZero(matrix7x7)
nodesTotal = len(adjacencyMatrix)
runNearestNeighborAlgorithm()
