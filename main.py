import numpy as np
import scipy.sparse as ssp

# Step 1: Create a sparse matrix (lil_matrix format)
a = ssp.lil_matrix((5, 3))
a[1, 2] = -1
a[4, 1] = 2

print("Sparse matrix 'a':")
print(a.todense())

# Step 2: Create a dense 1D array for broadcasting
d = np.ones(3) * 3
print("\nDense 1D array 'd':")
print(d)

# Step 3: Attempt element-wise multiplication using '*' operator
# BUG: This performs matrix multiplication instead of element-wise multiplication
result_matrix_mult = a * d
print("\nResult of 'a * d' (matrix multiplication, not element-wise):")
print(result_matrix_mult)
print("Shape:", result_matrix_mult.shape)
print("Type:", type(result_matrix_mult))

# Step 4: Show what the user expects (element-wise with broadcasting)
# This requires converting to dense, which defeats the purpose for large matrices
expected_result = a.toarray() * d
print("\nExpected result (a.toarray() * d - element-wise with broadcasting):")
print(expected_result)
print("Is sparse:", ssp.issparse(expected_result))

# Step 5: Demonstrate the memory issue - toarray() creates dense matrix
print("\nMemory issue: toarray() creates dense matrix:")
print("Original sparse matrix is sparse:", ssp.issparse(a))
print("After toarray() is sparse:", ssp.issparse(a.toarray()))