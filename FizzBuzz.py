#Add a function named fizzbuzz that gets one number (int) as an argument, and:
#If the number is divisible by 3, return "Fizz".
#If the number is divisible by 7, return "Buzz".
#If the number is divisible by both 3 and 7, return "FizzBuzz".
#If none of the above conditions are met, return the number itself in a string format.
print("Welcome to FizzBuzz!")

def fizzbuzz(num):
    if (num % 3 == 0) and (num%7==0):
        return "FizzBuzz"
    elif num%7==0:
        return "Buzz"
    elif num%3==0:
        return "Fizz"
    else:
        return str(num)
    
num = int(input())
output = fizzbuzz(num)
#string_num = str(num)
print(output)
