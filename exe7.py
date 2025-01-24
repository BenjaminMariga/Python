"""Create a dictionary called student with the following key-value pairs:

"name": "John"
"age": 25
"grade": "A"
Then, do the following:

Add a new key "major" with the value "Computer Science".
Update the "age" to 26.
Remove the "grade" key from the dictionary.
"""
student = {
    "name" : "John",
    "age" : 25,
    "grade": "A"
}
student.update({"major": "Computer Science"})
student["age"] = 26
del student["grade"]
print(student)