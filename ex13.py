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
