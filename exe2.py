
"""Write code to:

Add a new hobby "swimming" to the "hobbies" list.
Change the "last_name" to "Johnson".
Create a new key "is_employed" with the value True.
Remove the "age" key from the dictionary."""
person = {
    "first_name": "Alice",
    "last_name": "Smith",
    "age": 30,
    "hobbies": ["reading", "cycling", "hiking"]
}
person["last_name"]= "Johnson"
person.update({"is_employed":"True"})
del person["age"]
print(person)