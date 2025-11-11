#tore the inputs in two variables, 
#cast them to float and print the multiplication of the two.
var1 = input()
var2 = input()
var1 = float(var1)
var2 = float(var2)
# var1 = float(input()) will work the same
result = var1 * var2
print(f"{result}")

#Write a program that gets input from the user, his age.
#The program will output (print) the number of missing years till 120
userAGE = int(input())
result = 120 - userAGE
print(f"{result} years till 120")

#Write a program that gets an input from the user, a number, 1 or 0.
#The program will output "T" if the input is 1 and "F" otherwise.
userInput = int(input())
if userInput==0 :
    print("F")
elif userInput==1 :
    print("T")
