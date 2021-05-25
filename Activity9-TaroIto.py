day9List = ["toyota", "nissan", "honda", "ford", 'ram', 'gmc']
day9List2 = ["Tundra", "Titan", ["F150", "Raptor"], ["Ram 1500", "Rebel"], "Seirra", "Silverado"]

# 1. function that prints out all the values in the list

# def listPrinter(x = day9List):
#     for i in list(x):
#         print (i)
    
# print(listPrinter())


# # 2. function that takes one intger as a parameter and prints out my name as many times as specified

# def namePrinter(x):
#     for n in range(x):
#         print ("Taro Ito")

# print(namePrinter(10))

# # def namePrinter(x):
# #     print("Taro Ito\n" * x)
# # print(namePrinter(5))


# # CHALLENGE (multidimensional list)
# day9List2 = ["Tundra", "Titan", ["F150", "Raptor"], ["Ram 1500", "Rebel"], "Seirra", "Silverado"]
# def listPrinter2(x):
#     for (i) in list(x):
#         if (i == x[0]):
#             print(i)
#         elif (i == x[1]):
#             print(i)
#     for (i) in list(x[2]):
#         if (i == x[2][0]):
#             print (i)
#         elif (i == x[2][1]):
#             print (i)
#     for (i) in list(x[3]):
#         if (i == x[3][0]):
#             print(i)
#         elif (i == x[3][1]):
#             print (i)
#     for (i) in list(x):
#         if (i == x[4]):
#             print(i)
#         elif (i == x[5]):
#             print(i)
            
# print(listPrinter2(day9List2))


# num = [1, 3, 56, 2, 8, 98, 6549, 10, -3, 1030, 0.1]
# def isSorted(x = num):
# 	for i in range (1, len(x), 1):
# 		if x[i] < x[0]:
# 			x[0] = x[i]
#                 return x[0]   
# print(isSorted())


def spaceDeleter(y):
    return y.replace(" ", "")

def spaceDeleter1(z):
    return "".join(z.split())

print(spaceDeleter("taro Iro"))
print(spaceDeleter1("maureen joyce myrtil"))