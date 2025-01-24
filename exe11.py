#Quiz app
#quit option
#question answer
#score
#percentage

print ("Welcome to the quiz app")
ready = input("Are you ready to start the quiz: ").lower()
if ready != "yes" :
    exit()
print(" Let's begin:)")
score = 0
answer1 = input(" What does 'CPU' stand for?: ").lower()
if answer1 == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")
answer2 = input(" What is the binary representation of the decimal number 10?: ").lower()
if answer2 == "1010":
    print("Correct")
    score += 1
    
else:
    print("Incorrect")
    

answer3 = input("What does 'HTTP' stand for?: ").lower()
if answer3 == "hypertext transfer protocol":
    print("Correct")
    score += 1
else:
    print("Incorrect")


answer4 = input("In Python, which keyword is used to define a function?: ").lower()
if answer4 == "def":
    print("Correct")
    score += 1
else:
    print("Incorrect")


answer5 = input("What is the time complexity of binary search in a sorted array?: ").lower()
if answer5 == "O(log n)":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    

answer6 = input("Which data structure uses the 'Last In, First Out' (LIFO) principle?: ").lower()
if answer6 == "stack":
    print("Correct")
    score += 1
else:
    print("Incorrect")


print("Your final score is: " + str(score))
if score >= 4 :
    print( "Passed")
else: 
    print("Fail")