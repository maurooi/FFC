import numpy as np
import matplotlib.pyplot as plt

# Read data
f = open("sunspots.txt", "r")

t_data, y_data = [], []
data = f.readlines()
for line in data:
    t, y = line.split()
    t_data.append(float(t))
    y_data.append(float(y))

y, t = np.array(y_data), np.array(t_data)

# Fourier Transform
nu, F = np.fft.rfftfreq(len(y)), np.fft.rfft(y)
F[0] = 0            # Shifts the mean to zero

# Plot data and inverse Fourirer transform
fig, ax = plt.subplots()
ax.plot(t_data, y_data, label = "Original data")
ax.plot(t[:-1], np.fft.irfft(F), label = "Inverse Fourire Transform")
ax.set_xlabel("t")
ax.set_ylabel("y")
ax.legend()

# Plot Fourire transform
fig1, ax1 = plt.subplots()
ax1.plot(nu, np.abs(F), label = "Fourier")
ax1.set_xlabel("$\\nu$")
ax1.set_ylabel("$\mathcal{F}_\\nu(y)$")
ax1.legend()

plt.show()
