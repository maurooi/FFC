import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import Boltzmann
import vec2d as v2d

mass_of_argon = 39.948 # amu

def lj_force(r, epsilon, sigma):
    mod = r.mod()
    return 48 * epsilon * np.power(
        sigma, 12) / np.power(
        mod, 13) - 24 * epsilon * np.power(
        sigma, 6) / np.power(mod, 7)

def init_velocity(T, number_of_particles):
    R1 = np.random.rand(number_of_particles) - 0.5
    R2 = np.random.rand(number_of_particles) - 0.5
    vel_list = [np.sqrt(Boltzmann * T / (mass_of_argon * 1.602e-19)) * v2d.vec2d(R1[i], R2[i])\
                for i in range(number_of_particles)]
    return  np.array(vel_list)

def get_accelerations(positions):
    accel = np.full((positions.size, positions.size), v2d.vec2d(0, 0))
    for i in range(0, positions.size - 1):
        for j in range(i + 1, positions.size):
            r = positions[j] - positions[i]
            rmag = r.mod()
            force_scalar = lj_force(r, 0.0103, 3.4)
            force = force_scalar * r / rmag
            accel[i, j] = force / mass_of_argon
            accel[j, i] = - force / mass_of_argon
    return np.sum(accel, axis=0)

def update_pos(r, v, a, dt):
    return r + v * dt + 0.5 * a * dt * dt

def update_velo(v, a, a1, dt):
    return v + 0.5 * (a + a1) * dt

def run_md(dt, number_of_steps, initial_temp, r):
    positions = np.full((number_of_steps, 3), v2d.vec2d(0, 0))
    v = init_velocity(initial_temp, 3)
    a = get_accelerations(r)
    for i in range(number_of_steps):
        r = update_pos(r, v, a, dt)
        a1 = get_accelerations(r)
        v = update_velo(v, a, a1, dt)
        a = np.array(a1)
        positions[i, :] = r
    return positions

x = np.array([v2d.vec2d(1, 0), v2d.vec2d(5, 0), v2d.vec2d(10, 0)])
sim_pos = run_md(0.1, 10, 300, x)
dt = 0.1

for i in range(sim_pos.shape[1]):
    x_coord = [sim_pos[j, i].x for j in range(len(sim_pos[:, i]))]
    plt.plot(x_coord, '.', label='atom {}'.format(i))
plt.xlabel("Step")
plt.ylabel("Position (Angstrom)")
plt.legend()

plt.show()
