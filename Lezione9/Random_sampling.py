import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, alpha = 1):
    return np.exp(- alpha * x * x)

# Returns uniformly distributed numbers between min and max
def rand_range(min, max, n = 1):
    return (max - min) * np.random.rand(n) + min

# Integrates with MC method the function f(x) over the range [min, max) taking
# n_samples points
def MC_integration(f, min, max, n_samples = 1000):
    randoms = rand_range(min, max, n_samples)
    y = f(randoms)
    volume = max - min
    return np.mean(y) * volume, randoms

np.random.seed()
n_samples = 100
f = lambda x: gaussian(x, 5)
min, max = -1, 1
integral, randoms = MC_integration(f, min, max, n_samples)

print("1 / sqrt(N) = ", 1 / np.sqrt(n_samples))
print("Integral = ", integral)

fig, ax = plt.subplots()
x = np.linspace(min, max, n_samples)
ax.plot(x, f(x), color = "r", label = "Function")
ax.plot(randoms, np.zeros(n_samples), linewidth = 0, marker = ".", markersize = 1, label = "Random sampling")

plt.show()
