"""Write a program to find the largest number in the following array:
"""
my_array = [15, 22, 8, 19, 31, 5]
maxVal = my_array[0]
for i in my_array:
    if i > maxVal:
        maxVal = i
print(maxVal)

"""my_array = """
my_array = [18, 12, 9, 5, 7, 3, 15]
minVal = my_array[0]
for i in my_array:
    if i < minVal:
        minVal = i
print(minVal)