from builtins import len
import numpy as np


def upperTriangularMatrixWithMainDiagonalAtZero(matrixNxN):
    UpperTriangleMatrix = np.triu(matrixNxN, 1)
    return UpperTriangleMatrix + UpperTriangleMatrix.T - np.diag(np.diag(UpperTriangleMatrix))


def bruteForceSearch(nodesCount, hamiltonianCyclesList=None, hamiltonianCycle="", initialIndex=-1, flag=True):
    global nodesTotal
    if flag:
        nodesTotal = nodesCount
        hamiltonianCyclesList = []
        flag = False
    for index in range(nodesCount):
        if index == 0:
            hamiltonianCycle += str("-") + str(index)
        else:
            hamiltonianCycle = str(hamiltonianCycle[0:len(hamiltonianCycle) - 1]) + str(index)
        if nodesCount == 1 and index == 0:
            hamiltonianCycle += str("-") + str(initialIndex)
            formattedHamiltonianCycle = getHamiltonianCycle(hamiltonianCycle)
            hamiltonianCycleWeight = getWeightFromHamiltonianCycle(formattedHamiltonianCycle)
            hamiltonianCyclesList.append({
                'cycle': formattedHamiltonianCycle,
                'weight': hamiltonianCycleWeight
            })
            hamiltonianCycle = ""
        if nodesCount == nodesTotal:
            initialIndex = index
        bruteForceSearch(nodesCount - 1, hamiltonianCyclesList, hamiltonianCycle, initialIndex, flag)
    return hamiltonianCyclesList


def getHamiltonianCycle(cycle):
    nodes = ['A', 'B', 'C', 'D']
    hamiltonianCycle = cycle[1:len(cycle)]
    initialNode = hamiltonianCycle[0:1]
    initialNodeReplaced = nodes[int(hamiltonianCycle[0:1])]
    count = 1
    for nodeIndex in range(len(nodes)):
        if nodeIndex == 0:
            hamiltonianCycle = hamiltonianCycle.replace(initialNode, initialNodeReplaced, 1)
            nodes.pop(int(initialNode))
        else:
            nodeToReplace = hamiltonianCycle[nodeIndex + count]
            nodeReplaced = nodes[int(hamiltonianCycle[nodeIndex + count])]
            hamiltonianCycle = hamiltonianCycle.replace(nodeToReplace, nodeReplaced, 1)
            nodes.pop(int(nodeToReplace))
            count += 1
    hamiltonianCycle = hamiltonianCycle.replace(initialNode, initialNodeReplaced)
    return hamiltonianCycle


def getWeightFromHamiltonianCycle(formattedHamiltonianCycle):
    nodesLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    hamiltonianCycle = formattedHamiltonianCycle.split("-")
    weight = 0
    for nodeIndex in range(len(hamiltonianCycle) - 1):
        rowIndex = nodesLetters.index(hamiltonianCycle[nodeIndex])
        rowColumn = nodesLetters.index(hamiltonianCycle[nodeIndex+1])
        weight += adjacencyMatrix[rowIndex][rowColumn]
    return weight


def sortHamiltonianCyclesByWeight(hamiltonianCyclesList):
    return hamiltonianCyclesList['weight']


# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix = np.array([[0, 5, 9, 7], [0, 0, 4, 10], [0, 0, 0, 12], [0, 0, 0, 0]])
adjacencyMatrix = upperTriangularMatrixWithMainDiagonalAtZero(matrix)
print(adjacencyMatrix)
nodesTotal = len(adjacencyMatrix)
hamiltonianCycles = bruteForceSearch(nodesTotal)
hamiltonianCycles.sort(key=sortHamiltonianCyclesByWeight)
print(*hamiltonianCycles, sep="\n")
print("Cantidad de ciclos Hamiltonianos repetidos: " + str(len(hamiltonianCycles)))
hamiltonianCycleLessWeight = hamiltonianCycles[0]
print("El ciclo Hamiltoniano de menor peso es: " + str(hamiltonianCycleLessWeight["cycle"]) + " con un peso de: " +
      str(hamiltonianCycleLessWeight["weight"]))
