import matplotlib.pyplot as plt

# Setup
Nmax = 10                                                                       # Numer of terms to be summed
ratio = 0.1                                                                     # Ratio of the geometric series
ampl = 1                                                                        # Factor in front of series
exact = ampl / (1 - ratio)                                                      # Exact result of series

# Compute sum
differences = []
sum = 0
for i in range(Nmax):
    sum += ampl * ratio**i
    differences.append(exact - sum)

print("Sum = %g" % sum)
print("Perc. difference with exact value = %g" % ((exact - sum) / exact))

fig, ax = plt.subplots()
ax.plot(differences)
ax.set_ylabel("$S_N$")
ax.set_xlabel("N")
ax.set_yscale("log")

plt.show()
