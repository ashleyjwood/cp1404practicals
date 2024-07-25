import random

number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    min_value = 1
    max_value = 45
    quick_pick_size = 6
    quick_picks = []
    for j in range(quick_pick_size):
        random_number = random.randint(min_value, max_value)
        while random_number in quick_picks:
            random_number = random.randint(min_value, max_value)
        quick_picks.append(random_number)
    sorted_list = sorted(quick_picks)
    for number in sorted_list:
        print(f"{number:2} ", end="")
    print()
