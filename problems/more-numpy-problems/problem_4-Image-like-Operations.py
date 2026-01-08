## Problem 5: Image-like Operations
# Create a (5, 5) array with values from 0 to 24, reshaped.
# **Tasks:**
# - Treat it as a grayscale "image"
# - Use slicing to extract the center 3×3 patch
# - Set the border (outermost rows and columns) to 0, keeping the
# center patch unchanged
# - Stack the original and modified arrays vertically using `vstack`
# to compare
import numpy as np
arr = np.random.randint(0, 25, (5, 5))
print("(5, 5) array with values from 0 to 24 \n", arr)

center_patch = arr[1:4, 1:4]
print(" center 3×3 patch \n", center_patch)

zero = arr.copy()
zero[0,:] = 0
zero[-1,:] = 0
zero[:,0] = 0
zero[:,-1] = 0
print("border to '0'", zero)
stacked = np.vstack((arr, zero))
print("Stack the original and modified arrays vertically: ", stacked)
