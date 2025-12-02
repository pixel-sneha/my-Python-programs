#Create a function named whatToBuy that receives four arguments:
#First argument is a list of numbers that indicate the price of a construction item
#Second argument is a list of numbers that indicates the quantity of each construction item
#Third argument is a number indicating the total price allowed for each item
#Fourth argument is a list of construction names
#The function calculates, for each item, the total price required to buy it. return sorted list of names satisfying the condtion and number of items removed
def whatToBuy(prices, quantities, restriction, names):
    if len(prices)==0:
        return [[], 0]
    average_prices = sum(prices)/len(prices)
    average_quantities = sum(quantities)/ len(quantities)
    new_list = []
    total_names = 0
    for i in range(len(prices)):
        price = prices[i]
        quantity = quantities[i]
        name = names[i]
        total_price = (quantity * price) / (average_quantities * average_prices)
        if total_price < restriction:
            new_list.append(name)
        else:
            total_names += 1
    new_list.sort()
    return [new_list, total_names]
    

# Create a program that receives a string as input
#it prints how many times the character p (or P) is in the string.
#Some chars might be uppercase, use char.lower() to convert it to lowercase
text = input()
word_count = 0
for i in range(len(text)):
    if text[i] == 'p' or text[i] == 'P':
        text[i].lower()
        word_count += 1
print(word_count)
