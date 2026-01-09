# Problem: Write a generator function that yields even numbers up to a specified limit.


def even_number(limit):
    for num in range(2, limit+1, 2):
     yield num


for n in even_number(10):
   print(n)
   