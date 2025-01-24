"""Asks the user to enter a year.
Checks if the entered year is a leap year using the following rules:
A year is a leap year if it is divisible by 4.
However, it is not a leap year if it is divisible by 100, unless it is also divisible by 400.
Print:
"It is a leap year." if the year is a leap year.
"It is not a leap year." if it is not a leap year."""

print("year App")
year = int(input("Enter year of choice: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("this is a leap year")
else:
    print("It is not a leap year")

"""if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a leap year.")
else:
    print("It is not a leap year.")"""