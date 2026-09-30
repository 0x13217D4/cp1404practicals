import random
low_number = int(input("Enter a low number: "))
high_number = int(input("Enter a high number: "))
while high_number <= low_number:
    print("high number must be grater than low number")
    high_number = int(input("Enter a high number: "))
n = random.randint(low_number, high_number)
for i in range(n):
    print(":)",end="")