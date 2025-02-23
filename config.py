L = 1.0
Nx = 50
dx = L / (Nx - 1)
T = 0.2
Nt = 1000
dt = T / Nt
alpha = 0.01

assert alpha * dt / dx**2 <= 0.5, "Choose smaller dt or larger dx for stability"
