"Read a file line by line and store it into a variable"

filename = "sample.txt"
content = ""
with open(filename, 'r') as file:
    for line in file:
        content += line
print(content)
