import numpy as np
import math
from scipy.special import genlaguerre, sph_harm

#define constants
z_atomic = 1
a0  = 5.29177e-11

#define Spherical Harmonics
def Spherical_Harmonics(phi,theta):
    return sph_harm(m,l,phi,theta)

#define Radial Eqn solutions
def Radial_sol(r):
    rho = (2*z_atomic*r)/(a0*n)
    G_nl = genlaguerre(n-l-1,2*l+1)(rho)
    normalisation = np.sqrt( ((2*z_atomic)/(n*a0))**3 * math.factorial(n-l-1) / (2*n * math.factorial(n+l)) )
    return normalisation*np.exp(-rho/2)*(rho)**l*G_nl

#define wave function
def H_wave_fn(r,theta,phi):
  return Radial_sol(r)*Spherical_Harmonics(phi,theta)
