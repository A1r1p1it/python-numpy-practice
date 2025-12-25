### Problem 1: Random Number Statistics
# Create a 1D array of 100 random integers between 1-50. Find:
# - Mean, median, and standard deviation
# - How many numbers are above the mean
# - The index of the maximum value


import numpy as np
a = np.random.randint(1, 51, size = 100)

rand_mean = np.mean(a)
rand_median = np.median(a)
rand_std = np.std(a)

print("Mean: ", rand_mean)
print("Median: ", rand_median)
print("Standard deviation: ", rand_std, "\n")

b = print("Numbers above mean: ", a[a > rand_mean], "\n")
c = np.argmax(a)
print("Index value of max value: ", c)
