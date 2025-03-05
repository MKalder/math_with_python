from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# Vectors
v1 = np.array([1, 2, 0])
v2 = np.array([0, 1, 3])

# Alpha and Beta combinations
alpha = np.linspace(-10, 10, 10)
beta = np.linspace(-10, 10, 10)

# Meshgrid for combinations
A, B = np.meshgrid(alpha, beta)
grid = np.array([A.ravel(), B.ravel()])

# Linear combinations
points = grid.T @ np.vstack([v1, v2])

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', label='v1')
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='b', label='v2')
ax.scatter(points[:, 0], points[:, 1], points[:, 2], alpha=0.3, s=2)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Span of Two 3D Vectors")
ax.legend()
plt.show()