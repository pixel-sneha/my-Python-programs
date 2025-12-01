print("Welcome to FizzBuzz!")

def fizzbuzz(num):
    if (num % 3 == 0) and (num%7==0):
        return "FizzBuzz"
    elif num%7==0:
        return "Buzz"
    elif num%3==0:
        return "Fizz"
    else:
        if "3" in str(num):
            return "Almost Fizz"
        else:
            return str(num)

print("Enter number of iterations: ")
iteration = int(input())
for i in range(1,iteration+1):
    num = i
    output = fizzbuzz(num)
    print(output)
