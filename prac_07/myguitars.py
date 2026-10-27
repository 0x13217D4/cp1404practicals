from guitar import Guitar
FILENAME = "guitars.csv"

def main():
    guitars = load_guitars(FILENAME)
    print("My guitars:")
    display_guitars(guitars)
    guitars.sort()
    print("\nSorted by year (oldest to newest):")
    display_guitars(guitars)
    print("\nAdd your new guitars (blank name to finish)")
    add_new_guitars(guitars)
    save_guitars(FILENAME, guitars)
    print(f"{len(guitars)} guitars saved to {FILENAME}")

def load_guitars(filename):
    guitars = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    return guitars


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


def add_new_guitars(guitars):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")


def save_guitars(filename, guitars):
    with open(filename, "w", encoding="utf-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

main()
