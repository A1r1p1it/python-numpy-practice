### Problem 9: Multi-Condition Filter
#Generate 100 random numbers (1-100). Find numbers that are:
#- Greater than 50 AND divisible by 3
#- Less than 30 OR greater than 80
#- Between 40-60 AND even
arr = np.random.randint(1, 101, 100)
print("100 random numbers: \n", arr, "\n")

divide_3 = arr[(arr > 50) & (arr % 3 == 0)]
print("Greater than 50 AND divisible by 3: \n", divide_3, "\n")

less_30 = arr[(arr < 30) | (arr > 80)]
print("Less than 30 OR greater than 80: \n", less_30, "\n")

bet_40_60 = arr[(arr > 40) & (arr < 60) & (arr % 2 == 0)]
print("Between 40-60 AND even: \n", bet_40_60, "\n")
