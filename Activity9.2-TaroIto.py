# 1. function that is equivalent to list.max()

num = [1, 3, 56, 2, 8, 98, 6549, 10, -3, 1030, 0.1]
# def maxNum(x = num):
#     x.sort()
#     return x[-1]
# print(maxNum())

# def minNum(x = num):
#     x.sort()
#     return x[0]
# print(minNum())

def maxNum1(x = num):
    for i in range(1, len(x), 1):
        if (x[i] > x[0]):
                x[0] = x[i]
    return x[0]


# print(maxNum())           
print(maxNum1())

# print(num[0:11])
