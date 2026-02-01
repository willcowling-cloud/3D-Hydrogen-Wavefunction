from physics import hydrogen_wave_fn, a0
import numpy as np
import matplotlib.pyplot as plt

#create 2D meshgrid
x_range = np.linspace(-a0*100,a0*100,400)
z_range = np.linspace(-a0*100,a0*100,400)
X,Z = np.meshgrid(x_range,z_range)
#Using polar coordinates
r = np.sqrt(X**2 + Z**2)
theta = np.arccos(Z/(r+1e-15))
#set phi = 0 
phi = np.zeros_like(X)
scale = 1/a0

#Define 2D probability density function
#note we dont need the jacobian here as we are no longer changing coordinate system as we sample
def prob_density2D(r, theta, phi):
    return np.abs(H_wave_fn(r,theta,phi))**2


Prob_grid = prob_density2D(r,theta,phi)
log_grid = np.log10(Prob_grid)


#Plot
fig2 = plt.figure(figsize=(10, 8))
ax2 = fig2.add_subplot()

#Using a heat map to show probability density 
im = ax2.pcolormesh(X*scale, Z*scale, log_grid, 
                    shading='auto', 
                    cmap='magma',
                    vmin=log_grid.max()-10, # Only show the top 10 orders of magnitude, allowing the less dense regions to be shown
                    vmax=log_grid.max())
plt.colorbar(im, label='Log10 Probability Density')

#Label axis and orbital
plt.xlabel("x ($a_0$)")
plt.ylabel("z ($a_0$)")
ax2.set_title(f"Hydrogen 2D Slice - {n}{current_letter}, m={m}")
plt.savefig(f"Hydrogen 2D Slice - {n}{current_letter}, m={m}", dpi=300)
plt.show()
print(f"Max density: {Prob_grid.max()}")
