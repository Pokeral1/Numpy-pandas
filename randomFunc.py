import numpy as np
# Random floats between 0 and 1
np.random.rand(5)
# [0.37 0.95 0.73 0.60 0.16]

# Random integers — (low, high, size) — high is exclusive
np.random.randint(1, 100, 8)
# [23 87 4 65 12 90 44 31]

# Random floats with mean=0, std=1 (normal distribution)
np.random.randn(5)
# [-0.3  1.2 -0.8  0.5  1.9]

# Randomly pick from an array
np.random.choice([10, 20, 30, 40, 50], size=3)
# [30 10 50]

# Fix results so they're same every run — useful for practice
np.random.seed(42)
arr = np.array([64, 23, 87, 12, 45])

np.sort(arr)          # [12 23 45 64 87] — returns new sorted array
np.sort(arr)[::-1]    # [87 64 45 23 12] — descending

# 2D — sort within each row
grid = np.array([[3,1,2],[9,7,8]])
np.sort(grid, axis=1) # [[1,2,3],[7,8,9]]

# argsort — returns indices instead of values (you used this yesterday)
np.argsort(arr)       # [3 1 4 0 2] — index of smallest to largest

