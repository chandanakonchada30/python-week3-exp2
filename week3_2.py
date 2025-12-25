# #24331A05E2
# 2D array operations (indexing & slicing)
import numpy as np
matrix = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])
print("2D Array:\n", matrix)
print("\n***Indexing:***")
print(f"Element at Row 1, Col 2:",matrix[1, 2])
print(f"Top Left Element:",matrix[0, 0])
print("\n***Slicing:***")
print("First 2x2 Sub-matrix:\n",matrix[0:2, 0:2])
print("Entire Second Column:", matrix[:, 1])
print("Last Row:",matrix[-1, :])