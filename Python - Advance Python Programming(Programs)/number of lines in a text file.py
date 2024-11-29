"Count the number of lines in a text file"

filename = "sample.txt"
with open(filename, 'r') as file:
    lines = file.readlines()
line_count = len(lines)
print(line_count)
