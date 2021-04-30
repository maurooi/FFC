import numpy as np
import matplotlib.pyplot as plt

k = 4                           # N / m
m = 1                           # kg
omega = 2                       # s**-1
tau = 1e-3                      # s
N_oscillators = 10              # Number of oscillators to be simulated
N_steps = 20000                 # Number of steps to be done

# Force on the i-th oscillator
def F(i, next_x, x, prev_x, F_ext):
    if i == 0:
        return k * (next_x - x) / m + F_ext
    if i == N_oscillators - 1:
        return k * (prev_x - x) / m + F_ext
    return k * (next_x - 2 * x + prev_x) / m + F_ext

# Make one step with velocity-Verlet
def step(x : list, v : list, F_ext : list, tau):
    x_list, v_list = [], []
    # x loop: each x needs to be computed before computing velocities
    for i in range(len(x)):
        prev_x, next_x = x[i - 1], x[(i + 1) % N_oscillators]
        new_x = x[i] + v[i] * tau + F(i, next_x, x[i], prev_x, F_ext[i]) * tau**2 / 2
        x_list.append(new_x)
    # v loop
    for i in range(len(x)):
        prev_x, next_x = x[i - 1], x[(i + 1) % N_oscillators]
        new_next_x, new_prev_x = x_list[i - 1], x_list[(i + 1) % N_oscillators]
        new_v = v[i] + (F(i, next_x, x[i], prev_x, F_ext[i]) + \
                F(i, next_x, x_list[i], prev_x, F_ext[i])) * tau / 2
        v_list.append(new_v)
    # Return x and v
    return x_list, v_list

def solve(x0, v0, tau, N_steps):
    factor = 1
    t_list, x_list, v_list = [0], [x0], [v0]
    F_ext = [0 for i in range(len(x0))]
    F_ext[0] = factor * 1
    for i in range(N_steps):
        t = t_list[i] + tau
        F_ext[0] = factor * np.cos(omega * t)
        x, v = step(x_list[i], v_list[i], F_ext, tau)
        t_list.append(t)
        x_list.append(x)
        v_list.append(v)
    return t_list, x_list, v_list

d = 0.1
x0 = [d * i for i in range(N_oscillators)]
v0 = [0 for i in range(N_oscillators)]

t, x, v = solve(x0, v0, tau, N_steps)

fig, ax = plt.subplots()
for j in range(N_oscillators):
    ax.plot(t, [x[i][j] + j for i in range(len(x))])
ax.set_xlabel("t (s)")
ax.set_ylabel("Amplitude (m)")

plt.show()
