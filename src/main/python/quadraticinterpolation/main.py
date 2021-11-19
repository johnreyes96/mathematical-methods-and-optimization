import math


def formula(x):
    numerator = f(x[0]) * (x[1] ** 2 - x[2] ** 2) + f(x[1]) * (x[2] ** 2 - x[0] ** 2) + f(x[2]) * (
                x[0] ** 2 - x[1] ** 2)
    denominator = 2 * f(x[0]) * (x[1] - x[2]) + 2 * f(x[1]) * (x[2] - x[0]) + 2 * f(x[2]) * (x[0] - x[1])
    return numerator / denominator


def f(value):
    return 2 * value + (3 / value)


def isRemoveLastNumberOfArray(array, newValue):
    if array.index(newValue) == 1:
        return True
    else:
        return False


xValues = []

for index in range(0, 3):
    xValue = float(input("Introduce el valor para x[" + str(index) + "] "))
    xValues.append(xValue)

for iterator in range(1, 11):
    x3 = formula(xValues)
    xValues.append(x3)
    graphValues = sorted(xValues)
    print("I: {:02d} - x0: {:.3f} - f(x0): {:.4f} - x1: {:.3f} - f(x1): {:.4f} - x2: {:.3f} - f(x2): {:.4f} - x3: "
          "{:.3f} - f(x3): {:.4f}    |- {:.5f} --- {:.5f} --- {:.5f} --- {:.5f} -|".format(iterator, xValues[0],
                                                                                           f(xValues[0]), xValues[1],
                                                                                           f(xValues[1]), xValues[2],
                                                                                           f(xValues[2]), x3, f(x3),
                                                                                           graphValues[0],
                                                                                           graphValues[1],
                                                                                           graphValues[2],
                                                                                           graphValues[3]))

    xValues = sorted(xValues)
    if isRemoveLastNumberOfArray(xValues, x3):
        xValues.pop()
    else:
        xValues.pop(0)
