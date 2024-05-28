MINIMUM_LENGTH = 10
password = input("Enter your password: ")
while len(password) < MINIMUM_LENGTH:
    print(f"Password is too short! Must be at least {MINIMUM_LENGTH} characters.")
    password = input("Enter your password: ")
for i in range(len(password)):
    print("*", end="")
print()
