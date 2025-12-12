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
