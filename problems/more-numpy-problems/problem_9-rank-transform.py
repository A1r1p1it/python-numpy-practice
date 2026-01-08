## Problem 10: Rank Transform of an Array
# Create a 1D array of 20 random floats between 0 and 1.
# **Tasks:**
# - Compute the rank of each element (1 = smallest, 20 = largest)
# - Return an array of ranks aligned with the original elements
# - If there are ties, assign the average rank of the tied positions
import numpy as np
from scipy.stats import rankdata

arr = np.random.rand(20)
print("1D array of 20 random floats: \n", arr)

ranks = rankdata(arr, method='average')
print("Rank of each element: \n", ranks)
