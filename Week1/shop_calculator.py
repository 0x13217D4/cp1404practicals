"""
Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92
"""
number_of_items = int(input("Enter number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Enter number of items: "))
total_cost = 0
for i in range(number_of_items):
    price_of_item = float(input("Enter price of item: "))
    total_cost += price_of_item
if total_cost >= 100:
    total_cost = total_cost * 0.9
print(f"Total cost of {number_of_items} items: {total_cost:.2f}")