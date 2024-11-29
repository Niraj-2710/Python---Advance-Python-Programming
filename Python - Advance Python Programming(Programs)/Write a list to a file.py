"Write a list to a file"

filename = "output.txt"
my_list = ["apple", "banana", "cherry"]

with open(filename, 'w') as file:
    for item in my_list:
        file.write(f"{item}\n")
