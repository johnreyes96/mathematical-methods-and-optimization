def formula(x, fx):
    b0 = fx[0]
    b1 = (fx[1] - fx[0]) / (x[1] - x[0])
    b2 = (((fx[2] - fx[1]) / (x[2] - x[1])) - ((fx[1] - fx[0]) / (x[1] - x[0]))) / (x[2] - x[0])
    f2 = b0 + b1 * (x[3] - x[0]) + b2 * (x[3] - x[0]) * (x[3] - x[1])
    return f2


x = []
fx = []

for i in range(0, 3):
    vx = float(input("Introduce el valor para x[" + str(i + 1) + "] "))
    x.append(vx)
    vfx = float(input("Introduce el valor para fx[" + str(i + 1) + "] "))
    fx.append(vfx)

vx = float(input("Introduce el valor de x para calcular f(x): "))
x.append(vx)
print("El valor de f(x) es: ", formula(x, fx))
