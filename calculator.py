import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a , b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by 0.")
    return b / a

def log(a, b):
    if b == 1:
        raise ValueError("Base cannot equal 1")
    if b <= 0:
        raise ValueError("Base must be greater than 0.")
    if a <= 0:
        raise ValueError("X must be greater than 0")
    return math.log(a, b)

def exp(a, b):
    return a**b

