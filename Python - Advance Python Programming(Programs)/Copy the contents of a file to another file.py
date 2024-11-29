"Copy the contents of a file to another file"

source_filename = "source.txt"
destination_filename = "destination.txt"

with open(source_filename, 'r') as source_file:
    content = source_file.read()

with open(destination_filename, 'w') as dest_file:
    dest_file.write(content)
