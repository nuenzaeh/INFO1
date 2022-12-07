#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def compress(data):
    l = []    
    dict1 = data[0]
    for key in dict1.keys():
        l.append(key)
        l.sort()
    t=tuple(l)
    
    compressed_data = ()+(t,)
    j = []
    for dict in data:
        v = ()
        for k in t:
            val = dict[k]
            v = v + (val,)
        j.append(v)
    compressed_data = compressed_data + (j,)
    return compressed_data

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
data = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 4, "c": 6, "b": 5}
]
print(compress(data))