import numpy as np
import matplotlib.pyplot as plt

# Function for which we want to compute the roots
def f(x):
    return np.sqrt(x) - x - np.log(x + np.random.rand())

tolerance = 1e-5
interval = [0, 2.5]
counter = 0

# Bolzano theorem construction
if f(interval[0]) * f(interval[1]) < 0:
    diff = 1
    while np.abs(diff) > tolerance:
        counter += 1
        m = np.mean(interval)
        diff = f(m)
        if f(interval[0]) * diff < 0:
            interval = [interval[0], m]
        elif diff * f(interval[1]) < 0:
            interval = [m, interval[1]]
    print(m, diff, counter)
else:
    print("Method not appliable or no zeros in interval")

fig, ax = plt.subplots()

ax.plot(np.linspace(1e-3, 2, 1000), f(np.linspace(1e-3, 2, 1000)))
ax.hlines(0, 0, 2, linewidth = 0.5)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_xlim(0, 2)
plt.show()
