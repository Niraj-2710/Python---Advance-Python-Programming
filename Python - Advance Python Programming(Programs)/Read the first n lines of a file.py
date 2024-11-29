"Read the first n lines of a file"

filename = "sample.txt"
n = 5
with open(filename, 'r') as file:
    lines = [next(file) for _ in range(n)]
print(lines)
