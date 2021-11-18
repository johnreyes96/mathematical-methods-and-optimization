import math


def formula(x):
    numerator = f(x[0]) * (x[1] ** 2 - x[2] ** 2) + f(x[1]) * (x[2] ** 2 - x[0] ** 2) + f(x[2]) * (x[0] ** 2 - x[1] ** 2)
    denominator = 2 * f(x[0]) * (x[1] - x[2]) + 2 * f(x[1]) * (x[2] - x[0]) + 2 * f(x[2]) * (x[0] - x[1])
    return numerator / denominator


def f(value):
    return 2 * math.sin(value) - (value ** 2 / 10)


xValues = []

for index in range(0, 3):
    xValue = float(input("Introduce el valor para x[" + str(index) + "] "))
    xValues.append(xValue)

print("El valor de f(x) es: ", formula(xValues))
