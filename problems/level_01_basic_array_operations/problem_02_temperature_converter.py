### Problem 2: Temperature Converter
# Create an array of 10 random temperatures in Celsius (between 0-40).
# Convert them all to Fahrenheit using the formula: F = (C × 9/5) + 32
a = np.random.randint(0, 41, size = 10)
F = (a * 9/5) + 32
print("Temperatures in Fahrenheit: ", F)
