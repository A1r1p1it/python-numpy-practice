### Problem 4: Matrix Extraction
# Create a 6×6 array of random integers (1-20). Extract:
# - Every alternate row
# - The 4 corner elements
# - The middle 4 elements
import numpy as np


random_int_6x6 = np.random.randint(1, 21, size=(6, 6))
print("Original 6x6 array:\n", random_int_6x6, "\n")

alternate_rows = random_int_6x6[::2, :]
print("Every alternate row:\n", alternate_rows, "\n")

corner_elements = random_int_6x6[[0, 0, 5, 5], [0, 5, 0, 5]]
print("The 4 corner elements:", corner_elements, "\n")

middle_4_elements = random_int_6x6[2:4, 2:4]
print("The middle 4 elements:\n", middle_4_elements)
