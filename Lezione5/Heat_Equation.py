import numpy as np
import matplotlib.pyplot as plt

# Apply selected boundary conditions
def boundary_conditions(old_T, new_T, condition = "Dirichlet"):
    if condition.lower() == "Dirichlet".lower():
        return old_T[0], old_T[-1]
    elif condition.lower() == "Neumann".lower():
        return new_T[1], new_T[-2]
    return 0, 0

# Evolve the system for 1 timestep
def step(old_T, k, h, dt, boundary = "Dirichlet"):
    N_x = len(old_T)
    new_T = np.zeros(N_x)
    for i in range(1, N_x - 1):
        new_T[i] = old_T[i] + dt * k / h**2 * (old_T[i+1] + old_T[i-1] - 2 * old_T[i])
    new_T[0], new_T[-1] = boundary_conditions(old_T, new_T, condition = boundary)
    return new_T

# Full simulation
def solve(N_t, T, k, h, dt, boundary = "Dirichlet"):
    for i in range(1, N_t):
        T[i] = step(T[i - 1], k, h, dt, boundary)
    return T

# Constants
N_x, N_t = 100, 10000
k = 1                                                                           # m**2 / s
h = 0.01                                                                        # m
dt = 0.5 * h**2 / (2 * k)                                                       # s
T = np.zeros((N_t, N_x))                                                        # K

# Initial conditions
T[0][int(N_x / 2 - N_x / 10) : int(N_x / 2 + N_x / 10)] = 1.
T = solve(N_t, T, k, h, dt, "Neumann")

# Plots
fig, ax = plt.subplots()
for i in range(0, N_t, int(N_t / 10)):
    ax.plot([h * i for i in range(N_x)], T[i], label = "t = %1.2f s" % (i * dt))
ax.set_xlabel("x (m)")
ax.set_ylabel("T (K)")
ax.set_title("Neumann")
ax.legend()

# New initial conditions
T = np.zeros((N_t, N_x)) + 300                                                  # K
T[0][0] = 330
T[0][-1] = 300
T = solve(N_t, T, k, h, dt, "Dirichlet")

# Plots
fig1, ax1 = plt.subplots()
for i in range(0, N_t, int(N_t / 5)):
    ax1.plot([h * i for i in range(N_x)], T[i], label = "t = %1.2f s" % (i * dt))
ax1.set_xlabel("x (m)")
ax1.set_ylabel("T (K)")
ax1.set_title("Dirichlet")
ax1.legend()

plt.show()
