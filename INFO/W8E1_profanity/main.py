#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class ProfanityFilter:

    def __init__(self, keywords, template):
        self.__keywords = keywords
        self.__template = template
        self.__n = len(template)
    def __clean(self, msg):
        clean_msg = ""
        for word in msg:
            clean_msg = clean_msg + word.lower()
        print(clean_msg)
        return clean_msg

    def filter(self, msg):
        clean_msg = self.__clean(msg)
        filter_msg = clean_msg
        for word in self.__keywords:
            if word in clean_msg:
                loc = clean_msg.index(word)
                m = len(word)
                filler = (m//self.__n)*self.__template + self.__template[:m%self.__n]
                filter_msg = filter_msg[:loc]+ filler +filter_msg[loc+m:]

        return filter_msg



# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghi MasTard jklmno enBatching"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno
