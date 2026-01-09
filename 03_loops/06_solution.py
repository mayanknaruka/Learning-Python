# Problem: Compute the factorial of a number using a while loop.
# 5x4x3x2x1 it is called factorial numbers

number = 5
factorial = 1

while number > 0:
    # factorial = factorial * number
    # number = number - 1 
    factorial *= factorial
    number -= 1

print("factorial is: ",factorial)