# Hydrogen Atom Wavefunction Visualizer

This Python code creates a Monte Carlo simulation using a Rejection Sampling algorithm to map the electron probability density for the Hydrogen atom, given the chosen quantum numbers n,l,m. 

## Features
* **3D Probability Cloud**: Uses rejection sampling to visualize the electron density for different Hydrogen orbitals.
* **2D Density Slices**: Shows radial and angular nodes using a 'pcolourmesh' and lotharithmic scaling.

## Visualizations

### 2s Orbital (n=2, l=0, m=0)
| 3D Monte Carlo Cloud | 2D Density Slice (y=0) |
| :---: | :---: |
| <img src="images/Hydrogen%20Orbital%20-%202s,%20m=0.png" width="400"> | <img src="images/Hydrogen%202D%20Slice%20-%202s,%20m=0.png" width="400"> |

---

### 2p Orbital (n=2, l=1, m=0)
| 3D Monte Carlo Cloud | 2D Density Slice (y=0) |
| :---: | :---: |
| <img src="images/Hydrogen%20Orbital%20-%202p,%20m=0.png" width="400"> | <img src="images/Hydrogen%202D%20Slice%20-%202p,%20m=0.png" width="400"> |

---

### 4s Orbital (n=4, l=0, m=0)
| 3D Monte Carlo Cloud | 2D Density Slice (y=0) |
| :---: | :---: |
| <img src="images/Hydrogen%20Orbital%20-%204s,%20m=0.png" width="400"> | <img src="images/Hydrogen%202D%20Slice%20-%204s,%20m=0.png" width="400"> |

## How it Works
First we solve the Schrödinger equation in 3D for the Hydrogen atom:
* **Radial Part**: Using Generalized Laguerre polynomials imported from the scipy library.
* **Angular Part**: Using Spherical Harmonics also using the scipy library
Next we create the Probability Density Function (PDF) of the wavefunction, and use this to calculate the probability of the electron being at generated random points.
*If the probability of a point is insufficient, it is rejected.
*Plotting many accepted points builds the visualisation of the electron density cloud

**2D Slice**: Using an adapted version of the 3D PDF we are able to plot the wavefunction in 2D. This allows us to:
* Visulualise nodes more clearly
* Create a heat map to represent the dense reigons of high probability 


## Problems I faced along the way
* **Classical Orthogonal Polynomials**: At first I was 'hard coding' the results of the Associated Laguerre and Legendre into a function. This restricted the orbitals that could be shown to low values of n, and the code would break for certain values of n. In fixing this I learned the importance of using built in python libraries for such mathematical functions. Using the scipy library to create the required polynomials both increased the speed of the code and allowed orbitals of all n values to be visualised.  
* **Normalising the Wavefunction**: It was proving extremely difficult at first to prove that the PDF was normalised. This was due to the values of the PDF being of the order 10e-30 or smaller, resulting in floating point underflow. I solved this by representing the spacial coordinates in units of Bohr radii (a0).
* **Logarithmic Heat Scale Map**: Fitting all probabilities on a single heat map was impossible due to the huge variations in orders of magnitude across the spatial grid. At first I thought I would have to remove all points below a certain probability. However, If I used a logarithmic scale then compresses the range, also allowing nodes to be visualised
