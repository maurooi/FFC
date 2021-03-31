import numpy as np
import scipy.integrate as int
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

m1 = 1.0
m2 = 1.0
l1 = 0.2
l2 = 0.1
g = 9.81

def F1(theta, omega):
    t1, t2 = theta[0], theta[1]
    o1, o2 = omega[0], omega[1]
    return -(g * (2 * m1 + m2) * np.sin(t1) + g * m2 * np.sin(t1 - 2 * t2) + l1 * m2 * np.sin(2 * (t1 - t2)) * o1**2 + 2 * l2 * m2 * np.sin(t1 - t2) * o2**2)/\
            (2 * l1 * (m1 + m2 - m2 * np.cos(t1 - t2)**2))

def F2(theta, omega):
    t1, t2 = theta[0], theta[1]
    o1, o2 = omega[0], omega[1]
    return (np.sin(t1 - t2) * (g * (m1 + m2) * np.cos(t1) + l1 * (m1 + m2) * o1**2 + l2 * m2 * np.cos(t1 - t2) * o2**2))/(l2 * (m1 + m2 - m2 * np.cos(t1 - t2)**2))

def f(t, y : list):
    return y[1], F1([y[0], y[2]], [y[1], y[3]]), y[3], F2([y[0], y[2]], [y[1], y[3]])

def animation1(frame, y, integrator, arts):
    integrator.step()
    y.append(integrator.y)
    art1, art2, art3 = arts
    if len(integrator.y) >= 100:
        x1 = l1 * np.sin(y[-99:][0])
        x2 = l2 * np.sin(y[-99:][2]) + x1
        y1 = - l1 * np.cos(y[-99:][0])
        y2 = - l2 * np.cos(y[-99:][2]) + y1
    else:
        t1 = np.array([y[i][0] for i in range(len(y))])
        t2 = np.array([y[i][2] for i in range(len(y))])
        x1 = l1 * np.sin(t1)
        x2 = l2 * np.sin(t2) + x1
        y1 = - l1 * np.cos(t1)
        y2 = - l2 * np.cos(t2) + y1
    art1.set_data(x2, y2)
    art2.set_data([0, x1[-1]], [0, y1[-1]])
    art3.set_data([x1[-1], x2[-1]], [y1[-1], y2[-1]])
    return art1, art2, art3

np.random.seed()
initial_conditions = np.pi * np.random.rand(4)
y = [initial_conditions]

integrator = int.RK45(f, 0, initial_conditions, t_bound = np.inf, max_step = 1e-2)
t1 = np.array([y[i][0] for i in range(len(y))])
t2 = np.array([y[i][2] for i in range(len(y))])
x1 = l1 * np.sin(t1)
x2 = l2 * np.sin(t2) + x1
y1 = - l1 * np.cos(t1)
y2 = - l2 * np.cos(t2) + y1

fig1, ax1 = plt.subplots()
art1, = ax1.plot(x2, y2, color = "k", linewidth = 0.1)
art2, = ax1.plot([0, x1[-1]], [0, y1[-1]], color = "r", linewidth = 1)
art3, = ax1.plot([x1[-1], x2[-1]], [y1[-1], y2[-1]], color = "b", linewidth = 1)
arts = (art1, art2, art3)
ax1.set_xlim(- l1 - l2 - 0.1 * l1, l1 + l2 + 0.1 * l1)
ax1.set_ylim(- l1 - l2 - 0.1 * l1, + l1 + l2 + 0.1 * l1)
ax1.set_xlabel("x (m)")
ax1.set_ylabel("y (m)")
#ax1.axis("equal")
FuncAnimation(fig1, animation1, fargs = (y, integrator, arts), interval = 30, blit = True)

plt.show()
