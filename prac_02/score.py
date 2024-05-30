"""
Determine the status of a score based on a given range of values.
"""

# Imports
import random


def main():
    """Main function to get a score and print its status."""
    score = get_score()
    print_score_status(score)


def get_score():
    """Get a score from the user."""
    score = float(input("Enter score: "))
    return score


def print_score_status(score):
    """Print the status of the score based on its value."""
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


random_score = random.randint(1, 100)
print(random_score)
print_score_status(random_score)

main()
