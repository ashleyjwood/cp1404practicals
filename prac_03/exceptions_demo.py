"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When anything aside from an integer number is entered. E.g., a string or a float.

2. When will a ZeroDivisionError occur?
When the user enters "0" as the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes. You can us and if-else statement to check if the denominator is zero.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
