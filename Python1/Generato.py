# def with Iter

# Eg:1
# def sq():
#     for val in range(1, 11):
#         print(val*val)


# s = sq()
# myit = iter(s)
# next(myit)
# next(myit)

# Eg:2
# l = [x*x for x in range(1000000000000000000000000000000000000)]
# print(l)

# using generators
# # l1 = [x*x for x in range(1000000000000000000000000000000000000)]
# while True:
#     print(next(l1))

# Tuple complehension
# l1 = (x*x for x in range(10))
# print(type(l1))

# Eg3:
# WITHOUT FUNCTION WE CANNOT USE YIELD KEYWORD
# import time
# l1 = 5
# while l1 != 0:
#     time.sleep(2)
#     yield l1
#     l1 = l1-1


# -----------------------------------------------------------------------
# To over come above problems we need Generators
# Eg:1
# def num():
#     yield 1
#     yield 2
#     yield 3
#     yield 4


# n = num()
# print(next(n))
# print(next(n))
# print(n.__next__())
# print(n.__next__())

# Eg:2
# def sq():
#     for val in range(1, 11):
#         yield val*val


# s = sq()
# print(s.__next__())
# print(s.__next__())

# Eg:3 Real time
# import random
# import time


# def loter():
#     for val in range(20):
#         yield random.randint(0, 10)


# for val in loter():
#     time.sleep(2)
#     print(val)

# Eg: 4
# # To iterate a list using yield


# def list1(l1):
#     for val in l1:
#         yield val


# l2 = [2, 3, 4, 5]
# s = list1(l2)
# print(s.__next__())
# print(s.__next__())
# print(s.__next__())

# Eg 5
# import random
# # import sys


# def lottery():
#     for val in range(1, 4):
#         yield random.randint(1, 4)
#         # if val == 1:
#         #     print('You have agood day')
#         # elif val == 2:
#         #     print('You will meet your crush')


# l2 = lottery()
# x = l2.__next__()


# if x == 1:
#     print('Yes its 1')
# elif x == 2:
#     print('Its 2nd num')
# elif x == 3:
#     print('Its a 3rd number')
# elif x == 4:
#     print('the num is 4th number')
