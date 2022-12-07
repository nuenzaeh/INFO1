#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def absolute_value(a):
    # implement this function
    pass

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def gcd(a,b):
    if a==0 and b == 0:
        return None
    if a < 0:
        a = abs(a)
    if b < 0:
        b = abs(b)
    if a < b:
        t = a
        a = b
        b = t
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
a = -12
b = 28
print(f"greatest common divisor of {a} and {b} is = {gcd(a, b)}")

