#!/usr/bin/env python3

# Height in M
height = 1.8
# Weight in KG
weight = 80


# Determine the BMI. Change the function
# below to calculate the BMI return which category the result is in.
# Your implementation should work with any specific value.
# You must use the variables defined above.


def get_bmi_category():
    # You need to change the following part of the function
    # to determine the BMI and return the correct category.
    if height<= 0 or weight < 0:
        return "N/A"
    bmi = weight / height**2
    cat = ""
    if bmi <= 18.5:
        cat = "Underweight"
    elif bmi <=25:
        cat = "Normal Weight"
    elif bmi <= 30:
        cat = "Pre-Obesity"
    elif bmi <= 35:
        cat = "Obesity class I"
    elif bmi <= 40:
        cat = "Obesity class II"
    elif bmi > 40:
        cat = "Obesity class III"
    else:
        cat = "N/A"
    
    # bmi = round(bmi, 2)
    
    bmi = "{:.2f}".format(bmi)
    # Return the BMI values and the correct category after you have calculated the BMI.
    return f"BMI: {bmi}, Category: {cat}"

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(get_bmi_category())