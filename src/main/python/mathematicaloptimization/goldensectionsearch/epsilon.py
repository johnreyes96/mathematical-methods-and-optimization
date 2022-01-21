import math

import matplotlib.pyplot as plt
import numpy as np


def objectiveFunctionGraph():
    a, b = 0, 60
    T = np.linspace(a, b, 10)
    U = math.tan(50 / 180 * math.pi) * T - (9.81 / (2 * 25 ** 2 * math.cos(50 / 180 * math.pi) *
                                                    math.cos(50 / 180 * math.pi))) * T ** 2 + 1

    plt.plot(T, U, 'b')
    plt.plot(31.5, 19.7, 'ko')
    plt.annotate(r'$31.5, 19.7$', (31.5, 19.7), (31.5, 19.7))

    plt.grid()
    plt.show()


objectiveFunctionGraph()


def U(T):
    return math.tan(50 / 180 * math.pi) * T - (9.81 / (2 * 25 ** 2 * math.cos(50 / 180 * math.pi) *
                                                       math.cos(50 / 180 * math.pi))) * T ** 2 + 1


def GoldenSectionSearch():
    xi = 0
    xs = 60
    epsilon = 1
    cont = 0

    while True:
        d = ((math.sqrt(5) - 1) / 2) * (xs - xi)
        x1 = xi + d
        x2 = xs - d
        fx1 = U(x1)
        fx2 = U(x2)
        cont = cont + 1
        if abs(x1 - x2) < epsilon:
            print("-------------------------------------------------------")
            print("I: {:02d} - xi: {:.4f} - D: {:.4f} - x1: {:.4f} - x2: {:.4f} - f(x1): {:.4f} - f(x2): {:.4f} - "
                  "xu: {:.4f} - Error: {:.4f}    |- {:.5f} --- {:.5f} --- {:.5f} --- {:.5f} -|".format(cont, xi, d, x1,
                                                                                                       x2, fx1, fx2, xs,
                                                                                                       abs(x1 - x2), xi,
                                                                                                       x2, x1, xs))
        else:
            print("I: {:02d} - xi: {:.4f} - D: {:.4f} - x1: {:.4f} - x2: {:.4f} - f(x1): {:.4f} - f(x2): {:.4f} - "
                  "xu: {:.4f} - Error: {:.4f}    |- {:.5f} --- {:.5f} --- {:.5f} --- {:.5f} -|".format(cont, xi, d, x1,
                                                                                                       x2, fx1, fx2, xs,
                                                                                                       abs(x1 - x2), xi,
                                                                                                       x2, x1, xs))

        if fx1 < fx2:
            xs = x1
        else:
            xi = x2

        if abs(x1 - x2) < epsilon:
            break


GoldenSectionSearch()
