function = input('Dame la función f(x) : ')
derivativeFunction = input('Dame la derivada de función f(x) : ')
secondDerivativeFunction = input('Dame la segunda derivada de función f(x) : ')

initialValue = int(input('Dame el valor inicial de x : '))  # 5
percentage = float(input('Dame el porciento del error : '))  # 0.0001
approximateError = 1000
iterations = 1
x = initialValue

print(f'Xi      | Xi+1        | ea')
while approximateError > percentage:
    functionEvaluated = eval(function)  # -0.9*x**2+1.7*x+2.5
    derivativeFunctionEvaluated = eval(derivativeFunction)  # -1.8*x+1.7
    secondDerivativeFunctionEvaluated = eval(secondDerivativeFunction)  # -1.8
    xi = x - (functionEvaluated * derivativeFunctionEvaluated) / (derivativeFunctionEvaluated ** 2 -
                                                                  (functionEvaluated *
                                                                   secondDerivativeFunctionEvaluated))
    approximateError = abs((xi - x) / xi * 100)
    x = xi
    print(f'{iterations:1d}       | {x:.9f} | {approximateError:.9f}')
    iterations = iterations + 1

print(f'\n\n\nLa raíz exacta es: {x:.9f}')
print(f'Numero de iteraciones: {iterations:1d}')
