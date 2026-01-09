# Problem: Write a decorator that measures the time a function takes to execute.

import time

def time(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result