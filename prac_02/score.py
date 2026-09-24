import random
def main():
    score = float(input("Enter score: "))
    result = determine_score(score)
    print(f"User score {score} is {result}")
    if result == "Excellent":
        print("You get a prize!")
    random_score = random.randint(0, 100)
    print(f"Random: {random_score} is {determine_score(random_score)}")

def determine_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()