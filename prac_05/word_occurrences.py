"""
Word Occurrences
Estimate: 20 minutes
Actual:   17 minutes
"""

# Prompt the user to enter a string
text = input("Text: ")

# Split the input text into a list of words
words = text.split()

# Create a dictionary to count occurrences of each word
word_counts = {}