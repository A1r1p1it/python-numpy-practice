### Problem 6: Array Transformation
# - Create a 1D array with numbers 1-24
# - Reshape it to 4×6
# - Reshape it to 2×3×4
# - Print the shape at each step
import numpy as np


arr = np.arange(1, 25)
print("1D array:\n", arr)
print("Shape:", arr.shape, "\n")


array_4x6 = arr.reshape(4, 6)
print("Reshaped to 4x6:\n", array_4x6)
print("Shape:", array_4x6.shape, "\n")

array_2x3x4 = arr.reshape(2, 3, 4)
print("Reshaped to 2x3x4:\n", array_2x3x4)
print("Shape:", array_2x3x4.shape)
