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
    hamiltonianCyclesList = []
    for indexRow, row in enumerate(adjacencyMatrix):
        currentRow = indexRow
        hamiltonianCycle = [np.where(adjacencyMatrix[currentRow] == [row[currentRow]])[0][0]]
        for node in range(len(adjacencyMatrix) - 1):
            currentRow = getNearestNeighbor(adjacencyMatrix, hamiltonianCycle, currentRow)
            hamiltonianCycle.append(currentRow)
        hamiltonianCycle.append(hamiltonianCycle[0])
        hamiltonianCycleString = '-'.join(map(str, hamiltonianCycle))
        formattedHamiltonianCycle = getHamiltonianCycle(len(hamiltonianCycle) - 1, hamiltonianCycleString)
        hamiltonianCycleWeight = getWeightFromHamiltonianCycle(len(hamiltonianCycle) - 1, formattedHamiltonianCycle,
                                                               adjacencyMatrix)
        hamiltonianCyclesList.append({
            'cycle': formattedHamiltonianCycle,
            'weight': hamiltonianCycleWeight
        })
    return hamiltonianCyclesList


def getWeightFromHamiltonianCycle(nodesNumber, formattedHamiltonianCycle, adjacencyMatrix):
    nodesLetters = getNodes(nodesNumber)
    hamiltonianCycle = formattedHamiltonianCycle.split("-")
    weight = 0
    for nodeIndex in range(len(hamiltonianCycle) - 1):
        rowIndex = nodesLetters.index(hamiltonianCycle[nodeIndex])
        rowColumn = nodesLetters.index(hamiltonianCycle[nodeIndex+1])
        weight += adjacencyMatrix[rowIndex][rowColumn]
    return weight


def getNodes(nodesNumber):
    switcher = {
        1: ['A'],
        2: ['A', 'B'],
        3: ['A', 'B', 'C'],
        4: ['A', 'B', 'C', 'D'],
        5: ['A', 'B', 'C', 'D', 'E'],
        6: ['A', 'B', 'C', 'D', 'E', 'F'],
        7: ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        8: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
        9: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
        10: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    }
    return switcher.get(nodesNumber)


def getHamiltonianCycle(nodesNumber, hamiltonianCycle):
    nodes = getNodes(nodesNumber)
    initialNode = hamiltonianCycle[0:1]
    initialNodeReplaced = nodes[int(hamiltonianCycle[0:1])]
    count = 1
    for nodeIndex in range(len(nodes)):
        if nodeIndex == 0:
            hamiltonianCycle = hamiltonianCycle.replace(initialNode, initialNodeReplaced, 1)
        else:
            nodeToReplace = hamiltonianCycle[nodeIndex + count]
            nodeReplaced = nodes[int(hamiltonianCycle[nodeIndex + count])]
            hamiltonianCycle = hamiltonianCycle.replace(nodeToReplace, nodeReplaced, 1)
            count += 1
    hamiltonianCycle = hamiltonianCycle.replace(initialNode, initialNodeReplaced)
    return hamiltonianCycle


def sortHamiltonianCyclesByWeight(hamiltonianCyclesList):
    return hamiltonianCyclesList['weight']


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
    hamiltonianCycles = nearestNeighbor(adjacencyMatrix)
    hamiltonianCycles.sort(key=sortHamiltonianCyclesByWeight)
    print(*hamiltonianCycles, sep="\n")
    print("")
    hamiltonianCycleLessWeight = hamiltonianCycles[0]
    print("El ciclo Hamiltoniano de menor peso usando el algoritmo del vecino más cercano es: " +
          str(hamiltonianCycleLessWeight["cycle"]) + " con un peso de: " + str(hamiltonianCycleLessWeight["weight"]))


runNearestNeighborAlgorithm()
