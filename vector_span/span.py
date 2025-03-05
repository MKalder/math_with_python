from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# Define Vectors
v1 = np.array([1, 2, 0])  # First vector
v2 = np.array([0, 1, 3])  # Second vector

# Create a grid of coefficients (alpha, beta)
alpha = np.linspace(-10, 10, 20)  # Range for alpha
beta = np.linspace(-10, 10, 20)   # Range for beta
A, B = np.meshgrid(alpha, beta)

# Generate the plane points: alpha * v1 + beta * v2
X = A * v1[0] + B * v2[0]
Y = A * v1[1] + B * v2[1]
Z = A * v1[2] + B * v2[2]

# Plot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the plane surface
ax.plot_surface(X, Y, Z, alpha=0.5, color='cyan', edgecolor='k', linewidth=0.2)

# Plot the original vectors
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', linewidth=2, label='v1')
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='b', linewidth=2, label='v2')

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Plane spanned by v1 and v2")
ax.legend()
plt.show()