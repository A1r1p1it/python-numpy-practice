## Problem 9: Conditional Replacement with Two Masks
# Create a 2D array of shape (8, 8) with random integers between -10
# and 10.
# **Tasks:**
# - Replace all negative values with their absolute value ONLY if they
# are on even rows (rows 0, 2, 4, 6)
# - Replace all values greater than 5 with 5 ONLY on odd rows (rows 1,
# 3, 5, 7)
# - Keep everything else unchanged
import numpy as np

arr = np.random.randint(-10, 11, (8, 8))
print("2D array of shape (8, 8): \n", arr)

even_rows_mask = arr[::2] < 0
arr[::2][even_rows_mask] = np.abs(arr[::2][even_rows_mask])
print("After even rows negative → absolute:\n", arr)

odd_rows_mask = arr[1::2] > 5
arr[1::2][odd_rows_mask] = 5
print("After odd rows >5 → 5:\n", arr)


