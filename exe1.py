"""Write code to:

Retrieve and print the value of "bananas".
Add a new item to the dictionary: "grapes" with a value of 15.
Increase the value of "apples" by 5.
Check if "oranges" exists in the dictionary and print True or False."""
inventory = {
    "apples": 10,
    "bananas": 5,
    "oranges": 7
}
inventory = {
    "apples": 10,
    "bananas": 5,
    "oranges": 7
}

# 1. Retrieve and print the value of "bananas"
print("Bananas:", inventory["bananas"])

# 2. Add a new item: "grapes" with value 15
inventory["grapes"] = 15

# 3. Increase the value of "apples" by 5
inventory["apples"] += 5

# 4. Check if "oranges" exists in the dictionary and print True or False
print("Oranges exist:", "oranges" in inventory)

# Print the updated dictionary for reference
print("Updated Inventory:", inventory)