## Problem 4: Grade Curve with Broadcasting
# Create a (15, 4) array representing marks of 15 students in 4
# subjects (0–100).
# **Tasks:**
# - Compute the mean of each subject (column-wise)
# - Use broadcasting to subtract the subject mean from each column
# (centering)
# - Add 5 marks to all subjects of students whose overall average is
# below 40
# - Clip final array to max 100 using `np.clip`
import numpy as np

arr = np.random.randint(0, 101, (15, 4))
print("array representing marks of 15 students in 4 subjects \n", arr, "\n")

compute_mean = np.round(np.mean(arr, axis = 0))
print("mean of each subject: \n", compute_mean, "\n")

subtracting = arr - compute_mean
print("subtract the subject mean: \n", subtracting, "\n")

student_avg = np.average(arr, axis = 1)
print("Average of all student: \n", student_avg, "\n")

avg_40 = student_avg < 40
print("Students whose average is below 40 (boolean mask): \n", avg_40, "\n")

arr[avg_40] = arr[avg_40] + 5
print("Array after adding 5 marks: \n", arr, "\n")

final_marks = np.clip(arr, 0, 100)
print("Final marks: \n", final_marks, "\n")

