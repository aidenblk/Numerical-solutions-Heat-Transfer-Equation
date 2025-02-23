# Numerical Solutions for the Heat Equation

## Overview
This project implements numerical solvers for the **1D and 2D heat equation** using **finite difference methods (FDM)**. It includes:
- **Explicit method (Euler forward)**
- **Implicit Crank-Nicolson method** (solving a tridiagonal system)
- **2D explicit solver** with animated heatmap visualization

The project demonstrates numerical stability, computational efficiency, and interactive visualization of heat diffusion.

## Features
 **Solves the heat equation in 1D and 2D**  
 **Explicit and implicit finite difference solvers**  
 **Tridiagonal solver for Crank-Nicolson method**  
 **Animated heatmap for 2D heat diffusion**  
 **Structured modular design for extensibility**  

##Heat Equation
![Heat Equation](https://latex.codecogs.com/png.latex?\frac{\partial%20u}{\partial%20t}=%20\alpha%20\frac{\partial^2%20u}{\partial%20x^2})


![Heat Equation](https://latex.codecogs.com/png.latex?\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2})









## Installation
Ensure you have Python **3.x** installed, then install dependencies:

```bash
pip install numpy matplotlib
```
Clone the repository:
```bash
git clone https://github.com/yourusername/numerical-heat-equation.git
cd numerical-heat-equation
```
Usage
run the scrpit and choose the solver:
```bash
python main.py
```
File Structure
```bash
numerical-heat-equation/
│── main.py              # Runs the simulation
│── solver.py            # Numerical solvers
│── visualize.py         # Plotting and animation
│── config.py            # Configuration parameters
│── README.md            # Project documentation
```
