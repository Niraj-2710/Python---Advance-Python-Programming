"Read the last n lines of a file"

filename = "sample.txt"
n = 5
with open(filename, 'r') as file:
    lines = file.readlines()
last_n_lines = lines[-n:]
print(last_n_lines)
