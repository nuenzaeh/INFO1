#!/usr/bin/env python3

# use this list of presumably known Whatsapp numbers to check
# whether a trial nr from the function below exists in Whatsapp.
# Note that the grading framework might use different numbers here.
wa_nrs = ["0781111119", "0792653913", "0797763139", "0792793193", "0781139022", "0764320165"]


# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def get_possible_nrs(n):
    possible_nrs_for_juliet = []
    for i in range(2,10):
        print(i)
        for j in range (0,10):
            test = n[0:i] + str(j) + n[i:9]
            print(test)
            if test in wa_nrs:
                if not test in possible_nrs_for_juliet:
                    possible_nrs_for_juliet.append(test)
    return possible_nrs_for_juliet

    # Don't forget to return your result

# For this particular number, the function should find the
# last element in wa_nrs
print(get_possible_nrs("076432165"))


