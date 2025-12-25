### Problem 7: Even-Odd Separator
# Create an array of 30 random integers (1-100). Use masking to:
# - Create two separate arrays: one with even numbers, one with odd
# - Replace all even numbers with their squares
# - Count how many numbers are divisible by 5
a = np.random.randint(1, 101, size= 30)
print("Orginal integers: ", a, "\n")
xx = a % 2 == 0
yy = a % 2 != 0
even_numbers = a[xx]
odd_numbers = a[yy]

print("Even numbers in the array: ", even_numbers, "\n")                         
print("Odd numbers in the array: ", odd_numbers, "\n")
