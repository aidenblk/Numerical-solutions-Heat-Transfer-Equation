import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def plot_heat_distribution(u_all, L, Nx, dt, Nt):
    plt.figure(figsize=(10, 5))
    for i in range(0, Nt, Nt // 5):
        plt.plot(np.linspace(0, L, Nx), u_all[i], label=f"t={i*dt:.3f}s")

    plt.title("Heat Equation Simulation (Explicit Finite Difference)")
    plt.xlabel("Position (x)")
    plt.ylabel("Temperature (u)")
    plt.legend()
    plt.show()

def plot_heatmap_animation(u_all):
    fig, ax = plt.subplots()
    cax = ax.imshow(u_all[0], cmap="hot", interpolation="nearest", origin="lower")
    fig.colorbar(cax)

    def update(frame):
        cax.set_array(u_all[frame])
        ax.set_title(f"Time Step {frame}")

    ani = animation.FuncAnimation(fig, update, frames=len(u_all), repeat=False)
    plt.show()
