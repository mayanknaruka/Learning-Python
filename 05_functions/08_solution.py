# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value} ")

print_kwargs(name = "mayank", age=20, city="jaipur")
print_kwargs(language="Python", version=3.12)
