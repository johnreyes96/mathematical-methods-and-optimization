from builtins import len
import numpy as np


def upperTriangularMatrixWithMainDiagonalAtZero(adjacencyMatrix):
    return np.triu(adjacencyMatrix, 1)


def bruteForceSearch(adjacencyMatrix, count=0, cycle=""):
    for index in range(adjacencyMatrix):
        if index == 0:
            cycle += str(index)
        else:
            cycle = str(cycle[0:len(cycle)-1]) + str(index)
        if adjacencyMatrix == 1 and index == 0:
            count += 1
            print(str(count)+":"+str(cycle)+"|"+str(a[index][3])+": "+str(adjacencyMatrix)+"-"+str(index)) # ciclo hamiltoniano completo
            cycle = ""
        if adjacencyMatrix == 4:
            print(index) # indica que empieza a recorrer todos los ciclos hamiltonianos a partir del primer nodo
        # print(str(adjacencyMatrix) + "-" + str(index)) # el primer numero indica la cantidad de relaciones a nodos
        count = bruteForceSearch(adjacencyMatrix - 1, count, cycle)
    return count


# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a = np.array([[0, 5, 9, 7], [0, 0, 4, 10], [0, 0, 0, 12], [7, 0, 0, 40]])
b = upperTriangularMatrixWithMainDiagonalAtZero(a)
print(a)
print("cantidad de ciclos Hamiltonianos: " + str(bruteForceSearch(len(a))))
