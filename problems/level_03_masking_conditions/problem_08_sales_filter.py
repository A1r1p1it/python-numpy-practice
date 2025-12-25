###Problem 8: Sales Filter
#Create a "sales" array with 50 random values (100-1000). Find:
#- All sales above 500
#- Sales between 300-700
#x- Replace all sales below 200 with 200 (minimum guarantee)
import numpy as np
arr = np.random.randint(100, 1001, 50)
print("50 random values:\n", arr, "\n")

sal_500 = arr[arr > 500]
print("All sales above 500:\n", sal_500, "\n")

sal_300_700 = arr[(arr > 300) & (arr < 700)]
print("Sales between 300-700: ", sal_300_700, "\n")

arr[arr < 200] = 200
print("all sales below 200 with 200: ", arr,"\n")
