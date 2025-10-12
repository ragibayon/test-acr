# scipy

import numpy
import scipy
import scipy.signal
import timeit

# Step 1: Create a 1D array with 1,000,000 elements
a = numpy.array([range(1000000)])

# Step 2: Attempt to reshape to 1000x1000 (BUG: reshape without assignment)
a.reshape(1000, 1000)  # This doesn't modify 'a' in-place!

# Step 3: Define a 3x3 edge detection filter
filt = numpy.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])

# Step 4: Define convolution function
def convolve():
    global a, filt
    scipy.signal.convolve2d(a, filt, mode="same")

# Step 5: Benchmark the convolution performance
t = timeit.Timer("convolve()", "from __main__ import convolve")

# Step 6: Print timing results
print("Array shape:", a.shape)  # Shows the bug - still (1, 1000000)
print("%.2f sec/pass" % (10 * t.timeit(number=10)/100))