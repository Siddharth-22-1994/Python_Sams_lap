# a = input()
# try:
#     b = complex(a)
#     print('Input is complex')
# except ValueError:
#     print('String')

# b = str(a)
# if b:
#     print('String type')
# else:
#     try:
#         ans = int(a)
#         print('The given input is Integer type')
#     except ValueError:
#         if float(a):
#             print('The given input is Float Type')


# try:
#     b = a.imag
#     if b:
#         print('Complex value')
# except ValueError:
#     try:
#         val = int(a)
#         print('Input is a Integer number')
#     except ValueError:
#         try:
#             val = str(a)
#             print('This is String Input')
#         except ValueError:
#             print('yes')

# elif str(a):
#     print('The given input is String Type')
# # else:
# print('Given input is complex type')

# except ValueError:
#     print('This is Boolian type')
# ---------------------------------------------
# a = input()
# try:
#     val = int(a)
#     print("Input is an integer number")
# except ValueError:
#     try:
#         val = float(a)
#         print("Input is a float  number")
#     except ValueError:
#         try:
#             val = complex(a)
#             print('Complex value')
#         except ValueError:
#             try:
#                 val = str(a)
#                 print('String type')
#             except ValueError:
#                 pass
# # --------------------------------------------------

# user_input = input("Enter your Age")
# val = None
# try:
#     val = int(user_input)
#     print("Input is an integer number. Number = ", val)
# except ValueError:
#     try:
#         val = float(user_input)
#         print("Input is a float  number. Number = ", val)
#     except ValueError:
#         try:
#             val = complex(user_input)
#             print('Complex value')
#         except ValueError:
#             try:
#                 val = bool(user_input)
#                 if val:

#                     # if val == 'True' or val == 'False':
#                     print('Bool type')
#             except ValueError:
#                 print('String type')

x = eval(input())
ans = type(x)
a = type(6)
b = type(8.9)
c = type('YU')
d = type(8+8j)
if ans == a:
    print('Integer type')
elif ans == b:
    print('Float')
elif ans == c:
    print('String')
elif ans == d:
    print('Complex')
else:
    print('Bool type')
