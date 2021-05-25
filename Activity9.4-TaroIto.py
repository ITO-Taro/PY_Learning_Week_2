# 1. function that when given a string will restult in a Boolean value to determine whether or not the given string is a palindrome

def plndrmChecker(x):
    for i in range(0, int(len(x)/2)):
        if x[i] != x[len(x)-i-1]:
            return False
    return True
print(plndrmChecker("racecar"))
print(plndrmChecker("multidimensional"))

