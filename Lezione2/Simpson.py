import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

# Function to be integrated
def f(x, alpha):
    return np.exp(- alpha * x**2)

def simpson(x, y):
    h = np.abs(x[1] - x[0])
    return h * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2])) / 3

# Actual integration with the Simpson rule
interval = [-1, 1]
alpha = 1
N = 10000
x = np.linspace(interval[0], interval[1], N + 1)
y = f(x, alpha)
I = simpson(x, y)
exact = sp.erf(interval[1]) * np.sqrt(np.pi)

print("Exact: ", exact)
print("Numerical: ", I)
print("Error: ", exact - I)
