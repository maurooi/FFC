import numpy as np
import scipy as spc
import matplotlib.pyplot as plt

def f(t, a, b):
    return a * np.exp(- t / b) * np.sin(30 * 2 * np.pi * t) / 10

N = 1000
t = np.linspace(0, 2, N)
y = f(t, 10, 0.1)
T = t[-1]
tau = t[1] - t[0]

omega, F = [t[i] / (2 * T * tau) for i in range(N)], np.abs(spc.fft(y))[: N // 2] * tau

fig, ax = plt.subplots()
ax.plot(t, y)
ax.set_xlabel("t")
ax.set_ylabel("y(t)")

fig1, ax1 = plt.subplots()
ax1.plot(F)
ax1.set_xlabel("$\omega$")
ax1.set_ylabel("$\mathcal{F}(\omega)$")

plt.show()
