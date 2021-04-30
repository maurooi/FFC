import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo
import scipy.constants as spc

Z1, Z2 = 2, 79                              # Atomic number
alpha_mass = (2 * spc.proton_mass + 2 * spc.neutron_mass)
                                            # Mass of alpha particle in kg
F0 = Z1 * Z2 * spc.e**2 / \
        (4 * spc.pi * spc.epsilon_0 * alpha_mass)
                                            # Force amplitude in N * m**2 / kg
E = 5 * spc.electron_volt * 1e6             # Initial energy of the particle in J
d0 = F0 / E * alpha_mass                    # Special unit of length, it is almost
                                            # the minimum distance between the
                                            # target and the incident particle

def fit(theta, N, alpha):                   # Fitting function
    return N * F0 * alpha_mass / (2 * E * d0 * np.sin(theta / 2)**alpha)

f = open("data.dat", "r")                   # Open data file in reading mode

theta = []
for angle in f:
    theta.append(float(angle))              # Read each line

fig, ax = plt.subplots()                    # Plot histogram
ax.hist(theta, histtype = "step", bins = 30, label = "Data")
ax.set_yscale("log")

                                            # Fit histogram data
counts, bins = np.histogram(theta, bins = 30)
bins = bins[1:] - (bins[1] - bins[0]) / 2
p, cov = spo.curve_fit(fit, bins, counts, p0 = [1, 2], sigma = counts)
print(p, "\n", cov)
x = np.linspace(bins[0], bins[-1], 1000)
y = fit(x, p[0], p[1])

ax.plot(x, y, label = "fit", linewidth = 1) # Plot fit
ax.set_ylabel("Counts")
ax.set_xlabel("$\\theta$")
ax.legend()

plt.show()
