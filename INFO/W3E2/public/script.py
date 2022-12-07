#!/usr/bin/env python3

pwd = "aaAAAA0000++++"
pwd2 = "TEst12+++"
pwd3 = "HOwt_777"
pwd4 = "72369482"
def is_valid():
    validity = True
    if len(pwd) not in range(8,17):
        validity = False
    LC_count = 0
    UC_count = 0
    d_count = 0
    s_count = 0
    spec = ["+", "-", "*", "/"]
    for char in pwd:
        if char.islower():
            LC_count += 1
        elif char.isupper():
            UC_count += 1
        elif char.isdigit():
            d_count += 1
        elif char in spec:
            s_count += 1
        else: 
            validity = False
    if LC_count < 2 or UC_count < 2 or d_count < 2 or s_count < 2:
        validity = False
    
        
    # You need to change the following part of the function
    # to determine if it is a valid password.
    

    # You don't need to change the following line.
    return validity

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(is_valid())
# print(is_valid(pwd2))
# print(is_valid(pwd3))
# print(is_valid(pwd4))

