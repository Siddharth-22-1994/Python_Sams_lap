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

import math
x = 9
# print(int(math.pow(x, 2)))
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

# ----------------dict
d1 = {'a': 100, 'b': 200, 'c': 300}
# print(d1)

# Access items using keys
# print(d1['a'])

# change values using keys
# d1['a'] = 345
# print(d1)

# using get() method
# print(d1.get('a'))

# loop througn dict
# for val in d1:
#     print(val)

# for val in d1.keys():
#     print(val)

# for val in d1.values():
#     print(val)

# for val, val1 in d1.items():
#     print(val, val1)

# print(len(d1))

# add new item
# d1['d'] = 400
# print(d1)

# -------- remove Items
# print(d1.pop('a'))
# print(d1)

# print(d1.popitem())  # remove last item
# print(d1)

# print(d1.clear())
# print(d1)

# Nested dict

# parent = {
#     'c1': {
#         'name': 'sidhu',
#         'age': 26
#     },
#     'c2': {
#         'name': 'sid',
#         'age': 25
#     },
#     'c3': {
#         'name': 'kal',
#         'age': '24'
#     },
# }

# print(parent)

# dict constructor
# newdict = dict(fname='Sidhu', sname='T')
# print(newdict)

# --------if ------

# only if
# if-else
# if elif else

a = 8
# if a:
#     print('yes')

# if a > 5:
#     print('Greater than 5')

# x = int(input()) --> user defined input
# if x > 10:
#     print(a, 'is greater than 10')
# else:
#     print(a, 'less than 10')

# mark = 89
# if mark > 90:
#     print('A grade')
# elif mark > 70:
#     print('B grade')

# mark = int(input())
# if mark > 90 and mark <= 100:
#     print('O grade')
# elif mark > 70 and mark <= 89:
#     print('A grade')
# elif mark > 60 and mark <= 69:
#     print('B grade')
# elif mark < 40 and mark <= 59:
#     print('C grade')
# else:
#     print('No grade')

# Shorthand if/ Ternary Operator
# a = 2
# print('yes') if a > 5 else print('No')

# mark = int(input())
# print('O grade') if mark > 90 and mark <= 100 else print('A grade') if mark > 70 and mark <= 89 else print(
#     'B grade') if mark > 60 and mark <= 69 else print('C grade')

# Exercise Programs ---> Eligible to vote, Odd or even, Leap year....

# ----------> for loop ------------
# To print num from 1-10
# for val in range(1, 11, 2):  # - -> It skips 1 value
#     print(val)

# for val in range(20, 2, -2):
#     print(val)
# else:
#     print('Iteration completed')

a = 'Hello world'
# for val in a:
#     print(val)

# loop through List, set, tuple, dictionary
l1 = ['a', 'j', 'k', 'o', 89]
# for val in l1:
#     print(val)

# By using range() method to list
# for val in range(len(l1)):
#     print(val, l1[val])

# Using break statement
# for val in range(1, 10):
#     print(val)
#     if val == 6:
#         break

# for val in l1:
#     if val == 'o':
#         break
#     print(val)

# Continue Statement
# for val in l1:
#     if val == 'k':
#         continue
#     print(val)

# Nested for loop
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for val in adj:
#     for val1 in fruits:
#         print(val, val1)

# for val in range(0, 6): # to print square shape
#     for val1 in range(0, 6):
#         print('*', end=' ')
#     print()

# for val in range(0, 6):
#     for val1 in range(0, val+1):
#         print('*', end=' ')
#     print()

# Exercise Programs :To print tables, Sum of num in a list

# While loop
# i = 0
# while i < 7:
#     print(i)
#     i += 1

# break
# i = 0
# while i < 10:
#     print(i)
#     i += 1
#     if i == 8:
#         break

# continue
# i = 0
# while i < 10:
#     i += 1
#     if i == 6:
#         continue
#     print(i)

# else
# i = 0
# while i < 8:
#     print(i)
#     i += 1
# else:
#     print('Iteration over')

# -------------------------------function

# Function without args
# def hello():
#     print('Hello world')


# hello()

# Func with args
# def hello(name):
#     print('My name is', name)


# hello('Sidhu')
# hello('name2')
# hello('name3')

# Exercise sum of num
# def add(a, b):
#     return a+b


# print(add(5, 7))

# --- Positional args(based on the position)
# def prof(name, age):
#     print('My name is {}. My age is {}'.format(name, age))


# prof('sidhu', 26)

# --- Default args
# def prof(name, age, place='cbe'):
#     print('My name is {}. My age is {}. Iam from {}'.format(name, age, place))


# prof('sidhu', 26)

# keyword args
# def prof(name, place, age):
#     print('My name is {}. My age is {}. Iam from {}'.format(name, age, place))


# prof(age=26, name='Sid', place='cbe')

# --- Variable length
# def prof(*name):
#     print('My name is', name)


# prof('sidhu', 'sid', 'somename')

# def prof(*name):
#     for val in name:
#         print('My name is', val)


# prof('sidhu', 'sid', 'somename')

# Exception variable length args
# def prof(*name, age):
#     print('My name is', name, 'my age is', age)


# prof('sidhu', 'sid', 'somename', 26)

# ----------------- scope of variable
# Nested func
# x = 6  # global scop


# def outer():
#     x = 8  # local scope

#     def inner():
#         y = 9  # enclosed scope
#         print(y)
#         print(x)
#     inner()


# outer()

# Global variable

# x = 6
# def outer():
#     global x
#     x = x+1
#     print(x)


# outer()

# nonlocal variable
# def outer():
#     x = 8

#     def inner():
#         y = 9
#         nonlocal x
#         x += 1
#         print(y)
#         print(x)
#     inner()


# outer()

# --------------------------------- class
# class prof:
#     name = 'Sidhu'
#     age = 26
#     print(name, age)


# p = prof()

# --- Print while calling the func
# class prof:
#     name = 'Sidhu'
#     age = 26


# p = prof()
# print(p.name, p.age)

# --- Use methods in class
# class prof:
#     name = 'sidhu'
#     age = 26

#     def disp(self):
#         print(self.name, self.age)


# p = prof()
# p.disp()

# --- defining args in class
# class prof:
#     def disp(self, name, age):
#         print(name, age)


# p = prof()
# p.disp('Sidhu', 26)

# --- Using constructor
# class prof:
#     def __init__(self, name, age):
#         print(name, age)


# p = prof('Sidhu', 26)

# --- using method to disp code in class
# class prof:
#     def __init__(self, name, age):
#         self.fname = name
#         self.fage = age

#     def disp(self):
#         print(self.fname, self.fage)


# p = prof('Sidhu', 26)
# p.disp()

# -------------- Inheritance
# --- Single
# class Animal:
#     def speak(self):
#         print("Animal Speaking")

# # ---  child class Dog inherits the base class Animal


# class Dog(Animal):
#     def bark(self):
#         print("dog barking")


# d = Dog()
# d.bark()
# d.speak()

# ---- Multilevel
# class Animal:
#     def speak(self):
#         print("Animal Speaking")

# # ---  child class Dog inherits the base class Animal


# class Dog(Animal):
#     def bark(self):
#         print("dog barking")


# class cat(Dog):
#     def mew(self):
#         print('Cat mews')


# d = cat()
# d.bark()
# d.speak()
# d.mew()

#  --- Heirarcal
# class Animal:
#     def speak(self):
#         print("Animal Speaking")

# # ---  child class Dog inherits the base class Animal


# class Dog(Animal):
#     def bark(self):
#         print("dog barking")


# class cat(Animal):
#     def mew(self):
#         print('Cat mews')


# a = Animal()
# a.speak()

# d = Dog()
# d.bark()

# c = cat()
# c.mew()

# ------ Multiple
# class Calculation1:
#     def Summation(self, a, b):
#         return a+b


# class Calculation2:
#     def Multiplication(self, a, b):
#         return a*b


# class Derived(Calculation1, Calculation2):
#     def Divide(self, a, b):
#         return a/b


# d = Derived()
# print(d.Summation(10, 20))
# print(d.Multiplication(10, 20))
# print(d.Divide(10, 20))
