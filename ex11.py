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

#Write a program that takes two inputs: a text string and a delimiter character.
#The program should split the text by whitespace into words, 
#join these words using the delimited character and print the resulting string.
text = input()
delimiter = input()
updated_text = text.split()
final_text = delimiter.join(updated_text)
print(final_text)

#Create a program that receives a list as input and prints the following sliced list:
#For odd-length lists: take the middle item and one item on each side (3 items total)
#For even-length lists: take the two middle items
#When dividing numbers use // because list slicing only works with whole numbers.

lst = input().split(",")
size = len(lst)
middle = size//2
length_list = []
if size%2==0:
    print(lst[middle-1: middle+1])
else:
    print(lst[middle-1 : middle+2])
