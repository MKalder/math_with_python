import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from three_d_model import ThreeDModel

# cube - 6 faces, 8 verticles(corners), 12 edges
vertices_cube = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [1, 1, 0],
                     [0, 1, 0],
                     [0, 0, 1],
                     [1, 0, 1],
                     [1, 1, 1],
                     [0, 1, 1]])

faces_cube = np.array([[0, 1, 2, 3],
                [4, 5, 6, 7],
                [0, 1, 5, 4],
                [2, 3, 7, 6],
                [1, 2, 6, 5],
                [0, 3, 7, 4]])

center_one = np.array([2, 2, 2])

cube_one = ThreeDModel(verticals=vertices_cube, faces=faces_cube, scale=3, center=center_one)
cube_two = ThreeDModel(verticals=vertices_cube, faces=faces_cube, scale=2)

# 
verticals_triangle = np.array([[0, 0, 0],
                               [1, 0, 0],
                               [0, 1, 0],
                               [1, 1, 0],
                               [0.5, 0.5, 1]])

faces_triangle = np.array([[0, 1, 4],
                           [1, 3, 4],
                           [0, 2, 4],
                           [2, 3, 4],])

triangle_one = ThreeDModel(verticals=verticals_triangle, faces=faces_triangle, center= [0.5,0.5,2])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.add_collection3d(Poly3DCollection(cube_one.verticals[cube_one.faces], alpha=0.5, linewidths=1, edgecolors='r', facecolors='green'))
ax.add_collection3d(Poly3DCollection(cube_two.verticals[cube_two.faces], alpha=0.5, linewidths=1, edgecolors='b', facecolors='orange'))
ax.add_collection3d(Poly3DCollection(triangle_one.verticals[triangle_one.faces], alpha=1.0, linewidths=1, edgecolors='g', facecolors='black'))
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('A 3D Cartesian Coordinate System')

plt.show()
