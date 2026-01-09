# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.


number = 5

for i in range (1, 11):
    if i == 5:
        continue
    print(number, "x", i ,"=", number * i)



# numbers = 4 

# for i in range (1, 11):
#     if i == 5:
#         continue
#     print(numbers, "x", i, "=", numbers * i)


for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

"""
"""