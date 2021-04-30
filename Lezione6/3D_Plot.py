import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

L = 1
Nx = 1000
Ny = 1000

x = np.linspace(- L, L, Nx)
y = np.linspace(- L, L, Ny)

X, Y = np.meshgrid(x, y)

z1 = np.sin(2 * np.pi * (X + Y))
z2 = np.sin(2 * np.pi * (X * Y))

fig1 = plt.figure()
ax3D1 = fig1.add_subplot(111, projection = "3d")
ax3D1.plot_wireframe(X, Y, z1)
ax3D1.set_xlabel("x")
ax3D1.set_ylabel("y")
ax3D1.set_zlabel("$\sin(2\pi(x + y))$")

fig2 = plt.figure()
ax3D2 = fig2.add_subplot(111, projection = "3d")
ax3D2.plot_wireframe(X, Y, z2, color = "red")
ax3D2.set_xlabel("x")
ax3D2.set_ylabel("y")
ax3D2.set_zlabel("$\sin(2\pi(x y))$")

plt.show()
