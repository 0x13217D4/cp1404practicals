def main():
    filename = input("Enter filename: ")
    while filename != "":
        try:
            number_of_lines = count_lines(filename)
            print(f"{filename} has {number_of_lines} lines.")
        except FileNotFoundError:
            print(f"ERROR: {filename} does not exist.")
        filename = input("Enter filename: ")

def count_lines(filename):
    with open(filename, "r") as in_file:
        lines = in_file.readlines()
    return len(lines)

main()
