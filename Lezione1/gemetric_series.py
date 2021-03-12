# Setup
Nmax = 10                                                                       # Numer of terms to be summed
ratio = 0.1                                                                     # Ratio of the geometric series
ampl = 1                                                                        # Factor in front of series
exact = ampl / (1 - ratio)                                                      # Exact result of series

# Compute sum
sum = 0
for i in range(Nmax):
    sum += ampl * ratio**i

print("Sum = %g" % sum)
print("Perc. difference with exact value = %g" % ((exact - sum) / exact))
