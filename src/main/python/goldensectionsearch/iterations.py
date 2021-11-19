import math

import matplotlib.pyplot as plt
import numpy as np


def objectiveFunctionGraph():
    a, b = 0, 2

    T = np.linspace(a, b, 10)
    U = -1.5 * T ** 6 - 2 * T ** 4 + 12 * T

    plt.plot(T, U, 'b')
    plt.plot(1, 9, 'ko')
    plt.annotate(r'$8.697929$', (1, 9), (1, 9))

    plt.grid()
    plt.show()


# objectiveFunctionGraph()


def U(T):
    return -1.5 * T ** 6 - 2 * T ** 4 + 12 * T


def isRemoveLastNumberOfArray(array, newValue):
    if array.index(newValue) == 1:
        return True
    else:
        return False


def goldenSectionSearch():
    xi = 0
    xs = 2
    cont = 0

    while True:
        d = ((math.sqrt(5) - 1) / 2) * (xs - xi)
        x1 = xi + d
        x2 = xs - d
        fx1 = U(x1)
        fx2 = U(x2)
        cont = cont + 1
        print("I: {:02d} - xi: {:.4f} - D: {:.4f} - x1: {:.4f} - x2: {:.4f} - f(x1): {:.4f} - f(x2): {:.4f} - "
              "xu: {:.4f} - Error: {:.4f}    |- {:.5f} --- {:.5f} --- {:.5f} --- {:.5f} -|".format(cont, xi, d, x1, x2,
                                                                                                   fx1, fx2, xs,
                                                                                                   abs(x1 - x2), xi, x2,
                                                                                                   x1, xs))

        if fx1 < fx2:
            xs = x1
        else:
            xi = x2

        if cont == 3:
            break


goldenSectionSearch()
