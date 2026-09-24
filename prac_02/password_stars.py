password = "114514"

def main():
    password = get_password()
    print_stars(password)

def get_password():
    user_enter_password = input("Enter the password: ")
    while password != user_enter_password:
        print("Incorrect password")
        user_enter_password = input("Enter the password: ")
    return user_enter_password

def print_stars(password):
    print("*" * len(password))

main()