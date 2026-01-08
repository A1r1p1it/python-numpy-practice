## Problem 6: One-hot Encoding
# Create a 1D array of 12 random integers representing class labels in
# {0, 1, 2, 3}.
# **Tasks:**
# - Convert it into a one-hot encoded 2D array of shape (12, 4) using
# only NumPy (no loops if possible)
# - Verify that each row sums to 1
import numpy as np

class_labels = np.random.randint(0, 4, 12)
print("Class labels:", class_labels)

one_hot = np.zeros((12, 4), dtype=int)
print("\nEmpty hot encoding:\n", one_hot)

row_indices = np.arange(12)
one_hot[row_indices, class_labels] = 1
print("\nOne-hot encoding:\n", one_hot)

print("\nRow sums:", np.sum(one_hot, axis=1))
