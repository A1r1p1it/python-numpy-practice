## Problem 8: Sliding Window Sum

# Create a 1D array of 30 random integers between 1 and 10.
# **Tasks:**
# - Compute the sum of every sliding window of size 5
# - That means: sums of arr[0:5], arr[1:6], arr[2:7], ..., arr[25:30]
# - Do it using vectorized operations (NO Python for loop over
# windows)
arr = np.random.randint(1, 11, 30)
print("1D array of 30 random integers between 1 and 10: \n", arr)

sliding = [np.sum(arr[i: i + 5]) for i in range(26)]
print("sum of every sliding window: \n", sliding)
print(len(sliding))
