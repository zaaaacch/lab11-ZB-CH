import math

# https://github.com/zaaaacch/lab11-ZB-CH
# Partner 1: Zach Beattie
# Partner 2: Cooper Hayes

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""


def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError()

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a , b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by 0.")
    return b / a

def logarithm(a, b):
    if b == 1:
        raise ValueError("Base cannot equal 1")
    if b <= 0:
        raise ValueError("Base must be greater than 0.")
    if a <= 0:
        raise ValueError("X must be greater than 0")
    return math.log(a, b)

def exp(a, b):
    return a**b

