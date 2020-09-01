import math
import numpy as np

# Simple add function
def add(x, y):
    if isinstance(x, (int, float)) != isinstance(y, (int, float)):
        raise TypeError("Cannot add string with int/float")
    else:
        return x + y

#Calculate factorial
def factorial(x):
    sum = 1
    if x == 0:
        sum = 1
    else:
        for i in range(1, x+1):
            sum = sum*i
    return sum

# Approximate sinus function
def sin(x):
    sum = 0
    n = 50
    for i in range(n):
        sum += ((-1)**i * x**(2*i + 1)) / factorial(2*i + 1)
    return sum

# Divide function
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Just don't")
    else:
        return x/y

# Multiplication function
def multiply(x, y):
    return x * y

# Approximate e^x function
def pow_eul(x,n):
    sum = 0
    for i in range(n+1):
        sum = sum + (x**i) / factorial(i)
    return sum