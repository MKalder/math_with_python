import numpy as np
from scipy.linalg import lu

A = np.array([[2, 3, 1], [4, 1, 2], [3, 2, 1]])

# LU-Decomposition
P, L, U = lu(A)
det = np.prod(np.diag(U))

print("Matrix A:")
print(A)
print("\nL:")
print(L)
print("\nU:")
print(U)
print(f"\nDeterminante: {det:.2f}")