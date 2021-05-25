#1. write a function called isSorted which determines if the list is in need of being sorted in either true or false

num = [1, 3, 56, 2, 8, 98, 6549, 10, -3, 1030, 0.1]
num1 = sorted(num)
# def isSorted(x = num):
#     sn = x[0]
#     gn = x[-1]
#     for i in range(1,len(x)):
#         if x[i] < sn:
#             sn = x[i]
#     for i in range(1, len(x)):
#         if x[i] > gn:
#             gn = x[i]
#     if (sn == x[0] and gn == x[-1]):
#         return True


def isSorted1(x = num):
    for i in range(0, len(x)-1):
        if (x[i] > x[i+1]):
            return False
    return True

print(isSorted1())
print(isSorted1(num1))
print(num1)