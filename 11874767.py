# matplotlib

import matplotlib.pyplot as plt
import numpy as np

# Step 1: Create figure and set axis limits
fig = plt.figure()
plt.axis([0, 1000, 0, 1])

# Step 2: Initialize variables
i = 0
x = list()
y = list()

# Step 3: Start while loop to generate and plot points
while i < 1000:
    # Step 4: Generate random y-value
    temp_y = np.random.random()

    # Step 5: Append coordinates to lists
    x.append(i)
    y.append(temp_y)

    # Step 6: Plot current point (buggy: expects real-time update)
    plt.scatter(i, temp_y)

    # Step 7: Increment counter
    i += 1

    # Step 8: Call plt.show() expecting immediate display update (BUG: blocking behavior)
    plt.show()

print("Loop completed - all points should have appeared one by one")