# Hydrogen Atom Wavefunction Visualizer

A Python-based tool to simulate and visualize electron probability densities using Monte Carlo sampling and 2D cross-sections.

## Features
* **3D Probability Cloud**: Uses rejection sampling to visualize the orbital as a 3D point cloud.
* **2D Density Slices**: High-resolution `pcolormesh` plots with logarithmic scaling to reveal radial and angular nodes.

## Visualizations
### 4s Orbital (n=4, l=0, m=0)
| 3D Monte Carlo | 2D Radial Slice |
| :---: | :---: |
| ![3D Plot](Hydrogen_Wavefunction.png) | ![2D Slice](Hydrogen_2D_Slice.png) |

## How it Works
The simulation solves the Schrödinger equation for the Hydrogen atom using:
* **Radial Part**: Generalized Laguerre polynomials.
* **Angular Part**: Spherical Harmonics.
