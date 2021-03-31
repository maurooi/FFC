import numpy as np
import matplotlib.pyplot as plt
from VV_solver import VV_solver

def F(theta):
    l = 0.1
    g = 9.81
    return - g * np.sin(theta) / l

def K(theta):
    l = 0.1
    return l**2 * theta**2 / 2

def V(theta):
    l = 0.1
    g = 9.81
    return - g * l * np.cos(theta) + g * l

theta0 = np.pi / 10
thetaDot0 = 0

N = 1000
tau = 1e-3

vv = VV_solver(F, tau)

time, theta, thetaDot = vv.solve(N, theta0, thetaDot0)
kinetic, potential = [K(thetaDot[i]) for i in range(len(time))], [V(theta[i]) for i in range(len(time))]
totalE = [kinetic[i] + potential[i] for i in range(len(time))]

# Plots
fig1, ax1 = plt.subplots()
ax1.plot(time, theta, label = "$\\theta$")
ax1.set_xlabel("$t\ (s)$")
ax1.set_ylabel("$\\theta(t)$")
ax1.set_title("velocity Verlet - $\\theta$ and $\dot{\\theta}$")
ax1.legend(loc = 1)

ax2 = ax1.twinx()
ax2.plot(time, thetaDot, label = "$\dot{\\theta}$", color = "red")
ax2.set_ylabel("$\dot{\\theta}(t)\ (s^{-1})$")
ax2.legend(loc = 2)

fig2, ax3 = plt.subplots()
ax3.plot(time, kinetic, label = "$K$")
ax3.plot(time, potential, label = "$V$")
ax3.plot(time, totalE, label = "$E_{tot}$")
ax3.set_ylabel("$E\ (J)$")
ax3.set_xlabel("$t\ (s)$")
ax1.set_title("Velocity Verlet - Energy")
ax3.legend()

plt.show()

plt.show()
