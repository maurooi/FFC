import numpy as np
import matplotlib.pyplot as plt

# Function that generates random integers in the range [0, M)
def rand_gen(a, c, M, r0, n = 1):
    r = r0
    if n == 1:
        return (a * r + c) % M
    rand_list = []
    for i in range(n):
        r = (a * r + c) % M
        rand_list.append(r / float(M))
    return rand_list

a, c, M, r0, n = 5, 8, 104729, 9, 100000
rand_list = rand_gen(a, c, M, r0, n)

fig, ax = plt.subplots()
ax.plot(rand_list, marker = ".", linewidth = 0)

fig1, ax1 = plt.subplots()
ax1.hist(rand_list, histtype = "step", bins = 30)

plt.show()
