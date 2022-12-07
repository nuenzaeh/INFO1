#!/usr/bin/env python3

# You can freely adopt these values to try your solution
# with different values.
plain_text = "abcdefghijklmnopqrstuvwxyz"
plain_text = plain_text.upper()
shift_by = 2

# perform a ROTn encoding
def rot_n():
    n = shift_by
    
    # You need to change the functionality of this function to
    # create the correct 'encoded' string which will be returned
    # at the end of the function.
    encoded = ""
    
    
    
    i = 0
    for c in plain_text:
        if c.isalpha():
            if c.isupper():
                x = ord(c)-64
                x = ((x + n-1)%26)+65
            else: 
                x = ord(c)-96
                x = ((x + n-1)%26)+97
            # encoded[i]= chr(x)
            encoded = encoded + chr(x)
            i +=1
        else: 
            encoded = encoded + c
            i += 1
            

    # You don't need to change the following line.
    # It simply returns the string created above.
    return encoded

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(rot_n())

