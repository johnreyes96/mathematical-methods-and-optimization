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


def getNodes():
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
    return switcher.get(nodesTotal)


def getHamiltonianCycle(cycle):
    nodes = getNodes()
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
    nodesLetters = getNodes()
    hamiltonianCycle = formattedHamiltonianCycle.split("-")
    weight = 0
    for nodeIndex in range(len(hamiltonianCycle) - 1):
        rowIndex = nodesLetters.index(hamiltonianCycle[nodeIndex])
        rowColumn = nodesLetters.index(hamiltonianCycle[nodeIndex+1])
        weight += adjacencyMatrix[rowIndex][rowColumn]
    return weight


def sortHamiltonianCyclesByWeight(hamiltonianCyclesList):
    return hamiltonianCyclesList['weight']


def unique(hamiltonianCycles):
    hamiltonianCycles.sort(key=sortHamiltonianCyclesByWeight)
    initialNode = hamiltonianCycles[0]["cycle"][0]
    hamiltonianCyclesDistinct = []
    hamiltonianCyclesTemp = []
    hamiltonianCyclesTempAux = []
    countNodesWithEqualsWeight = 0
    lastNode = hamiltonianCycles[-1]
    for item in hamiltonianCycles:
        if initialNode == item["cycle"][0]:  # item["cycle"][0][::-1]
            if len(hamiltonianCyclesTemp) == 0 or item["weight"] == hamiltonianCyclesTemp[countNodesWithEqualsWeight-1]["weight"]:
                hamiltonianCyclesTemp.append(item)
                countNodesWithEqualsWeight += 1
            else:
                hamiltonianCyclesTempAux.append(item)
                if countNodesWithEqualsWeight == 2:
                    hamiltonianCyclesDistinct.append(hamiltonianCyclesTemp[0])
                    hamiltonianCyclesTemp = hamiltonianCyclesTempAux
                    hamiltonianCyclesTempAux = []
                    countNodesWithEqualsWeight = 1
                else:
                    hamiltonianCyclesWithSameWeight = []
                    for hamiltonianCycle in range(int(countNodesWithEqualsWeight)):
                        if hamiltonianCycle == 0:
                            hamiltonianCyclesWithSameWeight.append(hamiltonianCyclesTemp[hamiltonianCycle])
                        else:
                            flag = True
                            for node in hamiltonianCyclesWithSameWeight:
                                if node["cycle"] == hamiltonianCyclesTemp[hamiltonianCycle]["cycle"][::-1]:
                                    flag = False
                            if flag:
                                hamiltonianCyclesWithSameWeight.append(hamiltonianCyclesTemp[hamiltonianCycle])
                    hamiltonianCyclesDistinct.extend(hamiltonianCyclesWithSameWeight)
                    hamiltonianCyclesTemp = hamiltonianCyclesTempAux
                    hamiltonianCyclesTempAux = []
                    countNodesWithEqualsWeight = 1
        elif item == lastNode:
            hamiltonianCyclesTempAux.append(item)
            if countNodesWithEqualsWeight == 2:
                hamiltonianCyclesDistinct.append(hamiltonianCyclesTemp[0])
            else:
                hamiltonianCyclesWithSameWeight = []
                for hamiltonianCycle in range(int(countNodesWithEqualsWeight)):
                    if hamiltonianCycle == 0:
                        hamiltonianCyclesWithSameWeight.append(hamiltonianCyclesTemp[hamiltonianCycle])
                    else:
                        flag = True
                        for node in hamiltonianCyclesWithSameWeight:
                            if node["cycle"] == hamiltonianCyclesTemp[hamiltonianCycle]["cycle"][::-1]:
                                flag = False
                        if flag:
                            hamiltonianCyclesWithSameWeight.append(hamiltonianCyclesTemp[hamiltonianCycle])
                hamiltonianCyclesDistinct.extend(hamiltonianCyclesWithSameWeight)
    return hamiltonianCyclesDistinct


def runHamiltonianCycleAlgorithm():
    print(str(adjacencyMatrix)+"\n")
    hamiltonianCycles = bruteForceSearch(nodesTotal)
    hamiltonianCyclesDistinct = unique(hamiltonianCycles)
    hamiltonianCyclesDistinct.sort(key=sortHamiltonianCyclesByWeight)
    print(*hamiltonianCyclesDistinct, sep="\n")
    print("")
    print("Cantidad de ciclos Hamiltonianos diferentes: " + str(len(hamiltonianCyclesDistinct)))
    hamiltonianCycleLessWeight = hamiltonianCyclesDistinct[0]
    print("El ciclo Hamiltoniano de menor peso es: " + str(hamiltonianCycleLessWeight["cycle"]) + " con un peso de: " +
          str(hamiltonianCycleLessWeight["weight"]))


matrix3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix4x4 = np.array([[0, 5, 9, 7], [0, 0, 4, 10], [0, 0, 0, 12], [0, 0, 0, 0]])
matrix5x5 = np.array([[0, 4, 13, 15, 4], [0, 0, 7, 20, 35], [0, 0, 0, 22, 24], [0, 0, 0, 0, 10], [0, 0, 0, 0, 0]])
matrix6x6 = np.array([[0, 4, 13, 26, 90, 40], [0, 0, 7, 50, 35, 6], [0, 0, 0, 22, 24, 30], [0, 0, 0, 0, 10, 180], [0, 0, 0, 0, 0, 16], [0, 0, 0, 0, 0, 0]])
matrix7x7 = np.array([[0, 4, 13, 15, 28, 40, 24], [0, 0, 7, 20, 35, 6, 42], [0, 0, 0, 22, 24, 30, 10], [0, 0, 0, 0, 10, 20, 25], [0, 0, 0, 0, 0, 16, 18], [0, 0, 0, 0, 0, 0, 5], [0, 0, 0, 0, 0, 0, 0]])
matrix7x7_2 = np.array([[0, 10, 18, 5, 30, 40, 30], [0, 0, 15, 20, 35, 60, 26], [0, 0, 0, 22, 30, 42, 10], [0, 0, 0, 0, 10, 28, 12], [0, 0, 0, 0, 0, 16, 18], [0, 0, 0, 0, 0, 0, 50], [0, 0, 0, 0, 0, 0, 0]])
adjacencyMatrix = upperTriangularMatrixWithMainDiagonalAtZero(matrix7x7)
nodesTotal = len(adjacencyMatrix)
runHamiltonianCycleAlgorithm()
