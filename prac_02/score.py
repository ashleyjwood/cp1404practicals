"""
Determine the status of a score based on a given range of values.
"""

# Imports
import random


def main():
    """Main function to get a score and print its status."""
    score = get_valid_score()
    status = determine_score_status(score)
    print(f"The score is {score:.2f} and is {status}")

    random_score = random.uniform(0, 100)
    random_score_status = determine_score_status(random_score)
    print(f"The random score is {random_score:.2f} and is {random_score_status}")


def get_valid_score():
    """Get a valid score from the user."""
    score = float(input("Enter score: "))
    while not 0 <= score <= 100:
        print("Score must be between 0 and 100.")
        score = float(input("Enter score: "))
    return score


def determine_score_status(score):
    """Determine the status of the score based on its value."""
    if score >= 90:
        status = "Excellent"
    elif score >= 50:
        status = "Passable"
    else:
        status = "Bad"
    return status


main()
