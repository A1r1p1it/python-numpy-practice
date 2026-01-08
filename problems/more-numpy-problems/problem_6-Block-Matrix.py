## Problem 7: Block Matrix with hstack/vstack
# Create the following 2D block matrix using only NumPy functions,
# hstack, and vstack:
# ```
# [I3 Z3 ]
# [O3 2I3]
# ```
# Where:
# - I3: 3×3 identity matrix
# - Z3: 3×3 matrix of all 7s
# - O3: 3×3 zeros
# **Final shape:** (6, 6)
arr_i3 = np.eye(3)
print("I3: 3×3 identity matrix: ", arr_i3)
arr_z3 = np.ones((3, 3)) * 7
print("Z3: 3×3 matrix of all 7s: ", arr_z3)
arr_o3 = np.zeros((3, 3))
print("O3: 3×3 zeros: ", arr_o3)
arr_2i3 = np.eye(3) * 2
print("2I3: ", arr_2i3)
top_row = np.hstack((arr_i3, arr_z3))
bottom_row = np.hstack((arr_o3, arr_2i3))
print("Top row: \n", top_row)
print("bottom row: \n", bottom_row)
matrix_bloc = np.vstack((top_row, bottom_row))
print("Matrix block: \n", matrix_bloc)
