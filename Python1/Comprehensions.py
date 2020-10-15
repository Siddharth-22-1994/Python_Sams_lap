# Zip method

# a = [2, 3, 4, 5]
# b = ['q', 'e', 'r', 't']
# s = list(zip(a, b))
# print(s)
# ----------------------------------------------
# List comprehension
# x = [2, 3, 4, 5]

# print([a*10 for a in [2, 3, 4, 5]])
# or
# b = [a*10 for a in x]
# print(b)
#  or
#  print([x for x in range(1,11) if x%2==0])
# ---------------------------------------------
# Set comprehension
n = [1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 10]
# # print(set(n))

# Using set Comprehension

s1 = {x*2 for x in n}
# print(s1)

# Eg:2
# sentence = {'girl', 'boy', 'howmany', 'Go'}
# unique_words = {word for word in sentence if len(word) <= 3}
# print(unique_words)
# ------------------------------------------
# Dictionary comprehension
a = [2, 3, 4, 5]
b = ['q', 'e', 'r', 't']
# {2: 'q', 3: 'e', 4: 'r', 5: 't'} ---> to get this Output
# d1 = {}
# for val, val1 in zip(a, b):
#     d1[val] = val1
# print(d1)

# Using dict Comprehension
# d1 = {val: val1 for val, val1 in zip(a, b)}
# print(d1)


# print({k: v**3 for (k, v) in zip(string.ascii_lowercase, range(26))})
