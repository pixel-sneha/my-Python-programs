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
