# x = int(input())
# y = int(input())

# def decor(func):
#     def mul(x, y):
#         return x*y
#     return mul
# @decor
# def add(a, b):
#     c = a+b
#     return c
# print(add(x, y))
# --------------------------------
# ---------- Variables

# a = 5
# print(a)

# a = b = 7
# print('The value of a', a)
# print('The value of b', b)

# a, b = 2, 3
# print(a, b)

# a, b = 4  # Error
# print(a, b)

# a, b = c = 3, 4
# print(a)
# print(b)
# print(c)

# a = b, c = 7, 8
# print(a)
# print(b)
# print(c)

# a, b = c = 7, 8, 9 # Error
# print(a)
# print(b)
# print(c)

# swapping of numbers
# -----------------------------------
# Tokens
# 2.) Keywords --> Def, 33 keywords
# 3.) Literals --> string, numeric, Boolean, None, collection literals

# 4) Operators

# Arithmatic
# print(19/4)
# print(19//4)

# Assignment Operator
# a = 8
# a += 2
# print(a)

# a = 8
# b = 2
# a **= b   ---> a//=b
# print(a)

# Bitwise
# print(7 & 9)

# Logical
# a = 17
# print(not(a > 5 and a > 10))

# Membership
# a = '234'
# print('3' in a)

# Identity
# a = [1, 2, 3, 4]
# b = [1, 2, 3, 4]
# print(a is b)
# print(id(a))
# print(id(b))

# Strings
a = '  hellohow are you '
# print(a[-10:-1])
# print(a)
# print(a*2)
# print(len(a))
# print(a.lower())
# print(a.upper())
# print(a.strip())
# print(a.split('  #'))
# print(a.replace('h', 'E'))
# print('how' in a)
# print('how' not in a)

# string concat
# a = 'hello'
# b = 'world'
# # print(a+' '+b)
# format()
# name = 'sidhu'

# age = 27
# txt = 'My name is {}. Iam {} years old'
# print(txt.format(name, age))

# print('my name is {1}.Iam {0} years old'.format('sidhu', 27))

# txt = 'My name is \'sidhu\' '
# print(txt)
# --------------------------------

# Datatypes

a = 'helo'
# print(str(a))
# print(int(a))
# print(float(a))
# print(complex(a))
# print(bool(a))

# ----------------- List
l1 = [1, 2, 3, 4, 5, 'apple', 'banana', 'grapes']
# print(l1)
# print(l1[-6:-1])
# print(l1[::-1])
# print(len(l1))
# l1.reverse()

# To change the value
# l1[2] = 'mango'
# print(l1)

# for val in l1:
# print(val)

# if 2 in l1:
#     print('yes')

# Add elemnet
# l1.append('mango')
# print(l1)

# l1.insert(1, 'cherry')
# print(l1)

# delete element
# l1.pop(3)
# print(l1)

# l1.remove(1)
# print(l1)

# del l1[3]
# print(l1)

# l1.clear()
# print(l1)

# copy
# l2 = l1
# print(id(l1))
# print(id(l2))

# l2 = l1.copy()
# print(id(l2))
# print(id(l1))

# l2 = copy.copy(l1)
# print(l2)

# l2 = list(l1)
# print(id(l2))
# print(id(l1))

# a = 'hello'
# print(list(a))

# join two list
# a = [2, 3, 65, 76, -9, -0.8, 'o']
# b = ['birds', 'cars', 'bikes']
# ans = a+b
# print(ans)

# a.extend(b)
# print(a)

# for val in a:
#     a.append(val)

# print(a)

# construct a list
# new = list(('apple', 'grapes', 'all'))
# print(new)

# --------------------Tuple
t1 = (1, 2, 3, 4, 5, 2, 'r', 'i', 'u', 2, 2, 2)
t2 = ('hello', 'guys')
# print(t1)

# t2 = (3)
# t3 = (4,)
# t4 = 2
# t5 = 'u',
# print(type(t5))

# print(t1[::-1])

# print(len(t1))
# print(t1.index(4))
# print(t1.count(2))

# Converting to list we can change item in tuple
#  l2 = list(t1)
# l2.append('honey')

# ans = tuple(l2)
# print(ans)

# for val in t1:
#     print(val)

# if 3 in t1:
#     print('num')

# join tuple
# ans = t1+t2
# print(ans)

# construct tuple
# new = tuple(('s', '8', 'p'))
# print(new)

# ----------------------sets
s1 = {100, 23, -89, 1, 2, 3, 4, 'u', 'L', 'opi'}
# print(s1)

# for val in s1:
#     print(val)

# print(len(s1))

# To add elements

# s1.add('Mango')
# print(s1)

# s1.update(['cherry', 'fruits', 'apple'])
# print(s1)

# To remove elements
# s1.pop()
# print(s1)

# s1.remove(100)
# print(s1)

# s1.discard(23234)
# print(s1)

# s1.clear()
# print(s1)

# del s1
# print(s1)

#  Join sets
a = {1, 2, 3, 4, 5, 6, 'y', 'e'}
b = {'e', 'l', 'o', 'y'}

# ans = a.union(b)
# print(ans)

# ans = a.difference(b)
# print(ans)

# ans = b.difference(a)
# print(ans)

# ans = a.symmetric_difference(b)
# print(ans)

# new = set((1, 2, 3, 4, 5, 6, 7, 8, 9, 0))
# print(s1)
