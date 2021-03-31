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
N = 5000                                                                        # number of steps -> 1s of integration
l = 0.1                                                                         # m

# Initial conditions
theta0 = np.pi / 1.1                                                            # dimensionless
thetaDot0 = 0                                                                   # s**(-1)
theta = [theta0]                                                                # array of angular positions
thetaDot = [thetaDot0]                                                          # array of angular velocities
time = [0]
kinetic = [K(thetaDot0, l)]
potential = [V(theta0, l)]
totalE = [K(thetaDot0, l) + V(theta0, l)]

for i in range(N):
    # Update position and velocity
    newTheta = theta[i] + thetaDot[i] * tau + pendulum_eq(theta[i], l) * tau**2 / 2
    newThetaDot = thetaDot[i] + tau * (pendulum_eq(theta[i], l) + pendulum_eq(newTheta, l)) / 2
    # Append positions and velocities to lists
    theta.append(newTheta)
    thetaDot.append(newThetaDot)
    # Append times and energies to lists
    time.append(time[i] + tau)
    kinetic.append(K(newThetaDot, l))
    potential.append(V(newTheta, l))
    totalE.append(K(newThetaDot, l) + V(newTheta, l))

fig1, ax1 = plt.subplots()
ax1.plot(time, theta, label = "$\\theta$")
ax1.set_xlabel("$t\ (s)$")
ax1.set_ylabel("$\\theta(t)$")
ax1.set_title("Velocity Verlet - $\\theta$ and $\dot{\\theta}$")
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
ax3.set_title("Velocity Verlet - Energy")
ax3.legend()

fig3, ax4 = plt.subplots()
ax4.plot(theta, thetaDot)
ax4.set_xlabel("$\\theta$")
ax4.set_ylabel("$\dot{\\theta}$")
ax4.set_title("Velocity Verlet - Phase diagram")
# ax4.axis("equal")

plt.show()
