# dataframe

import pandas as pd
import numpy as np

# Step 1: Create a mock DataFrame with mixed data types and zero values
df2 = pd.DataFrame({
    'ID': ['P001', 'P002', 'P003', 'P004'],
    'Name': ['John', 'Jane', 'Bob', 'Alice'],
    'Weight': [70.5, 0, 65.2, 80.0],
    'Height': [175.0, 160.5, 0, 170.0],
    'BootSize': ['42', '0', '38', '40'],
    'SuitSize': ['M', 'L', '0', 'S'],
    'Type': ['A', 'B', 'A', 'C']
})

print("Original DataFrame:")
print(df2)
print("\nData types:")
print(df2.dtypes)

# Step 2: Working approach (individual column replacements)
print("\n--- Working approach ---")
df2_working = df2.copy()
df2_working.loc[df2_working['Weight'] == 0, 'Weight'] = np.nan
df2_working.loc[df2_working['Height'] == 0, 'Height'] = np.nan
df2_working.loc[df2_working['BootSize'] == '0', 'BootSize'] = np.nan
df2_working.loc[df2_working['SuitSize'] == '0', 'SuitSize'] = np.nan
print(df2_working)

# Step 3: Buggy approach - user expects this to modify df2 directly
print("\n--- Buggy approach ---")
# This creates a new object but doesn't modify df2
df2[["Weight","Height","BootSize","SuitSize"]].astype(str).replace('0', np.nan)

# Step 4: Show that df2 remains unchanged
print("DataFrame df2 after buggy approach (zeros remain):")
print(df2)

# Step 5: Demonstrate the issue - the operation doesn't modify the original
print("\nThe buggy approach returns a new object but doesn't modify df2!")
result = df2[["Weight","Height","BootSize","SuitSize"]].astype(str).replace('0', np.nan)
print("Result of the chained operation:")
print(result)