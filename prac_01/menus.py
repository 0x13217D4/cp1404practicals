user_name = input("Enter name: ")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
user_choice = input(">>> ").upper()
while user_choice != "Q":
    if user_choice == "H":
        print(f"Hello {user_name}")
    elif user_choice == "G":
        print(f"Goodbye {user_name}")
    else:
        print("Invalid choice")
    user_choice = input(">>> ").upper()
print("Finished.")