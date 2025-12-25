### Problem 5: Checkerboard Pattern
# Create an 8×8 array and fill it with a checkerboard pattern
# (alternating 0s and 1s)
a = np.round(10*np.random.rand(8, 8))

c = np.zeros(a.shape)

c[1::2, ::2] = 1
c[::2, 1::2] = 1
print("Checkerboard Pattern \n",c)
