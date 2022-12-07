#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):
        return False
    f1 = open(path_reading, 'r')
    contents = f1.readlines()
    print(contents)
    print(len(contents))
    f2 = open(path_writing, 'w')
    if len(contents) == 0:
        return f2
    f2.write("Firstname,Lastname\n")
    if len(contents) == 1:
        return f2
    for name in contents[1:]:
        n = name.split("; ")
        if len(n) == 2:
            pre = n[1]
            pre = pre[:-1]
            print(pre)
            new = pre+","+n[0]+"\n"
            
            f2.write(new)
        else:
            n = n[0].split(" ")
            if len(n) == 2:
                new = n[0]+","+n[1]
                print(new)
            if len(n) == 1:
                new = ","+n[0]
                print(new)
            f2.write(new)
            
    return path_writing


# The following line calls your solution function with the provided input file
# and then attempts to read and print the contents of the resulting output file.
# You do not need to modify these lines.
INPUT_PATH = "my_data.txt"
OUTPUT_PATH = "my_data_processed.txt"
process_data(INPUT_PATH, OUTPUT_PATH)
# if os.path.exists(OUTPUT_PATH):
#     with open(OUTPUT_PATH) as resultfile:
#         print(resultfile.read())
# else:
#     print("No output file exists")

