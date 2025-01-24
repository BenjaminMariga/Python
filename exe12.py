#random number 
import random

max_value = int(input("Enter the maximum value for the range"))

if max_value <= 2:
    print("enter a value greater than 2")   
    exit()

        
          
rand_num = random.randrange(1, max_value) 
print("Are you ready to guess the number!")
welcome = input("Type Yes to CONTINUE or no to EXIT: ").lower()
if welcome != "yes":
    exit()
print("Let the game begin")
guess = 0
while True:
    user_guess = int(input("Enter your guess: "))
    if user_guess > 10:
        print("number should not be greater than ", max_value)
       
    if user_guess == rand_num:
        print("great. You got after "+ str(guess) + " gueses")
        break
    else:
        print("try Again")
        guess += 1



