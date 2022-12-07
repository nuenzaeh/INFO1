#!/usr/bin/env python3

# You can freely adopt this number to print pyramids of different sizes
h = 7
def build_string_pyramid():
    j = 2
    for i in range(0, h):
        str = "1"
        print(str)
        for j in range(2, i):
            str = str + "*" + str(j)


def build_string_pyramid1():
    l = ["1"]
    print(1)
    for i in range(2,h+1):
        l.append(str(i))
        print(*l, sep = "*")
    for i in range(h-1, 0, -1):
        del(l[i])
        print(*l, sep = "*")
    return ""

    

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# See the console output and compare it to the image in the task description
print(build_string_pyramid())



