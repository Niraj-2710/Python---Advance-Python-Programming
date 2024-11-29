"Count the frequency of words in a file"

from collections import Counter

filename = "sample.txt"
with open(filename, 'r') as file:
    words = file.read().split()
word_count = dict(Counter(words))
print(word_count)
