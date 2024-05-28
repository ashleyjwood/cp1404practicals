"""
Enter a password and print a row of stars the same length.
"""

# CONSTANTS
PASSWORD_LENGTH_MIN = 10


def main():
    password = get_password()
    print_stars(password)


def get_password():
    """Get a password from the user and check its length."""
    password = input("Enter your password: ")
    while len(password) < PASSWORD_LENGTH_MIN:
        print(f"Password is too short! Must be at least {PASSWORD_LENGTH_MIN} characters.")
        password = input("Enter your password: ")
    return password


def print_stars(password):
    """Print a row of stars the same length as the password."""
    for i in range(len(password)):
        print("*", end="")
    print()


main()
