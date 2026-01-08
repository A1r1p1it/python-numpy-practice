# ## Problem 1: Z-score Normalization ✓ Completed
# Create a 1D array of 50 random integers between 10 and 100.
# **Tasks:**
# - Compute the mean and standard deviation
# - Normalize the array to z-scores: (x - mean) / std
# - Count how many values have absolute z-score greater than 2
import numpy as np
arr = np.random.randint(10, 100, 50)
print("50 random int: ", arr, "/n")

mean_50 = np.mean(arr)
print("Mean of 50 arrays: ", mean_50, "\n")

median_50 = np.median(arr)
print("Median of array of 50: ", median_50, "\n")

z_scores = (arr - mean_50) / np.std(arr)
print("z-scores: ", z_scores[:10], "\n")

abs_zscore = np.abs(z_scores) > 2
total = np.sum(abs_zscore)
print(total)
