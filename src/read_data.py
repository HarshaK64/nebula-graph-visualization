import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Load your DataFrame from the 'emails.csv' file
nRowsRead = 1000
df1 = pd.read_csv('emails.csv', delimiter=',', nrows=nRowsRead)
df1.dataframeName = 'emails.csv'
nRow, nCol = df1.shape

# Split the 'message' column into words
words = df1['message'].str.split().explode()

# Count the frequency of each word
word_counts = words.value_counts()

# Select the top N words (e.g., top 10) for visualization
top_n = 10
top_words = word_counts.head(top_n)

# Create a bar chart to visualize the most frequent words
plt.figure(figsize=(12, 6))
plt.bar(top_words.index, top_words.values)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title(f'Top {top_n} Most Frequent Words in Email Messages')
plt.xticks(rotation=45)
plt.show()
