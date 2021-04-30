import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as spc
import vec2d as vec
import scipy.optimize as spo

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

def F(x, y):                                # Coulomb force between fixed target
    r = vec.vec2d(x, y)                       # at origin and incident particle
    return F0 * r / r.mod()**3

def step(r, v, tau):                        # Velocity-Verlet integration step
    new_r = r + v * tau + F(r.x, r.y) * tau**2 / 2
    new_v = v + (F(r.x, r.y) + F(new_r.x, new_r.y)) * tau / 2
    return new_r, new_v

def solve(r0, v0, tau, N):
    new_r, new_v = r0, v0
    for i in range(N - 1):
        new_r, new_v = step(new_r, new_v, tau)
    return new_r, new_v

def fit(theta, N, alpha):
    return N * F0 * alpha_mass / (2 * E * d0 * np.sin(theta / 2)**alpha)

np.random.seed()
theta = []
N_part = 1000

for i in range(N_part):
    r0 = vec.vec2d(- 100, (2 * np.random.rand() - 1) * 100) * d0
    v0 = vec.vec2d(1, 0) * np.sqrt(2 * E / (2 * spc.proton_mass + 2 * spc.neutron_mass))
    tau = d0 / v0.mod()
    N = 2 * int(r0.mod() / d0)

    r, v = solve(r0, v0, tau, N)

    theta.append(v.get_angle(v0))

# Uncomment to save data
# f = open("data.dat", "w")
# for angle in theta:
#     f.write(str(angle) + "\n")

fig, ax = plt.subplots()
ax.hist(theta, histtype = "step", bins = 10, label = "Data")
ax.set_yscale("log")

counts, bins = np.histogram(theta, bins = 10)
bins = bins[1:] - (bins[1] - bins[0]) / 2
p, cov = spo.curve_fit(fit, bins, counts, p0 = [1, 2], sigma = counts)
print(p, cov)
x = np.linspace(bins[0], bins[-1], 1000)
y = fit(x, p[0], p[1])

ax.plot(x, y, label = "fit", linewidth = 1)
ax.set_ylabel("Counts")
ax.set_xlabel("$\\theta$")
ax.legend()

plt.show()
