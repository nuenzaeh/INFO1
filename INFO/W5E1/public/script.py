#!/usr/bin/env python3


# Complete the following to implement the described hamming distance function.
# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def hamming_dist(signal_1, signal_2):
    list1 = signal_1["data"]
    list2 = signal_2
    print(list1)
    print(list2)
    print(type(list1))
    print(len(list1))
    print(type(list2))
    print(len(list2))
    final = []
    if len(list1) != len(list2) or (len(list1)==0 or len(list2)==0):
        return "Empty signal on at least one of the sensors"
    # for sig1 in list1:
    for word in range(0, len(list1)):
        sig1 = list1[word]
        sig2 = list2[word]
        print(sig1 + " "+ sig2)
        if len(sig1) != len(sig2):
            return "Sensor defect detected"
        counter = 0
        for i in range(0, len(list1)):
            if not sig1[i] == sig2[i]:
                counter+=1
                # print(sig1 + " " +str(counter))
        if counter > 0:
            final.append((list1[word], signal_2[word], counter))
    return final
                
            

# The following lines print your function's output for an exemplary input to the console.
# Note that this does not include any of the mentioned edge cases for defective sensors or signals of different lenghts.
# Try to write your own tests for this.

# signal_sensor_1 = {"times": [0, 1, 2, 3, 4, 5],
#                    "data": ["00101110", "11001011", "11110000", "01000011", "11001101", "00011011"]}
# signal_sensor_2 = ("00101110", "11001001", "11110011", "01111011", "11001101", "00011011")
# print(hamming_dist(signal_sensor_1, signal_sensor_2))
signal_sensor_1 = {"times": [0, 1, 2, 3, 4, 5],
                   "data": ["11001011", "00101110"]}
signal_sensor_2 = ("11001001", "00101110")
print(hamming_dist(signal_sensor_1, signal_sensor_2))
# d("foobar", "cooler") = 3

# d("shift", "tshif") = 5

# d("00101", "00111") = 1