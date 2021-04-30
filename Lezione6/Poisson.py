import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Implementation of boundary conditions
def is_over_boundary(i, j, N, boundary):
    return np.sqrt((i - int(N / 2))**2 + (j - int(N / 2))**2) > boundary

# Computes one iteration of the SOR algorithm
def SOR_alg(V, rho, h, w, N, i, j, boundary):
    if is_over_boundary(i, j, N, boundary):
        return 0
    new_V = w * (V[i + 1, j] + V[i - 1, j] + V[i, j + 1] + V[i, j - 1] + h * h * rho[i, j]) / 4 + (1 - w) * V[i, j]
    return new_V

# Compute one complete step of the SOR algorithm
def step(V, rho, h, w, N, boundary):
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            V[i, j] = SOR_alg(V, rho, h, w, N, i, j, boundary)
    return V

# Check convergence of the algorithm
def convergence_condition(difference, threshold):
    if difference < threshold:
        return True
    return False

# Solves the problem with relaxation method
def run_SOR(V, rho, h, w, threshold, boundary):
    diff = 10
    N = len(V)
    while not convergence_condition(diff, threshold):
        old_V = V.copy()
        V = step(V, rho, h, w, N, boundary)
        diff = np.max(np.abs(V - old_V)) / (np.max(rho) * h**2)
    return V

# Declaration of useful constants
N = 101
L = 1                   # Length of the box, in m
h = N / L               # Spatial separation between two grid points, in m
w = 1.8                 # Relaxation parameter
V = np.zeros((N, N))    # Potential
rho = np.zeros((N, N))  # Charge density

# Initial conditions
cx, cy = int(N / 2), int(N / 2)
rho[cx, cy] = 1e-3 / h**2        # Initial charge density

V = run_SOR(V, rho, h, w, 1e-5, N / 2) * 1e3    # mV

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")

x, y = np.meshgrid([i * L / N for i in range(N)], [i * L / N for i in range(N)])
ax.plot_wireframe(x, y, V)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("V(x, y)")

fig1, ax1 = plt.subplots()
cplot = ax1.contour(x, y, V, levels = 10)
ax1.clabel(cplot, inline = True, fontsize = 10)
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.axis("equal")

plt.show()
