from builtins import len
import numpy as np


def upperTriangularMatrixWithMainDiagonalAtZero(adjacencyMatrix):
    return np.triu(adjacencyMatrix, 1)


def bruteForceSearch(adjacencyMatrix, hamiltonianCyclesList=[], cycle="", initialIndex=-1):
    for index in range(adjacencyMatrix):
        if index == 0:
            cycle += str("-") + str(index)
        else:
            cycle = str(cycle[0:len(cycle) - 1]) + str(index)
        if adjacencyMatrix == 1 and index == 0:
            cycle += str("-") + str(initialIndex)
            sss = getHamiltonianCycle(cycle)
            hamiltonianCyclesList.append(sss)
            print(str(len(hamiltonianCyclesList)) + ": " + str(sss))
            cycle = ""
        if adjacencyMatrix == 4:
            initialIndex = index
        bruteForceSearch(adjacencyMatrix - 1, hamiltonianCyclesList, cycle, initialIndex)
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
a = np.array([[0, 5, 9, 7], [0, 0, 4, 10], [0, 0, 0, 12], [0, 0, 0, 0]])
b = upperTriangularMatrixWithMainDiagonalAtZero(a)
print(a)
print("cantidad de ciclos Hamiltonianos: " + str(len(bruteForceSearch(len(a)))))
