import numpy as np
import pandas as pd

arr = np.round(100*np.random.rand(20,3))
data = pd.DataFrame(arr, columns=['Subject 1', 'Subject 2', 'Subject 3'])

print("Students marks in 3 subjects: \n", data, "\n")

mean_col = np.mean(arr, axis=0)
print("Class average for each subject: ", mean_col, "\n")

mean_row = np.mean(arr, axis=1)
print("Each student's average: \n", mean_row, "\n")
