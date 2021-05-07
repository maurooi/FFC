import numpy as np
import matplotlib.pyplot as plt

def Fourier(T, t, y):
    N, tau = len(t), t[1] - t[2]
    omega = - (t -  t[int(N / 2 - 1)]) / (T * tau)
    F = np.array(
        [
            np.sum(y * np.exp(2j * np.pi * omega[i] * t))\
        for i in range(N)]
    ) * tau
    return omega, F

T = 1       # s
# t = np.linspace(- T, T, 1000, endpoint=True)
# y = np.sin(20 * np.pi * t / T) + np.sin(40 * np.pi * t / T) + np.sin(80 * np.pi * t / T)
t = np.linspace(-2, 2, 10000)
y = np.exp(- t**2 / (2 * 0.005**2))

omega, F = Fourier(t[-1], t, y)

fig, ax = plt.subplots()
ax.plot(t, y)
ax.set_xlabel("t")
ax.set_ylabel("y(t)")

fig1, ax1 = plt.subplots()
ax1.plot(omega, np.abs(F))
ax1.set_xlabel("$\omega$")
ax1.set_ylabel("$\mathcal{F}(\omega)$")

plt.show()
