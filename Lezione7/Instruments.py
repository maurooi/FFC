import numpy as np
import scipy as scp
import matplotlib.pyplot as plt

f_piano = open("piano.txt", "r")

amplitudes = []
for amplitude in f_piano:
    amplitudes.append(int(amplitude))

print(len(amplitudes))

F_amplitudes = np.abs(scp.fft(amplitudes))**2

fig, ax = plt.subplots()
ax.plot(amplitudes)
ax.set_xlabel("t (A.U.)")
ax.set_ylabel("Amplitude (A.U.)")
ax.set_title("Piano")

fig1, ax1 = plt.subplots()
ax1.loglog(F_amplitudes, marker = ".", color = "k", linewidth = 0)
ax1.set_xlabel("$\omega$ (A.U.)")
ax1.set_ylabel("$|\mathcal{F}|^2(\omega)$")
ax1.set_title("Piano")

################################################################################

f_trumpet = open("trumpet.txt", "r")

amplitudes = []
for amplitude in f_trumpet:
    amplitudes.append(int(amplitude))

print(len(amplitudes))

F_amplitudes = np.abs(scp.fft(amplitudes))**2

fig2, ax2 = plt.subplots()
ax2.plot(amplitudes)
ax2.set_xlabel("t (A.U.)")
ax2.set_ylabel("Amplitude (A.U.)")
ax2.set_title("Trumpet")

fig3, ax3 = plt.subplots()
ax3.loglog(F_amplitudes, marker = ".", color = "k", linewidth = 0)
ax3.set_xlabel("$\omega$ (A.U.)")
ax3.set_ylabel("$|\mathcal{F}|^2(\omega)$")
ax3.set_title("Trumpet")

plt.show()
