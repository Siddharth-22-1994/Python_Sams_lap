# Instance var, class var
# Instance meth, static meth, class meth

# To write the student details in a class
# ass students with same age

# name1 = 'name1'
# age = 20
# mark1 = 460
# grade = 'O'

# name2 = 'name2'
# age = 20
# mark2 = 340
# grade = 'A'

# name3 = 'name3'
# age = 20
# mark3 = 400
# grade = 'O'

# print(name1, age, mark1, grade)
# print(name2, age, mark2, grade)
# print(name3, age, mark3, grade)

# # ---------------------------------------


# def common(age, gender):
#     print('The students in age', age, gender)


# ans = common(20, 'Male')


# name = 'name1'
# mark = 410
# print(name, mark)


# name2 = 'name2'
# mark2 = 350
# print(name2, mark2)
# ------------------------------------

# class a:
#     age = 20
#     gender = 'Male'

#     def funinaclass(self):
#         print('The students age and gender in A class', self.age, self.gender)

#     def prof(self, name, mark):
#         print(name, mark)


# aclass = a()
# aclass.funinaclass()
# aclass.prof('name1', 456)
# aclass.prof('name2', 390)


# class b:
#     age = 17
#     gender = 'Female'

#     def funinbclass(self):
#         print('The students age and gender in B class', self.age, self.gender)

#     def prof(self, name, marks):
#         print(name, marks)


# bclass = b()
# bclass.funinbclass()
# bclass.prof('girl1', 390)
# bclass.prof('girl2', 400)

# ------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
# Learn Intro to class

# Step1
# class prof:
#     name = 'name1'
#     age = 23


# p = prof()
# print(p.name)
# print(p.age)
# ------------------------------
# Step 2
# class prof:
#     name = 'Ram'
#     age = 28

#     def profun(self):
#         print(self.name, self.age)

# p = prof()
# p.profun()
# ---------------------------------
# Step3
# class prof:
#     name = 3
#     age = 4

#     def mul(self):
#         print(prof.name*prof.age)

#     def div(self):
#         print(prof.name/prof.age)


# p1 = prof()
# p1.mul()
# p1.div()
# ------------------------------
# Step 4
# class prof:
#     def pr2(self, name, age):
#         print(name)
#         print(age)


# p2 = prof()
# p2.pr2('name1', 22)
# p2.pr2('name2', 25)
# ------------------------------
# Step 5
# Contstructors
# class prof:
#     def __init__(self, name, age):
#         print(name, age)


# p = prof('name1', 24)
# ----------------------------
# As a remedy

# class prof:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(name, age)


# p = prof('name1', 24)

# -----------------------------
# Step 6
# class prof:
#     def __init__(self, name, age): -----> diff functions
#         self.fname = name
#         self.fage = age

#     def fun1(abc):
#         print(abc.fname, abc.fage)


# p = prof('name1', 25)
# p.fun1()
# -----------------------------------
# Class destructor

# class prof:
#     def __init__(self):
#         print('This is constructor')

#     # def __del__(self):
#     #     print('Destructor called')

#     def display(self):
#         print('This is normal function')

#     def __del__(self):
#         print('Destructor is called')


# p = prof()
# p.display()
# ------------------------------------------------
# 'Self'
#  Explanation for 'Self'

# class prof:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def oper(self):
#         print(self.a**2, self.b**2)


# p = prof(2, 3)
# p.oper() == prof.oper(p)
# print(type(p.oper))
# print(type(prof.oper))

# Ref link: https://www.programiz.com/article/python-self-why
# ------------------------------------------------------------------------

# Method overloadnig
# Eg1:
# class Human:
#     def sayhello(self, name=None):
#         if name is not None:
#             print('Hello'+' ' + name)
#         else:
#             print('No name passed')

# h = Human()
# h.sayhello('Rana')
# h.sayhello()
# Same method if we pass argument it behaves differently
# If parameter is not passed it behaves differebtly

# Eg:2
# def add(datatype, *args):

#     # if datatype is int
#     # initialize answer as 0
#     if datatype == 'int':
#         answer = 0

#     # if datatype is str
#     # initialize answer as ''
#     if datatype == 'str':
#         answer = ''

#     # Traverse through the arguments
#     for x in args:

#         # This will do addition if the
#         # arguments are int. Or concatenation
#         # if the arguments are str
#         answer = answer + x

#     print(answer)


# # Integer
# add('int', 5, 6)

# # String
# add('str', 'Hi ', 'Geeks')

# Eg:3
#  Above same example Using class
# class clas1:
#     def num(self, datatype, *args):
#         if datatype == 'int':
#             for val in args:
#                 print(val, 'This is integer type')
#         elif datatype == 'str':
#             for val in args:
#                 print(val, 'This is str type')


# c = clas1()
# c.num('str', 'e', 't')
