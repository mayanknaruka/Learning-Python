# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    number = int(input("enter the number b/t 1 to 10: "))

    if 1 <= number <=10:
        print("thanks")
        break
    else:
        print("please try again later")