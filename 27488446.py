# scikit-learn

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# Step 1: Create a list of text documents
texts = ["dog cat fish", "dog cat cat", "fish bird", "bird"]

# Step 2: Initialize CountVectorizer
cv = CountVectorizer()

# Step 3: Fit and transform the texts
cv_fit = cv.fit_transform(texts)

# Step 4: Print vocabulary expecting word frequencies but getting indices instead
print(cv.vocabulary_)
# User expects: {u'bird': 2, u'cat': 3, u'dog': 2, u'fish': 2}
# But actually gets: {u'bird': 0, u'cat': 1, u'dog': 2, u'fish': 3}

# Step 5: Show what the user actually gets vs what they expect
print("\nActual output (word-to-index mapping):")
print(cv.vocabulary_)
print("\nExpected output (word frequencies):")
print("{u'bird': 2, u'cat': 3, u'dog': 2, u'fish': 2}")

# The bug: vocabulary_ returns feature indices, not frequency counts
# The actual frequency data is in cv_fit.toarray().sum(axis=0)