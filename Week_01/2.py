item_price = float(input("Enter item price: $"))
has_GST = input("Do you have GST? (y/n): ")
if has_GST == "y":
    final_price = item_price * 1.1
else:
    final_price = item_price
print(f"${final_price:.2f}")