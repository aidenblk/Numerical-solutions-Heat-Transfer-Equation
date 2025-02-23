import numpy as np
from config import alpha, dt, dx, Nx, Nt

def explicit_fdm(initial_condition):
    u = initial_condition.copy()
    u_all = [u.copy()]

    for _ in range(Nt):
        u_new = u.copy()
        for i in range(1, Nx-1):
            u_new[i] = u[i] + alpha * dt / dx**2 * (u[i+1] - 2*u[i] + u[i-1])
        
        u = u_new.copy()
        u_all.append(u.copy())

    return u_all

def crank_nicolson_fdm(initial_condition):
    u = initial_condition.copy()
    u_all = [u.copy()]

    r = alpha * dt / (2 * dx**2)
    
    A = np.diag((1 + 2*r) * np.ones(Nx-2)) + \
        np.diag(-r * np.ones(Nx-3), k=1) + \
        np.diag(-r * np.ones(Nx-3), k=-1)

    for _ in range(Nt):
        b = u[1:-1] + r * (u[:-2] - 2*u[1:-1] + u[2:])
        u_new = u.copy()
        u_new[1:-1] = np.linalg.solve(A, b)
        u = u_new.copy()
        u_all.append(u.copy())

    return u_all

def explicit_fdm_2d(initial_condition, Nx, Ny, dx, dy, dt, alpha, Nt):
    u = initial_condition.copy()
    u_all = [u.copy()]

    r_x = alpha * dt / dx**2
    r_y = alpha * dt / dy**2

    for _ in range(Nt):
        u_new = u.copy()
        for i in range(1, Nx-1):
            for j in range(1, Ny-1):
                u_new[i, j] = u[i, j] + r_x * (u[i+1, j] - 2*u[i, j] + u[i-1, j]) + r_y * (u[i, j+1] - 2*u[i, j] + u[i, j-1])
        
        u = u_new.copy()
        u_all.append(u.copy())

    return u_all
