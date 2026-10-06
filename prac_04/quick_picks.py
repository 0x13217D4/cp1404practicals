import random

NUMBER_OF_PICKS = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for _ in range(number_of_quick_picks):
        pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in pick))

def generate_quick_pick():
    pick = []
    while len(pick) < NUMBER_OF_PICKS:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in pick:
            pick.append(number)
    pick.sort()
    return pick

main()