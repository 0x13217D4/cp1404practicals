user_number = int(input("Have many age?: "))

total = 0
for i in range(user_number):
    age = int(input("Enter your Age: "))
    total += age

average = total / user_number
print(total)
print(average)

age = int(input("Enter your Age: "))
total = 0
count = 0

while age != -1:
    total += age
    count += 1
    age = int(input("Enter your Age: "))

average = total / count
print(total)
print(count)