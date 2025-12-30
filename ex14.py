employees = {"Alice": "HR", "Bob": "Engineering", "Diana": "Marketing"}

# You are managing a dictionary of employee data,
# where each key is an employee's name and the value is their department.
if "Alice" in employees:
    print("Alice is in the company.")
if "John" not in employees:
    print("John is not in the company.")

def check_inventory(inventory, item):
    # Check if the item exists as a key in the inventory dictionary.
    if item in inventory:
        return f"{item} is in stock. Quantity: { inventory[item]}"
    elif item not in inventory:
        return f"{item} is not in stock."
