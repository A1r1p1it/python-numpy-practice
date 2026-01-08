## Problem 2: Top-k Using Sorting 
# Create a 1D array of 30 random integers between 1 and 500.
# **Tasks:**
# - Find the 5 largest values WITHOUT using `np.sort` on the full
# array
# - Hint: Use `np.argpartition()`
# - Return them sorted in descending order
# - Also return their original indices
arr = np.random.randint(1, 500, 30)
print("30 random in: ", arr, "\n")

indices = np.argpartition(arr, -5)[-5:]
print("Indices of the last 5 values: ", indices, "\n")

largest_5 = arr[indices]
print("5 largest numbers: ", largest_5, "\n")

sorting_order = np.sort(largest_5)[::-1]
print("Descending order: ", sorting_order, "\n")

sort_idx = np.argsort(largest_5)[::-1]
orginal_indices = indices[sort_idx]
print("Orginal indices: ", orginal_indices, "\n")

