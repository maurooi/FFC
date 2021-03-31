import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

# Function to be integrated
def f(x):
    return x**4 - 2 * x + 1

def trap(x, y):
    h = np.abs(x[1] - x[0])
    return h * (y[0] + y[-1]) / 2 + np.sum(h * y[1:-1])

def simpson(x, y):
    h = np.abs(x[1] - x[0])
    return h * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2])) / 3

# Actual integration with the Simpson rule
interval = [-1, 1]
alpha = 1
N_list = range(10, 10000, 10)
diff_trap = []
diff_simp = []

for N in N_list:
    x = np.linspace(interval[0], interval[1], N + 1)
    y = f(x)
    exact = (x**5 / 5 - x**2 + x)[-1] - (x**5 / 5 - x**2 + x)[0]
    diff_trap.append(np.abs(exact - trap(x, y)))
    diff_simp.append(np.abs(exact - simpson(x, y)))

fig, ax = plt.subplots()
ax.loglog(N_list, diff_trap, label = "Trapezoids")
ax.loglog(N_list, diff_simp, label = "Simpson")
ax.set_xlabel("$N$")
ax.set_ylabel("$I$")
ax.legend()

plt.show()
