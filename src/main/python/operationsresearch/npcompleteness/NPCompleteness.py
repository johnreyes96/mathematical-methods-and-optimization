from builtins import len
import numpy as np


def upperTriangularMatrixWithMainDiagonalAtZero(matrix):
    return np.triu(matrix, 1)


def bruteForceSearch(nodesCount, hamiltonianCyclesList=[], hamiltonianCycle="", initialIndex=-1, flag=True):
    global nodesTotal
    if flag:
        nodesTotal = nodesCount
        flag = False
    for index in range(nodesCount):
        if index == 0:
            hamiltonianCycle += str("-") + str(index)
        else:
            hamiltonianCycle = str(hamiltonianCycle[0:len(hamiltonianCycle) - 1]) + str(index)
        if nodesCount == 1 and index == 0:
            hamiltonianCycle += str("-") + str(initialIndex)
            formattedHamiltonianCycle = getHamiltonianCycle(hamiltonianCycle)
            hamiltonianCyclesList.append(formattedHamiltonianCycle)
            print(str(len(hamiltonianCyclesList)) + ": " + str(formattedHamiltonianCycle))
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


# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix = np.array([[0, 5, 9, 7], [0, 0, 4, 10], [0, 0, 0, 12], [0, 0, 0, 0]])
adjacencyMatrix = upperTriangularMatrixWithMainDiagonalAtZero(matrix)
print(matrix)
nodesTotal = len(matrix)
print("cantidad de ciclos Hamiltonianos: " + str(len(bruteForceSearch(nodesTotal))))
