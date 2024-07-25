"""
This script is a menu that allows you to:
    - Enter a valid score between 0 and 100
    - Print a status based on your score
    - Display a row of stars which is the same length as your score
"""

# CONSTANTS
MENU = """- (G)et a valid score
- (P)rint result
- (S)how stars
- (Q)uit """


def main():
    """Get a valid score from the user, return a result, and print stars based on the score."""
    score = None
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score is not None:
                print_score_status(score)
            else:
                print("Score cannot be empty")
        elif choice == "S":
            if score is not None:
                print_stars(score)
            else:
                print("Score cannot be empty")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_valid_score():
    """Get a score from the user and check if it is valid."""
    try:
        score = float(input("Enter score: "))
        if 0 <= score <= 100:
            return score
        print("Score must be between 0 and 100")
        score = None
    except ValueError:
        print("Invalid input")
    return None


def print_score_status(score):
    """Print the status of the score based on its value."""
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def print_stars(score):
    """Print a row of stars based on the score."""
    print("*" * int(score))


main()
