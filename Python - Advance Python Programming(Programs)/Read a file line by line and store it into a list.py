"Read a file line by line and store it into a list"

filename = "sample.txt"
with open(filename, 'r') as file:
    lines = file.readlines()
print(lines)
