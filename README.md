# Hydrogen Atom Wavefunction Visualizer

This Python code creates a Monte Carlo simulation using a Rejection Sampling algorithm to map the electron probability cloud for the Hydrogen atom, given the chosen quantum numbers. 

## Features
* **3D Probability Cloud**: Uses rejection sampling to visualize the electron density for different Hydrogen orbitals.
* **2D Density Slices**: Shows radial and angular nodes using a 'pcolourmesh' and lotharithmic scaling.

## Visualizations
### 4s Orbital (n=4, l=0, m=0)
| 3D Monte Carlo | 2D Radial Slice |
| :---: | :---: |
| ![3D Plot](Hydrogen_Wavefunction.png) | ![2D Slice](Hydrogen_2D_Slice.png) |

## How it Works
The simulation solves the Schrödinger equation for the Hydrogen atom using:
* **Radial Part**: Generalized Laguerre polynomials.
* **Angular Part**: Spherical Harmonics.
