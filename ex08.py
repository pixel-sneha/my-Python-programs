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

