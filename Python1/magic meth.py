# Examples

# n = 6
# x = n.__add__(6)
# y = n.__sub__(7)
# z = n.__mul__(2)
# c = n.__floordiv__(2)
# a = n.__mod__(8)
# m = n.__pow__(2)
# print(x)
# print(y)
# print(y)
# print(m)

# ------------------------------------------
# Binary Operators

# Operator	Method
# +	object.__add__(self, other)
# -	object.__sub__(self, other)
# *	object.__mul__(self, other)
# //	object.__floordiv__(self, other)
# /	object.__truediv__(self, other)
# %	object.__mod__(self, other)
# **	object.__pow__(self, other[, modulo])
# <<	object.__lshift__(self, other)
# >>	object.__rshift__(self, other)
# &	object.__and__(self, other)
# ^	object.__xor__(self, other)
# |	object.__or__(self, other)
# ------------------------------------------------
# Extended Assignments
# Operator	Method
# +=	object.__iadd__(self, other)
# -=	object.__isub__(self, other)
# *=	object.__imul__(self, other)
# /=	object.__idiv__(self, other)
# //=	object.__ifloordiv__(self, other)
# %=	object.__imod__(self, other)
# **=	object.__ipow__(self, other[, modulo])
# <<=	object.__ilshift__(self, other)
# >>=	object.__irshift__(self, other)
# &=	object.__iand__(self, other)
# ^=	object.__ixor__(self, other)
# |=	object.__ior__(self, other)
# ---------------------------------------------------
# Unary Operators
# Operator	Method
# -	object.__neg__(self)
# +	object.__pos__(self)
# abs()	object.__abs__(self)
# ~	object.__invert__(self)
# complex()	object.__complex__(self)
# int()	object.__int__(self)
# long()	object.__long__(self)
# float()	object.__float__(self)
# oct()	object.__oct__(self)
# hex()	object.__hex__(self)
# ---------------------------------------------------
# Comparison Operators
# Operator	Method
# <	object.__lt__(self, other)
# <=	object.__le__(self, other)
# ==	object.__eq__(self, other)
# !=	object.__ne__(self, other)
# >=	object.__ge__(self, other)
# >	object.__gt__(self, other)
# ---------------------------------------------------------
# Eg:2


# class student:
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2
#         # print(self.m1+self.m2)

#     def fun1(self, other):
#         m1 = self.m1+other.m1
#         m2 = self.m2+other.m2
#         s3 = student(m1, m2)

#         return s3


# s1 = student(2, 6)
# s2 = student(3, 1)

# s3 = s1+s2

# print(s3)
# print(s3.m2)


# Eg:4 __new__
# ----------------------
# class player:
#     total_obj = 2
#     curr_obj = 0

#     def __new__(cls, *args):
#         if(cls.curr_obj >= cls.total_obj):
#             raise ValueError('More than 2 Objects')
#         cls.curr_obj += 1
#         return super().__new__(cls)

#     def __init__(self, name, health):
#         self.name = name
#         self.health = health

#     def get_name(self):
#         return self.name

#     def get_health(self):
#         return self.health


# obj1 = player('sam', 103)
# obj2 = player('john', 35)
# obj3 = player('ji', 26)

# print(obj1.get_name())
# print(obj1.get_health())
# print(obj2.get_name())
# print(obj2.get_health())


# Eg:5
# -----------------------
# https://www.journaldev.com/22761/python-callable-__call__

# # __call__
# class prof:
#     def __init__(self, name):
#         self.name = name

#     def __call__(self, age, height):
#         return age, height


# p = prof('name2')
# age1 = p(24, 164)
# print('My age is', age1)

class prof:
    def __init__(self, name):
        self.name = name
        print(name)

    def __call__(self, age):
        print('Age is', age)


p = prof('Hisname')
p(34)

# class person:
#     i = 0

#     def __init__(self, id):
#         self.i = id


# p = person(10)
# print(callable(p))
# print(callable(person))

# class Employee:
#     id = 0
#     name = ' '

#     def __init__(self, i, n):
#         self.id = i
#         self.name = n

#     def __call__(self, *args, **kwargs):
#         print('Printing args')
#         print(*args)

#         print('Printing Kwargs')
#         for v, v1 in kwargs.items():
#             print(v, v1)


# e = Employee(10, 'Puni')
# if callable(e):
#     e()

#     e(10, 20)

#     e(10, 30, {'f': 12, 'r': 89})

#     e(10, 'A', name='po', id=20)
