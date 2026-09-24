def main():
    score = get_valid_score()
    print("(G)Get a valid score\n(P)Print result\n(S)Show stars\n(Q)Quit")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score(score))
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid choice")
        print("(G)Get a valid score\n(P)Print result\n(S)Show stars\n(Q)Quit")
        choice = input(">>> ").upper()

def get_valid_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

def determine_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()