#Write a program that gets one input, a number. The input number indicates how many times to execute the function. 
#Create a function that calculates the sum of all of the numbers between 1 and 10000 and prints it
num = int(input())
sum = 0
def printfunc():
    sum = 0
    for i in range(1,10001):
        sum += i
        if i>=10000:
            break
    print(f"{sum}")
for i in range(num):
    printfunc()
    if i>=num:
        break
#Write a program that gets two inputs, numbers.
#Create a function that gets two arguments
#calculates the product of them and prints it
def addNum(val1,val2):
    total = val1 * val2
    print(f"{total}")

val1 = int(input())
val2 = int(input())
addNum(val1,val2)

#Create a function that receives two arguments and returns the bigger number of the two. 
#if both are equal then return one of them.
iterations = int(input())
num1 = int(input())
num2 = int(input())

def bigger(arg1, arg2):
    if arg1 > arg2:
        return arg1
    else:
        return arg2

for i in range(iterations):
    if num1 < 2 or num2 <2:
        break
    result = bigger(num1,num2)
    if result == num1:
        num1 /= 2
        print(num1)
    elif result == num2:
        num2 /= 2
        print(num2)
