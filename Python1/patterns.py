# Right angled triangle
# for row in range(0, 5):
#     for col in range(0, row+1):
#         print('*', end=' ')
#     print()

# # inverted right angld triangle

# for val in range(5, 0, -1):
#     for col in range(0, val):
#         print('*', end=' ')
#     print()

# Triangle
# n = int(input())
# for row in range(0, n):
#     for col in range(0, n-row-1):
#         print(end=' ')
#     for j in range(0, row+1):
#         print('*', end=' ')
#     print()

# Inverted triangle
# n = int(input())
# for row in range(n, 0, -1):
#     for col in range(0, n-row):
#         print(end=' ')
#     for col in range(0, row):
#         print('*', end=' ')
#     print()

# --------------------------------------
# for row in range(5, 0, -1):
#     for col in range(0, row):
#         print('*', end=' ')
#     print()

# n = int(input())
# for val in range(1, n+1):
#     print('* '*val)
# a = eval(input())
# print(type(a))

# for row in range(0, 5):
#     for col in range(1, row+1):
#         print('*', end=' ')
#     print()
# for val in range(6):
#     print('*'*val)
# print()

# for val in range(5, 0, -1):
#     for val1 in range(0, val+1):
#         print('* ', end=' ')
#     print()

# n = int(input())
# for val in range(0, n+1):
#     print(' '*(n-val), ' *' * val)
# for val in range(n-1, 0, -1):
#     print(' '*(n-val), ' *' * val)

# Using Nested while
# To print right angled trinagle
# i = 1
# while i < 11:
#     j = 0
#     while j < i:
#         print('*', end='')
#         j = j+1
#     print()
#     i = i+1

# For info
# i = 0
# while i < 10:
#     j = 0
#     while j < 10:
#         print(i, j)
#         j = j+1
#     i = i+1
