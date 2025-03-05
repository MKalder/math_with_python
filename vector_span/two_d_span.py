import numpy as np
import matplotlib.pyplot as plt

# Vectors
v1 = np.array([2, 1])
v2 = np.array([1, 3])

# Create a grid of combinations (alpha, beta)
alpha = np.linspace(-10, 10, 20)
beta = np.linspace(-10, 10, 20)

# Linear combinations
grid = np.array([a * v1 + b * v2 for a in alpha for b in beta])

# Plot
plt.figure(figsize=(10, 10))
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label='v1')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b', label='v2')
plt.scatter(grid[:, 0], grid[:, 1], s=2, alpha=0.5)

plt.xlim(-20, 20)
plt.ylim(-20, 20)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid()
plt.legend()
plt.title("Span of Two 2D Vectors")
plt.show()