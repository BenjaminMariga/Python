"""Takes an integer input from the user and stores it in a variable called number.
Checks if the number is:
Greater than 10: Print "The number is greater than 10."
Equal to 10: Print "The number is exactly 10."
Less than 10: Print "The number is less than 10."""

number = int(input("Enter a number: "))

if number  > 10:
    print("The number is greater than 10")
elif number == 10:
    print("The number is exactly 10")
else:
    print("The number is less than 10")