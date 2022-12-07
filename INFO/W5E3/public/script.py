from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
 ] 

def reverse_index(dataset):
    index_dictionary = {}
    for i in range(0,len(dataset)):
        s = dataset[i]
        s = s.lower()
        list = s.split()
        for word in list:
            if word in index_dictionary.keys():
                index_dictionary[word].append(i)
                               
            else:
                index_dictionary[word] = [i]
    
    return index_dictionary


    # don't forget to return your resulting dictionary

# You can see the output of your function here
print(reverse_index(dataset))
