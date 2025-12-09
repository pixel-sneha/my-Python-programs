input_list = input().split(', ')
if len(input_list) >= 5:
    print([input_list[0], input_list[1], input_list[len(input_list) - 2], input_list[len(input_list) - 1]])
else:
    print([input_list[0], input_list[len(input_list) - 1]])

#Create a program that receives a list as input (given) and prints three new lists based on the following slicing operations:
#A list containing every third element, starting from index 1 (the second element)
#A list containing all the elements from the 6th element to the 1st in reverse order
#A list containing every second element starting from the middle of the list to the end
lst = input().split(",")
size = len(lst)//2
print(lst[1::3])
print(lst[5::-1])
print(lst[size::2])

#Create a function that Concatenate the list with itself (list + list).
#Repeats the resulting list repeats times using the * operator. And Return the final pattern.
def create_pattern(numbers, repeats):
    concat_list = numbers + numbers
    final_list = concat_list * repeats
    return final_list

#Create a program that receives two lists and prints a new list of 
#all elements that are in the first list but NOT in the second list.
lst1 = input().split(",")
lst2 = input().split(",")
final_list = []
for i in lst1:
    if i not in lst2:
        final_list.append(i)
print(final_list)

#Write a Python program that performs the following tasks:
#Assign values to three variables name, age, and city in a single line. Set name to "Alice", age to 30, and city to "New York".
#Assign the value 100 to three variables x, y, and z in a single line.
#Create a list named colors containing the values "red", "green", and "blue". Assign these values to three variables color1, color2, and color3 in a single line.

# Assign values to name, age, and city
name,age,city = "Alice",30,"New York"

# Assign 100 to x, y, and z
x = y = z = 100

# Create a list of colors and assign them to color1, color2, and color3
colors = ["red", "green", "blue"]
color1, color2, color3 = colors

# Output
print(f"Name: {name}, Age: {age}, City: {city}")
print(f"x: {x}, y: {y}, z: {z}")
print(f"Colors: {color1}, {color2}, {color3}")
