FILENAME = "test.txt"
in_file = open(FILENAME, 'r')
for line in in_file:
    if line.startswith("#"):
        print(line, end="")
in_file.close()