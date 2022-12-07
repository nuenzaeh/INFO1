#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.

def analyze(posts):
    dict1 = {}
    for post in posts:
        for word in post.split():
         
        # checking the first character of every word
            if word[0] == '#':
                if word[1].isalpha():
                    hashtag = word[1:]
                    if hashtag in dict1.keys():
                        dict1[hashtag] += 1
                    else:
                        dict1[hashtag] = 1
           
            
                
    return dict1


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(analyze(["",
                  "good morning #90zurich #limmat",
                  "spend my #weekend in #zurich",
                  "#Zurich <3"]))
posts = [
    "hi #weekend",
    "good morning #zurich #limmat",
    "spend my #weekend in #zurich",
    "#zurich <3"]
print(analyze(posts))
analyze(["",
                  "good morning #90zurich #limmat",
                  "spend my #weekend in #zurich",
                  "#Zurich <3"])
