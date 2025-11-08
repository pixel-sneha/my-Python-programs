# replace the question marks of the variables b1 and b2 so that b3 evaluates to True.
b1 = 1
b2 = 2
b3 = not (b1 + b2) < (b1 * b2)
print(f"b3 = {b3}")

# place the question marks of the variables b1, b2  and b3 so that b4 will hold True.
b1 = True
b2 = True
b3 = False

b4 = b1 and b2 and (not b3)
print(f"b4 = {b4}")
