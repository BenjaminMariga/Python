"""Question 2: Eligibility for Voting and Driving
Write a program that asks the user for their age and checks:
If they are eligible to vote (age 18 and above).
If they are eligible to apply for a driving license (age 21 and above).
Requirements:
If the age is below 18, print "Not eligible for voting or driving.
If the age is 18–20, print "Eligible for voting but not for driving.
If the age is 21 or above, print "Eligible for both voting and driving."""

print("Voting and Driving Eligibility")
while True:
    age = int(input("Enter your age: "))
    if age <= 18 :
        print("Not eligible to vote and drive")
    elif age >=18 and  age <= 20:
        print("Eligible for voting but not for driving")
    elif age >=21:
        print("Eligible for both voting and driving")
    else:
        print("invalid input")
        break
