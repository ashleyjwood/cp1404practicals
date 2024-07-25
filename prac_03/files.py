# Question 1
user_name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(user_name, file=out_file)
out_file.close()

# Question 2
in_file = open("name.txt", "r")
text = in_file.read().strip()
print(f"Hi {text}!")
in_file.close()

# Question 3
with open("numbers.txt", "r") as in_file:
    line = in_file.readlines()
    result = int(line[0].strip()) + int(line[1].strip())
print(f"{line[0].strip()} + {line[1].strip()} = {result}")

# Question 4
with open("numbers.txt", "r") as in_file:
    total = 0  # Initialise total
    for line in in_file:
        value = int(line.strip())
        total += value
print(total)
