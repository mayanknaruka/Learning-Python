# Problem: Reverse a string using a loop.

input_str = "python"
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str   #reversed_str = reversed_str + char  to print same as it is python
    print(reversed_str)

