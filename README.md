# Hydrogen Atom Wavefunction Visualizer

This Python code creates a Monte Carlo simulation using a Rejection Sampling algorithm to map the electron probability cloud for the Hydrogen atom, given the chosen quantum numbers. 

## Features
* **3D Probability Cloud**: Uses rejection sampling to visualize the electron density for different Hydrogen orbitals.
* **2D Density Slices**: Shows radial and angular nodes using a 'pcolourmesh' and lotharithmic scaling.

## Visualizations

### 2s Orbital (n=2, l=0, m=0)
The $2s$ orbital is spherically symmetric and contains one radial node.

| 3D Monte Carlo Cloud | 2D Density Slice (y=0) |
| :---: | :---: |
| ![2s 3D](Hydrogen%20Orbital%20-%202s,%20m=0.png) | ![2s 2D](Hydrogen%202D%20Slice%20-%202s,%20m=0.png) |

---

### 2p Orbital (n=2, l=1, m=0)
The $2p$ orbital ($m=0$) exhibits the classic "dumbbell" shape pointing along the Z-axis, with an angular node at the XY-plane.

| 3D Monte Carlo Cloud | 2D Density Slice (y=0) |
| :---: | :---: |
| ![2p 3D](Hydrogen%20Orbital%20-%202p,%20m=0.png) | ![2p 2D](Hydrogen%202D%20Slice%20-%202p,%20m=0.png) |

---

### 4s Orbital (n=4, l=0, m=0)
A higher energy state showing significantly more complex radial structure. Notice the three distinct radial nodes visible in the 2D slice.

| 3D Monte Carlo Cloud | 2D Density Slice (y=0) |
| :---: | :---: |
| ![4s 3D](Hydrogen%20Orbital%20-%204s,%20m=0.png) | ![4s 2D](Hydrogen%202D%20Slice%20-%204s,%20m=0.png) |

## How it Works
The simulation solves the Schrödinger equation for the Hydrogen atom using:
* **Radial Part**: Generalized Laguerre polynomials.
* **Angular Part**: Spherical Harmonics.
