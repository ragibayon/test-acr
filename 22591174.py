# pandas

import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Step 1: Create a DataFrame with columns 'a' and 'b'
df = pd.DataFrame({'a': range(5), 'b': range(5)})

# Step 2: Insert some -1 values using chained indexing (potentially buggy)
df['a'][1] = -1
df['b'][1] = -1
df['a'][3] = -1
df['b'][4] = -1

# Step 3: Filter using AND operator - user expects this to keep rows where both are not -1
df1 = df[(df.a != -1) & (df.b != -1)]

# Step 4: Filter using OR operator - user expects this to keep rows where at least one is not -1
df2 = df[(df.a != -1) | (df.b != -1)]

# Step 5: Concatenate and display results
result = pd.concat([df, df1, df2], axis=1, keys=['original df', 'using AND (&)', 'using OR (|)'])

print(result)

# Step 6: Print user's confusion about the behavior
print("\nUser's confusion: AND operator seems to behave like OR, and OR operator seems to behave like AND!")