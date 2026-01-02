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

#Create a function named print_employee_details that takes a dictionary employee_data as an argument. 
#The function should loop through the dictionary and print each key-value pair in the format 'key: value'.
# If the dictionary is empty, the function should print 'No data available'
def print_employee_details(employee_data):
    if len(employee_data)==0:
        print("No data available")
        return
    else:
        for key, value in employee_data.items():
            print(f'{key}: {value}')
    #suppose you want capitalized key here, then use
            print(f'{key.capitalize()}: {value}')
