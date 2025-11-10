#You are given a code.the variables a and b have missing values, 
#fill them so that the code inside the if statement will be executed!
a = 15
b = 11
c = 0
if a >= b and not b < 10:
    c = 2

c += 1
print(f"c = {c}")

#Your task is to initialize variable status based on the conditions:
#"Calm" if wind is smaller than 8,
#"Breeze" if wind is between 8 and 31 (including 8 and 31).
#"Gale" if wind is between 32 and 63 (including 32 and 63)
#"Storm" otherwise
wind = int(input()) 
status = "unset"
if wind < 8:
    status = "Calm"
elif wind >= 8 and wind<= 31:
    status = "Breeze"
elif wind >=32 and wind<= 63:
    status = "Gale"
else:
    status = "Storm"
print(f"status = {status}")

#You are given a code which gets as input two numbers n1 and n2 and a character op.
#The possible values for op are '+', '-', '/' and '*'
#set the variable result based on the conditions

n1 = int(input())
n2 = int(input()) 
op = input() 
result = 0
if op=='+':
    result = n1+n2
elif op=='-':
    result = n1 - n2
elif op=='/':
    result = n1 / n2
elif op=='*':
    result = n1 * n2

print(f"result = {result}")
