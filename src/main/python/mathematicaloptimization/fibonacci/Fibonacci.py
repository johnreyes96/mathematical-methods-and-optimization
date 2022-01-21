import matplotlib.pyplot as plt
import numpy as np


def GraficarFuncionObjetivo():
    a, b = 40, 90

    T = np.linspace(a, b, 100)
    U = 204165.5 / (330 - 2 * T) + 10400 / (T - 20)

    plt.figure(figsize=(6, 3))
    plt.plot(T, U, 'b')
    plt.plot(55.08, 1225.17, 'ko')
    plt.annotate(r'$55.08, 1225.17$', (55.08, 1225.17), (50, 1250))
    plt.xlabel("Temperatura")
    plt.ylabel("Costo")
    plt.grid()
    plt.show()
    return None


GraficarFuncionObjetivo()


def U(T):
    return 204165.5 / (330 - 2 * T) + 10400 / (T - 20)


U(55.08)


def Fibonacci(*params):
    a = params[0]
    b = params[1]
    k = params[2]
    it = params[3]
    reg = params[4]
    L = params[5]
    n = params[6]
    fs = params[7]
    ep = params[8]

    i_arriba = n - k + 1
    i_abajo = n + 1
    Lk = L * fs[i_arriba] / fs[i_abajo]

    xa = a + Lk
    xb = b - Lk

    U_xa = U(xa)
    U_xb = U(xb)

    if U_xa > U_xb:
        a = xa
    else:
        b = xb

    if np.abs(U_xa - U_xb) > ep:
        k = k + 1
        it = it + 1

        reg.append([it, xa, U_xa])
        print("It: {:02d} - Temp: {:.10f} - Costo: {:.10f}".format(it, xa, U_xa))

        return Fibonacci(a, b, k, it, reg, L, n, fs, ep)
    else:
        print("-------------------------------------------------------")
        print("It: {:02d} - Temp: {:.10f} - Costo: {:.10f}".format(it, xa, U_xa))

        return reg


def RunFibonacci():
    n = 30

    fs = [1, 1]
    for i in range(n):
        aux = fs[-1] + fs[-2]
        fs.append(aux)

    a, b, k = 40, 90, 2
    L = b - a

    return Fibonacci(a, b, k, 0, [], b - a, n, fs, 1e-6)


reg = RunFibonacci()


def Evaluacion(reg):
    reg1 = np.array(reg)
    fig, axs = plt.subplots(1, 2, figsize=(15, 4))

    fig.suptitle('Convergencia')

    axs[0].axhline(55.08, color='k', linewidth=3, linestyle='--')
    axs[0].plot(reg1[:, 0], reg1[:, 1], linewidth=4)
    axs[0].set_xlabel('Iteraciones')
    axs[0].set_ylabel('Temperatura')
    axs[0].grid()
    axs[0].set_xlim([0, 15])

    axs[1].axhline(1225.17, color='k', linewidth=3, linestyle='--')
    axs[1].plot(reg1[:, 0], reg1[:, 2], linewidth=4)
    axs[1].set_xlabel('Iteraciones')
    axs[1].set_ylabel('Costo')
    axs[1].grid()
    axs[1].set_xlim([0, 15])

    plt.show()

    return None


Evaluacion(reg)