#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class Publication:

    def __init__(self, authors, title, year):
        self.__authors = authors  # list of authors last names
        self.__title = title  # title string
        self.__year = year  # int

    @property
    def get_authors(self):
        return self.__authors

    @property
    def get_title(self):
        return self.__title

    @property
    def get_year(self):
        return self.__year

    def __repr__(self):
        string1 = f"Publication({(self.__authors)}, \"{self.__title}\", {str(self.__year)})"
        return string1.replace("\'", "\"")

    def __str__(self):
        string1 = f"Publication({(self.__authors)}, \"{self.__title}\", {str(self.__year)})"
        return string1.replace("\'", "\"")


    def __eq__(self, other):
        return self.__authors==other.__authors and self.__title==other.__title and self.__year==other.__year

    def __hash__(self):
        return int(self.__year)

    def __lt__(self, other):#<
        return self.__authors< other.__authors

    def __le__(self, other):
        return self.__authors<= other.__authors

    def __gt__(self, other):
        return self.__authors > other.__authors

    def __ge__(self, other):
        return self.__authors >= other.__authors






# To implement the required functionality, you will also have to implement several
# of the special functions that typically include a double underscore.


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]

    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
    #print(p)
    print(s)
    print(str(p))
    print("str(p) == s",str(p) == s)
    diff = []
    for i in range(len(s)):
        if not s[i] == str(p)[i]:
                diff.append((s[i], str(p)[i]))
    print(diff)
    p1 = Publication(["A"], "B", 1234)
    p2 = Publication(["A"], "B", 1234)
    p3 = Publication(["B"], "C", 2345)
    #print("p1 == p2",p1 == p2)  # True
    #print("p2 == p3",p2 == p3)  # False

    sales = {
        p1: 273,
        p2: 398,
    }
