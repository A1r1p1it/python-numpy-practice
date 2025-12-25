## Problem 12: Data Cleaning
#Create an array with 100 random numbers (1-100). Randomly replace 10
#positions with 999 (representing missing data):
#- Use masking to find all 999 values
#- Replace them with the array's mean
#- Find how many values are now above the new mean
arr = np.random.randint(1, 101, 100)
arr[arr[:10]] = 999
arr
mask = arr[arr == 999]
print("All 999 value in array: ",mask, "\n")

mean = np.mean(arr)
print("Array's mean: ", mean, "\n")
replace_mean = arr[arr == 999]= mean
print("Replacing 999s with arrays mean: ", replace_mean, "\n")
arr[arr < mean]
print("All the values above mean: ", arr)
