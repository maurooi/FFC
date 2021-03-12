import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

N = 10000                                                                       # Number of points to be generated
np.random.seed()                                                                # Set seed for random generator
x_list = []                                                                     # List containing all random x coordinates
y_list = []                                                                     # List containing all random y coordinates
n = 0                                                                           # Number of points inside circle
x_circle = np.linspace(0, 1, 1000)
y_circle = np.sqrt(1 - x_circle**2)

# Actual point generation
for i in range(N):
    x = np.random.rand()
    y = np.random.rand()
    r = np.sqrt(x**2 + y**2)
    # Append points to lists
    x_list.append(x)
    y_list.append(y)

    # Check if r < 1 (point inside circle)
    if r < 1:
        n += 1

print("pi = %g" % (4 * n / N))

fig, ax = plt.subplots()

ax.plot(x_list, y_list, marker = ".", linewidth = 0, markersize = 1)
ax.plot(x_circle, y_circle)
ax.add_patch(patches.Rectangle((0, 0), 1, 1, linewidth = 1, edgecolor = 'r', facecolor = 'none'))
ax.set_xlabel("x (A. U.)")
ax.set_ylabel("y (A. U.)")
ax.axis("equal")

plt.show()
