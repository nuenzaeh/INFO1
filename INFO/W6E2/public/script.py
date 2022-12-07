#You are completely free to change this variables to check your algorithm.
num1 = 28

num2 = 26
def divisors(n):
    s = 0
    for j in range(1, n+1):
        if(n%j==0):s = s+j
    return s

# def sum_of(divisors):
#     s = 0
#     for i in divisors:
#         s = s+i
#     return s
#Function to check whether two numbers are friendly pairs or not.
def isFriendlyPair():
    if not (num1>0 and num2>0) or num1==num2 or not(isinstance(num1, int) and isinstance(num2,int)):
        return "Invalid"
    s1 = divisors(num1)
    s2 = divisors(num2)
    a1 = s1/num1
    a2 = s2/num2
    if a2 != a1: return False
    #You need to complete this function.
    #You need to return a boolean variable . If num1 and num2 are friendly pairs return True. 
    # If they are not return False. 
    # The numbers must be valid according to description before determining friendly parity situations. 
    # Return "Invalid" if they are not valid.
   
    return True

#This line prints your method's return so that you can check your output.
print(isFriendlyPair())