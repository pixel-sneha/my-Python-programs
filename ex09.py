#Write a function with one argument that represents a number n.
#The function will return the sum of all the numbers from 1 to n (including).
def sigma(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

#Write a program that gets a dynamic number of input values.
#The first input is a number that represents the number of the input values following it.
#print the sum of all the input numbers.
totalInput = int(input())
dynamicNum = 0
for i in range(totalInput):
    var = int(input())
    dynamicNum += var
    if i == totalInput:
        break
print(dynamicNum)

#Write a function named is_valid that gets two strings arguments, username and password.
#The function will return True if the username and password are valid in the system, otherwise Fals
def is_valid(username, password):
    if username=="user":
        if password=="qweasd":
            return True
        else:
            return False
    elif username=="admin":
        return True
    else:
        return False

#Create a function named values that receives a list as an argument 
#and prints all of the items in the list one after the other.
def values(lst):
    length = len(lst)
    for i in range(length):
        print(f"{lst[i]}")

#Create a function named change_element that will return a modified list 
#by changing the element in an index with the value of new_element

def change_element(lst, index, new_element):
    # Write code here
    for i in range(len(lst)):
        if i == index:
            lst[i] = new_element
            break
    print(lst)
    
