h = 47


def build_string_pyramid(h = h):
    j = 2
    total=""
    for i in range(2, h+2):
        string = "1"
        for k in range(2, i):
            string = string + "*" + str(k)
        total = total + string + "\n"
    if h > 99:
        for i in range(h, 99, -1):
            string = string[:-4]
            total = total + string + "\n"
        for i in range(99, 9 , -1):
            string = string[:-3]
            total = total + string + "\n"
        for i in range(9, 1, -1):
            string = string[:-2]
            total = total + string + "\n"
    elif h > 9:
        for i in range(h, 9 , -1):
            string = string[:-3]
            total = total + string + "\n"
        for i in range(9, 1, -1):
            string = string[:-2]
            total = total + string + "\n"
    if h <10:
        for i in range(h,1,-1):
            string = string[:-2]
            total = total + string + "\n"

        string = string[:-2]
        total = total + string + "\n"
    return total
#print(build_string_pyramid())
print(build_string_pyramid(110))