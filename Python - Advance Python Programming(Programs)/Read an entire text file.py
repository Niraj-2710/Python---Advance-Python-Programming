" Read an entire text file "

filename = "sample.txt"
with open(filename,'r') as file:
    content = file.read()
print(content)


