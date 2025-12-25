### Problem 3: Grade Classifier
# Generate 20 random exam scores (0-100). Use masking to:
# - Count how many students passed (≥40)
# - Find all scores above 80 (A grade)
# - Replace all failing scores with 0
arr = np.random.randint(1, 101, 20)
print("20 random integers: ", arr, "\n")
student_40 = arr[arr >= 40]
print("Number of students whp passed the exam: ", student_40, "\n")
score_80 = arr[arr > 80]
print("All the score above 80: ", score_80, "\n")
arr[arr <= 40] = 0
print("Replacing all failing scores wiht '0': ", arr)
