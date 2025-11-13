#Write a program that receives one input, an integer, 
#calculates the factorial of the input and prints it.
findfact = int(input())
i = 1
for i in range(1,findfact):
    findfact *= i;
    if i==findfact:
        break
print(f"{findfact}")

#Write a program that gets a dynamic number of input values.
#The first input is a number that represents the number of the input values following it.
# print the sum of all the input numbers
total = int(input())
initial = 0
for i in range(total):
    var = int(input())
    initial += var
    if var==total:
        break
print(f"{initial}")
