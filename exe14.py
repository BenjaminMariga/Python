"""Start
    Set my_array to [7, 12, 9, 4, 11]
    Set minVal to the first element of my_array

    For each element i in my_array:
        If i is less than minVal:
            Update minVal to i

    Print "Lowest value: ", minVal
End
"""
my_array = [7,12,9,4,11]
minVal = my_array[0]
for i in my_array:
    if minVal > i:
        minVal = i
print(minVal)
