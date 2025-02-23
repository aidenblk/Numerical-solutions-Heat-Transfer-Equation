import numpy as np
from solver import explicit_fdm, crank_nicolson_fdm, explicit_fdm_2d
from visualize import plot_heat_distribution
from config import L, Nx, dt, Nt, alpha

# User chooses solver
solver_type = input("Choose solver: (1) Explicit 1D, (2) Crank-Nicolson 1D, (3) Explicit 2D: ")

if solver_type == "1":
    # 1D Explicit Solver
    u_initial = np.zeros(Nx)
    u_initial[int(Nx/4):int(3*Nx/4)] = 1  # Heat pulse in the middle
    u_all = explicit_fdm(u_initial)
    plot_heat_distribution(u_all, L, Nx, dt, Nt)

elif solver_type == "2":
    # 1D Crank-Nicolson Solver
    u_initial = np.zeros(Nx)
    u_initial[int(Nx/4):int(3*Nx/4)] = 1
    u_all = crank_nicolson_fdm(u_initial)
    plot_heat_distribution(u_all, L, Nx, dt, Nt)

elif solver_type == "3":
    # 2D Explicit Solver
    Ny = Nx  # Square domain
    dx = dy = L / (Nx - 1)
    u_initial = np.zeros((Nx, Ny))
    u_initial[Nx//4:3*Nx//4, Ny//4:3*Ny//4] = 1  # Initial heat pulse
    u_all = explicit_fdm_2d(u_initial, Nx, Ny, dx, dy, dt, alpha, Nt)

    # Plot heatmap animation (new function in `visualize.py`)
    from visualize import plot_heatmap_animation
    plot_heatmap_animation(u_all)


