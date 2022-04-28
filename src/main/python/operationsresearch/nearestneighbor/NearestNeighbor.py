import numpy as np


def upperTriangularMatrixWithMainDiagonalAtZero(matrixNxN):
    UpperTriangleMatrix = np.triu(matrixNxN, 1)
    return UpperTriangleMatrix + UpperTriangleMatrix.T - np.diag(np.diag(UpperTriangleMatrix))


def nearestNeighbor(adjacencyMatrix):
    for indexRow, row in enumerate(adjacencyMatrix):
        rowToCompare = row
        for node in range(len(row)):
            print(str(rowToCompare)+": "+str(np.min(rowToCompare)))
            if node == 0:
                hamiltonianCycle = str(np.where(rowToCompare == 0)[0][0])
                # hamiltonianCycle = str("-") + str(column)
                rowToCompare = np.delete(rowToCompare, np.where(rowToCompare == np.min(rowToCompare))[0][0])
            else:
                rowToCompare = np.delete(rowToCompare, np.where(rowToCompare == np.min(rowToCompare))[0][0])
            # rowToCompare = np.delete(rowToCompare, np.min(rowToCompare))
            # print(rowToCompare)
            # print(str(rowToCompare)+": "+str(np.min(rowToCompare)))
            # print(str(np.min(row))+"|"+str(np.where(row == 0)[0][0]))
        print("\n")


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
