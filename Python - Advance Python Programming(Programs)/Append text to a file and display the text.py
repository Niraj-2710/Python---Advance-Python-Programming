"Append text to a file and display the text"

filename = "sample.txt"
text_to_append = "This is the new text."

with open(filename, 'a') as file:
    file.write(text_to_append + "\n")

with open(filename, 'r') as file:
    content = file.read()
print(content)
