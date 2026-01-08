## Problem 2: Top-k Using Sorting 
# Create a 1D array of 30 random integers between 1 and 500.
# **Tasks:**
# - Find the 5 largest values WITHOUT using `np.sort` on the full
# array
# - Hint: Use `np.argpartition()`
# - Return them sorted in descending order
# - Also return their original indices
import numpy as np
arr = np.random.randint(1, 500, 30)
print("30 random integers: ", arr, "\n")

indices = np.argpartition(arr, -5)[-5:]
print("Indices of the largest 5 :", indices)

largest_5 = arr[indices]
print("5 largest value: ", largest_5)

sorting_order = np.sort(largest_5)[::-1]
print("Descending order of the 5 largest numbers: ", sorting_order)

orginal_indices = indices[np.argsort(largest_5)[::-1]]
print("og indices in descending order: ", orginal_indices)

