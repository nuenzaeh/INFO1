#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def merge(a, b):
    mergelist = []
    if len(a) == 0 or len(b)== 0:
        return mergelist
    if len(a) == len(b):
        mergelist = [(a[i], b[i]) for i in range(0, len(a))]
        return mergelist
    if len(a) > len(b):
        n = b[len(b)-1]
        for i in range(len(b), len(a)):
            b.append(n)
        mergelist = [(a[i], b[i]) for i in range(0, len(b))]            
        return mergelist
    if len(a) < len(b):
        m = a[len(a)-1]
        for i in range(len(a), len(b)):
            a.append(m)
        mergelist = [(a[i], b[i]) for i in range(0, len(a))]
        return mergelist
        
    



# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(merge([0, 1, 2], [5, 6]))
print(merge([0, 1, 2], [5, 6, 7])) # should return [(0, 5), (1, 6), (2, 7)]
print(merge([2, 1, 0], [5, 6]))    # should return [(2, 5), (1, 6), (0, 6)]
print(merge([], [2, 3])    )       # should return []