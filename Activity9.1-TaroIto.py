# 1. function that takes 3 different numbers as a parameter
# 2. sort this list in any way other than using built in methods (i.e., sort)

num = [4, 7, 1]
num2 = [1, 5, 2]
def listSort(x = num):
    if x[0]>x[1] and x[0]>x[2] and x[1]>x[2]:
        return (x[0], x[1], x[2])
    elif (x[0]>x[1] and x[0]>x[2] and x[2]>x[1]):
        return (x[0], x[2], x[1])
    elif (x[0]<x[1] and x[1]>x[2] and x[0]>x[2]):
        return (x[1], x[0], x[2])
    elif x[0]<x[1] and x[1]>x[2] and x[0]<x[2]:
        return (x[1], x[2], x[0])
    elif x[2]>x[1] and x[2]>x[0] and x[1]>x[0]:
        return (x[2], x[1], x[0])
    elif x[2]>x[1] and x[2]>x[0] and x[0]>x[1]:
        return (x[2], x[0], x[1])

print(listSort())
print(listSort(num2))
print(max(num))