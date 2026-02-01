from physics import hydrogen_wave_fn, a0
import numpy as np
import matplotlib.pyplot as plt

#define / choose quantum numbers
n = 4
l = 0
m = 0

#define probability density function
def prob_density(r, theta, phi):
    return np.abs(H_wave_fn(r,theta,phi))**2*r**2*np.sin(theta)

#normalisation check
norm_check, error = integrate.nquad(prob_density, [[0,100*a0], [0,np.pi], [0,2*np.pi]])
print(f'Normalisation Check: total probability = {norm_check}')

#Generate random sample in the box, evenly distributed throughout 3D space once operated on by the prob_density function
Npoints = 150000
r_rand = np.random.rand(Npoints) * 50 * a0
theta_rand = np.random.rand(Npoints) * np.pi
phi_rand = np.random.rand(Npoints) * 2*np.pi

#Compute probabilities for each point
p = prob_density(r_rand, theta_rand, phi_rand)

#Accept/reject sampling
p_max = p.max()
mask = np.random.rand(Npoints) < (p / p_max)

#Keep only accepted points
r_acc = r_rand[mask]
theta_acc = theta_rand[mask]
phi_acc = phi_rand[mask]

#convert to cartesian for plotting
x_plot = r_acc * np.sin(theta_acc) * np.cos(phi_acc)
y_plot = r_acc * np.sin(theta_acc) * np.sin(phi_acc)
z_plot = r_acc * np.cos(theta_acc)

#Plot
#create 3D space
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_box_aspect([1, 1, 1])
ax.set_xlabel("x ($a_0$)")
ax.set_ylabel("y ($a_0$)")
ax.set_zlabel("z ($a_0$)")

#scatter plot points
scale = 1/a0
ax.scatter(x_plot*scale, y_plot*scale, z_plot*scale, s=0.3, alpha = 0.10)

#label orbital
orbital_letters = ['s','p','d','f']
current_letter = orbital_letters[l]
ax.set_title(f"Hydrogen Orbital - {n}{current_letter}, m={m}")
plt.savefig(f"Hydrogen Orbital - {n}{current_letter}, m={m}", dpi=300)
plt.show()
