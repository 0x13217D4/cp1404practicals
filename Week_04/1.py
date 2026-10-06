names = ["Ada","Alan","Bill","John"]
print(",".join(names))
name_to_remove = input("Enter a name to remove: ")
while name_to_remove != "":
    try:
        names.remove(name_to_remove)
        print(",".join(names))
    except ValueError:
        print(f"The name {name_to_remove} was not found.")
    name_to_remove = input("Enter a name to remove: ")