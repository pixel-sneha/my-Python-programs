# Write a program that:
#Takes a number as input from the user (float).
#takes the number of decimal places to round to (integer).
#Outputs the rounded number.
num = float(input())
places = int(input())
print(round(num,places))

#Create a function named calculate_discount that takes two parameters:
#price: The original price of an item (float)
#discount_percentage: The discount percentage (float)
#The function should:

#Calculate the discount amount
#Subtract the discount amount from the original price
#Round the result to 2 decimal places, Return the final discounted price
def calculate_discount(price, discount_percentage):
    discount_amount = price * (discount_percentage / 100)
    discounted_price = price - discount_amount
    return round(discounted_price, 2)

#Convert the following data into lists using the list() function:
a_tuple = (10,20,30)
a_string = "python"
a_range = range(1,6)
print(list(a_tuple))
print(list(a_string))
print(list(a_range))

#Create a function named create_student_dict that takes three parameters: name, age, and major. 
#The function should return a dictionary where the keys are "name", "age", and "major", 
#and the values are the corresponding values passed to the function.
def create_student_dict(name, age, major):
    dictionary = {
        "name": name,
        "age": age,
        "major": major
    }
    return dictionary

#Create a function named get_capital that takes two parameters: country_capitals (a dictionary) and country_name (a string). The function should 
#return the capital city of the given country name using the country_capitals dictionary.

def get_capital(country_capitals, country_name):
    return country_capitals[country_name]

def update_employee_info(employee_dict, key, value):
    # Update the dictionary with the new key and value
    employee_dict[key] = value
    
    # Return the updated dictionary
    return employee_dict


# Recipe Manager
recipe_book = {
    "Pancakes": ["flour", "milk", "eggs", "sugar"],
    "Salad": ["lettuce", "tomato", "cucumber", "olive oil"],
    
}
print(recipe_book["Pancakes"])
recipe_book["Smoothie"] = ["banana", "milk", "honey"]
recipe_book["Smoothie"] = ["banana", "milk", "honey", "blueberries"]
print(recipe_book)

#Create a function named create_book_dict that takes three parameters: title, author, and year. The function should return a dictionary where the keys are "title", "author", and "year",
#and the values are the corresponding values passed to the function.
def create_book_dict(title, author, year):
    book_dict = {
        "title" : title,
        "author" : author,
        "year" : year
    }
    return book_dict


#Create a function named update_inventory that takes three parameters: inventory_dict (a dictionary), item (a string), and quantity (an integer).
#The function should update the inventory_dict with the new item and quantity. If the item already exists in the inventory, its quantity should be increased by the given amount. If the item does not exist, a new item should be added with the given quantity. 
#The function should return the updated dictionary.

def update_inventory(inventory_dict, item, quantity):
    # Update the dictionary with the new item and quantity
    if item in inventory_dict:
        inventory_dict[item] += quantity
    else:
        inventory_dict[item] = quantity
    
    # Return the updated dictionary
    return inventory_dict

# Step 1: Create the Grades Dictionary
grades = {
    # Add initial student grades
    "Alice" : 85,
    "Bob" : 90,
    "Charlie" : 78
}

# Step 2: Access All Keys and Values
keys = grades.keys()

# Print all students and grades
print(f"Students: {keys}")
print("Grades:",grades.values())

# Step 3: Add a New Student
# Add Diana with a grade of 92
grades["Diana"] = 92

# Step 4: Retrieve a Student's Grade
# Get Bob's grade using get() method
print("Bob's grade:",grades.get("Bob"))

# Step 5: Remove a Student
# Remove Charlie using pop() method
# Print the updated dictionary
updated_dict = grades.pop('Charlie')
print("Updated grades:",grades)
