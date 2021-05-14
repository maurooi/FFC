import matplotlib.pyplot as plt
import numpy as np

# Function for Fourirer transform
def Fourier(y, T, t):
    N = len(y)
    nu = np.array([(i - N // 2) / T for i in range(N)])
    F = np.array(
        [np.sum(y * np.exp(2j * np.pi * nu[i] * t)) for i in range(N)]
    ) * (t[1] - t[0])
    return nu, F

# Function for inverse Fourier transform
def InvFourier(y, nu_max, nu):
    N = len(y)
    t = np.array([i / nu_max for i in range(N)])
    invF = np.array(
        [np.sum(y * np.exp(- 2j * np.pi * nu * t[i])) for i in range(N)]
    ) * (nu[1] - nu[0])
    return t, invF

# Useful constants definition
T, N = 10, 2000
t = np.linspace(0, T, N)
y = np.sin(50 * np.pi * t / T)
nu, F = Fourier(y, T, t)
new_t, new_y = InvFourier(F, N / T, nu)

# Plot data and inverse tFourier transform
fig, ax = plt.subplots()
ax.plot(t, y, label = "Original Data")
ax.plot(new_t, new_y, label = "Inverse Fourier transform")
ax.set_xlabel("t")
ax.set_ylabel("y")
ax.legend()

# Plot Fourier transform
fig1, ax1 = plt.subplots()
ax1.plot(nu, np.abs(F), label = "Fourier Transform")
ax1.set_xlabel("$\\nu$")
ax1.set_ylabel("$\mathcal{F}_\\nu(y)$")
ax1.legend()

plt.show()
