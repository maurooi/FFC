import numpy as np
import scipy.optimize as spo
import matplotlib.pyplot as plt

def linear_fit(x, A, B):
    return A * x + B

min, max = -1, 1
std = 0.1
x = np.linspace(min, max, 15)
y = linear_fit(x, -2, 3) + np.random.normal(loc = 0, scale = std, size = 15)
errors = std * np.ones(15)

fig, ax = plt.subplots()
ax.errorbar(x, y, yerr = errors, elinewidth = 1, linewidth = 0, marker = ".", label = "Data")
ax.set_xlabel("x")
ax.set_ylabel("y(x)")

p, cov = np.polyfit(x, y, 1, cov = True, w = 1 / errors)
label = "Fit, A = %1.2f$\pm$%1.4f, B = %1.2f$\pm$%1.4f" % (p[0], cov[0,0], p[1], cov[1,1])
ax.plot(x, linear_fit(x, p[0], p[1]), label = label)
ax.legend(fontsize = 7)
ax.set_title("Linear fit")

plt.show()

def non_linear_fit(t, A, tau, omega):
    return A * np.exp(- t / tau) * np.cos(omega * t)

min, max = 0, 10
Npoints = 100
T, std = 1, 0.05
t = np.linspace(min, max, Npoints)
y = non_linear_fit(t, 1, 3, 2 * np.pi / T) + np.random.normal(loc = 0, scale = std, size = Npoints)
errors = std * np.ones(Npoints)

fig1, ax1 = plt.subplots()
ax1.errorbar(t, y, yerr = errors, elinewidth = 1, linewidth = 0, marker = ".", label = "Data")
ax1.set_xlabel("t")
ax1.set_ylabel("y(t)")

p, cov = spo.curve_fit(non_linear_fit, t, y, p0 = [1, 3, 2 * np.pi / T], sigma = errors)
t_new = np.linspace(min, max, 1000)
ax1.plot(t_new, non_linear_fit(t_new, p[0], p[1], p[2]), label = "Fit")
ax1.legend()

plt.show()
