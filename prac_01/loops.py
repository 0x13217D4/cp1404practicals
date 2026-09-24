for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_stars = int(input("Enter number of stars: "))
for i in range(number_of_stars):
    print("*", end=' ')

number_of_lines = int(input("Enter number of lines: "))
for l in range(1,number_of_lines+1):
    print("*" * l)
