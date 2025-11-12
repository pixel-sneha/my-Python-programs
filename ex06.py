#for loop
for i in range(3,28)
    print(f"Hello Coddy: {i}")
#while loop
#Write a program that gets one input, float number.
#Use a while loop to divide the input by 2 as long as the number is bigger or equal to 3.5.
#Print the first number that is smaller than 3.5.
var1 = float(input())
while var1 >= 3.5:
    var1 /= 2
print(f"{var1}")

#use of continue
#add if and continue statements so that only the even numbers will be printed (2, 4, 6, ...). 
for i in range(1, 21):
    if i % 2 == 1:
        continue
    print(i)
