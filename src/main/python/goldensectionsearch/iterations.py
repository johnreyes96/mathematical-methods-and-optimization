import math

import matplotlib.pyplot as plt
import numpy as np


def objectiveFunctionGraph():
    a, b = 0, 2

    T = np.linspace(a, b, 10)
    U = -1.5 * T ** 6 - 2 * T ** 4 + 12 * T

    plt.plot(T, U, 'b')
    plt.plot(1, 8, 'ko')
    plt.annotate(r'$8.697929$', (8.697929, 0.88), (1, 8))

    plt.grid()
    plt.show()


# objectiveFunctionGraph()


# Objective function
def U(T):
    return -1.5 * T ** 6 - 2 * T ** 4 + 12 * T


def isRemoveLastNumberOfArray(array, newValue):
    if array.index(newValue) == 1:
        return True
    else:
        return False


def GoldenSectionSearch():
    xi = 0
    xs = 2
    epsilon = 1e-3
    cont = 0

    while True:
        d = ((math.sqrt(5) - 1) / 2) * (xs - xi)
        # if cont == 0:
        x1 = xi + d
        x2 = xs - d
        cont = cont + 1
        print("I: {:02d}   |- {:.5f} --- {:.5f} --- {:.5f} --- {:.5f} -|".format(cont, xi, x2, x1, xs))
        fx1 = U(x1)
        fx2 = U(x2)

        if fx1 < fx2:
            xs = x1
        else:
            xi = x2

        # if np.abs(U_alpha1 - U_alpha2) < epsilon:
        #     print("-------------------------------------------------------")
        #     print("It: {:02d} - Temp: {:.10f} - Costo: {:.10f} - {:.10f} - {:.10f}".format(cont, alpha1, U_alpha1, alpha2, U_alpha2))
        if cont == 3:
            break


GoldenSectionSearch()
