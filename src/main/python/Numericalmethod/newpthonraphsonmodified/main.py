funcion = input('Dame la funcion f(x) : ')
dfuncion = input('Dame la derivada de funcion f(x) : ')
d2funcion = input('Dame la segunda derivada de funcion f(x) : ')

xi = int(input('Dame el valor inicial de x : '))
e = float(input('Dame el porciento del error : '))
ea = 1000
c = 1
x = xi

while ea > e:
    g = eval(funcion) # -0.9*x**2+1.7*x+2.5
    h = eval(dfuncion) # -1.8*x+1.7
    k = eval(d2funcion) # -1.8
    j = x - (g * h) / (h ** 2 - (g * k))
    ea = abs((j - x) / j * 100)
    x = j
    c = c+1


print(f'\n\n\n\nLa raiz exacta es: {j:.6f}')
print(f'\n\nNumero de iteraciones: {c:1d}')
