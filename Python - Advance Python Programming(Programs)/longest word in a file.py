"Find the longest word in a file"

filename = "sample.txt"
with open(filename, 'r') as file:
    words = file.read().split()
longest_word = max(words, key=len)
print(longest_word)
