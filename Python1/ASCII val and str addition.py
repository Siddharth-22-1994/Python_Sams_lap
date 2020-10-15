# Task 1
# # To convert given val to ascii and add with integer

# import functools

# a = '234r'
# ind = a[0:3]
# # print(ind)
# aval = ord(a[3])
# print('The ASCII value of r is', aval)
# l2 = []
# for val in ind:
#     l2.append(int(val))
# # print(l2)
# l2.append(aval)
# # print(l2)

# x = functools.reduce(lambda a, b: a+b, l2)
# print('The addition of 2,3,4,114 is', x)
# -------------------------------------------------------------
# Task 2
# To convert user defined val to ascii and add with integer

a = eval(input())
leng = len(a)
i = 0
rem = 0
conrem = 0
while i < leng:
    itval = a[i]
    i = i+1
    try:
        if int(itval):
            convint = int(itval)
            rem = rem+convint
        #     print('The rem is', rem)
        # else:
        #     print(ord(itval))
    except Exception:
        conval = ord(itval)
        print('The ascii value of', itval, 'is', conval)
        conrem = conrem+conval
        answer = rem+conrem
        print(answer)
# -----------------------------------------------------------------
# elif str(itval):
#     asc = ord(itval)
#     print('The asc value is', asc)
#     rem = rem+convint+asc
#     print(rem)

# if (isinstance(itval, int)):
#     print(sum(itval))
# else:
#     print(ord(itval))

# a = 't'
# if (isinstance(a, int)):
#     print(a)
# else:
#     print(ord(a))
