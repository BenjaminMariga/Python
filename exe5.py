"""Asks the user to input a number.
Checks if the number is:
Positive: Print "The number is positive."
Negative: Print "The number is negative."
Zero: Print "The number is zero."
"""
while True:
    number = int(input("Enter number"))
    if number > 0:
        print("The number is positive")
    elif number < 0:
        print("The number is negative")
    else:
        print("number is 0")
        break