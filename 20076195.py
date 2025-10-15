import pandas as pd
import numpy as np

# Step 1: Set random seed for reproducibility
np.random.seed(42)

# Step 2: Create a mock DataFrame with 12M rows (using smaller size for demo)
# In practice this would be 12,000,000 rows but using 100,000 for demonstration
print("Creating large DataFrame...")
words = ['apple', 'banana', 'cherry', 'date', 'elderberry'] * 20000
documents = np.random.randint(1, 1000, 100000)
frequency = np.random.randint(1, 100, 100000)

df = pd.DataFrame({
    'word': words,
    'documents': documents,
    'frequency': frequency
})

print(f"DataFrame shape: {df.shape}")
print("Columns:", df.columns.tolist())

# Step 3: Create groupby object - this runs efficiently
print("\nCreating word grouping...")
word_grouping = df[['word','frequency']].groupby('word')

# Step 4: Calculate max frequency per word - this runs quickly
print("Calculating max frequency per word...")
MaxFrequency_perWord = word_grouping[['frequency']].max().reset_index()
MaxFrequency_perWord.columns = ['word','MaxFrequency']
print("Max frequency calculation completed quickly")
print(MaxFrequency_perWord.head())

# Step 5: Attempt to count occurrences using inefficient approach
# This is the buggy/slow approach that the user is experiencing
print("\nCounting occurrences using inefficient method...")
print("This may take unexpectedly long time...")

# BUG: Using count() on grouped data in an inefficient way
# The user tries to count after groupby which is redundant and slow
word_grouping_for_count = df[['word','frequency']].groupby('word')
Occurrences_of_Words = word_grouping_for_count.count().reset_index()
Occurrences_of_Words.columns = ['word', 'count']
print("Count operation completed (slower than expected)")
print(Occurrences_of_Words.head())

# Step 6: Show that df.word.describe() runs well as mentioned by user
print("\nRunning df.word.describe() - this runs quickly:")
print(df.word.describe())