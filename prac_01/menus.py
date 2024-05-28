name = input("Enter your name: ")
menu = """(H)ello
(G)oodbye
(Q)uit"""
print(menu)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid input")
    print(menu)
    choice = input(">>> ").upper()
print("Finished")
