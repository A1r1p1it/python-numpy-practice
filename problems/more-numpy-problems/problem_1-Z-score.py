# ## Problem 1: Z-score Normalization ✓ Completed
# Create a 1D array of 50 random integers between 10 and 100.
# **Tasks:**
# - Compute the mean and standard deviation
# - Normalize the array to z-scores: (x - mean) / std
# - Count how many values have absolute z-score greater than 2
import numpy as np
import pandas as pd
arr = np.random.randint(10, 100, 50)
print("50 random integers: ", arr, "\n")

mean_a = np.mean(arr)
print("Mean of the array: ",mean_a, "\n")

std_a = np.std(arr)
print("Standard deviation of the array: ", std_a, "\n")

z_scores = (arr - mean_a) / std_a
vert_ical = np.vstack((z_scores))
print("z-scored: ", vert_ical[:10], "\n")

great_er = np.abs(z_scores) > 2
great_er
add_ing = np.sum(great_er)
print(add_ing)
