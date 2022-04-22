from builtins import len
import numpy as np


def upperTriangularMatrixWithMainDiagonalAtZero(adjacencyMatrix):
    return np.triu(adjacencyMatrix, 1)


def bruteForceSearch(adjacencyMatrix, count=0, cycle="", initialIndex=-1):
    for index in range(adjacencyMatrix):
        if index == 0:
            cycle += str("-") + str(index)
        else:
            cycle = str(cycle[0:len(cycle)-1]) + str(index)
        if adjacencyMatrix == 1 and index == 0:
            count += 1
            cycle += str("-")+str(initialIndex)
            print(str(count)+": "+str(getHamiltonianoCycle(cycle)))  # ciclo hamiltoniano completo
            cycle = ""
        if adjacencyMatrix == 4:
            initialIndex = index
            # print(index)  # indica que empieza a recorrer todos los ciclos hamiltonianos a partir del primer nodo
        # print(str(adjacencyMatrix) + "-" + str(index)) # el primer numero indica la cantidad de relaciones a nodos
        count = bruteForceSearch(adjacencyMatrix - 1, count, cycle, initialIndex)
    return count


def getHamiltonianoCycle(cycle):
    nodes = ['A', 'B', 'C', 'D']
    hamiltonianoCycle = cycle[1:len(cycle)]
    initialNode = hamiltonianoCycle[0:1]
    initialNodeReplaced = nodes[int(hamiltonianoCycle[0:1])]
    count = 1
    for nodeIndex in range(len(nodes)):
        if nodeIndex == 0:
            hamiltonianoCycle = hamiltonianoCycle.replace(initialNode, initialNodeReplaced, 1)
            nodes.pop(int(initialNode))
        else:
            nodeToReplace = hamiltonianoCycle[nodeIndex + count]
            nodeReplaced = nodes[int(hamiltonianoCycle[nodeIndex + count])]
            hamiltonianoCycle = hamiltonianoCycle.replace(nodeToReplace, nodeReplaced, 1)
            nodes.pop(int(nodeToReplace))
            count += 1
    hamiltonianoCycle = hamiltonianoCycle.replace(initialNode, initialNodeReplaced)
    return hamiltonianoCycle


# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a = np.array([[0, 5, 9, 7], [0, 0, 4, 10], [0, 0, 0, 12], [0, 0, 0, 0]])
b = upperTriangularMatrixWithMainDiagonalAtZero(a)
print(a)
print("cantidad de ciclos Hamiltonianos: " + str(bruteForceSearch(len(a))))
