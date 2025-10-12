# numpy

import numpy as np

# Step 1: Create two arrays with identical values including NaN
a = np.array([1, 2, np.NaN])
b = np.array([1, 2, np.NaN])

# Step 2: Attempt to compare arrays using np.all(a==b)
# This fails because NaN != NaN in IEEE floating-point arithmetic
if np.all(a==b):
    print('arrays are equal')
else:
    print('arrays are not equal')

# Step 3: Show the element-wise comparison to demonstrate the bug
print('Element-wise comparison:', a==b)
print('Result of np.all(a==b):', np.all(a==b))