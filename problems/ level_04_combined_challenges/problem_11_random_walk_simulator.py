### Problem 11: Random Walk Simulator
#- Start with position 0
#- Generate 1000 random steps: each step is +1 or -1 (use randint)
#- Use cumulative sum to track position over time
#- Find the maximum and minimum positions reached
arr = np.random.randint(0, 2, 1000)
arr[arr == 0] = -1
#arr = np.random.choice([-1, 1], size=1000)
print("Generates 1000 steps: ", arr, "\n")

cum_pos = np.cumsum(arr)
print("cumulative sum to track position over time: ", cum_pos, "\n")

max = np.max(cum_pos)
print("maximum position: ", max,"\n")

min = np.min(cum_pos)
print("minimum position: ", min,"\n")
