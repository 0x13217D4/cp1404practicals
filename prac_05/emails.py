email_to_name = {}
email = input("Email: ")
while email != "":
    name = email.split("@")[0]
    confirmation = input(f"Is your name {name}? (Y/n) ").upper()
    if confirmation != "" and confirmation != "Y":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")
print()
for email, name in email_to_name.items():
    print(f"{name} ({email})")

