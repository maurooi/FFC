import matplotlib.pyplot as plt
import numpy as np

def pendulum_eq(theta, l):
    g = 9.81 # m/s**2
    return - g * np.sin(theta) / l

def K(thetaDot, l):
    return l**2 * thetaDot**2 / 2

def V(theta, l):
    g = 9.81 # m/s**2
    return - g * l * np.cos(theta) + g * l

# Useful constants
tau = 1e-3                                                                      # s
N = 1000                                                                        # number of steps -> 1s of integration
l = 0.1                                                                         # m

# Initial conditions
theta0 = np.pi - 0.1                                                             # dimensionless
thetaDot0 = 0                                                                   # s**(-2)
theta = [theta0]                                                                # array of angular positions
thetaDot = [thetaDot0]                                                          # array of angular velocities
time = [0]
kinetic = [K(thetaDot0, l)]
potential = [V(theta0, l)]
totalE = [K(thetaDot0, l) + V(theta0, l)]

for i in range(N):
    # Update positions and velocities
    newTheta = theta[i] + tau * thetaDot[i]
    newThetaDot = thetaDot[i] + tau * pendulum_eq(theta[i], l)
    # Append positions and velocities to lists
    theta.append(newTheta)
    thetaDot.append(newThetaDot)
    # Append times and energies to lists
    time.append(time[i] + tau)
    kinetic.append(K(thetaDot[i], l))
    potential.append(V(theta[i], l))
    totalE.append(K(thetaDot[i], l) + V(theta[i], l))

fig1, ax1 = plt.subplots()
ax1.plot(time, theta, label = "$\\theta$")
ax1.set_xlabel("$t\ (s)$")
ax1.set_ylabel("$\\theta(t)$")
ax1.legend(loc = 1)
ax1.set_title("Euler - $\\theta$ and $\dot{\\theta}$")

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
ax3.set_title("Euler - Energy")
ax3.legend()

plt.show()
