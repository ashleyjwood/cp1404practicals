"""
Emails
Estimate:   30 minutes
Actual:     forgot to start the timer
"""
email_to_name = {}


def main():
    """Print a list of name, email pairs as entered by the user."""
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        print(f"Is your name {name}? (y/n)")
        choice = input().strip().lower()
        if choice == 'y' or choice == "":
            email_to_name[email] = name
        else:
            name = input("Name: ")
            email_to_name[email] = name
        email = input("Email: ")

    print_pairs()


def extract_name_from_email(email):
    """Extract name from email."""
    return " ".join(email.split('@')[0].split(".")).title()


def print_pairs():
    """Print name, email pairs."""
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
