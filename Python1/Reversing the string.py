# def pypart(n):
#myList = []
# for i in range(1,n+1):
#myList.append(" * "*i)
# print("\n".join(myList))


# name=input()
# str=""
# while name!=0:
#  rev_str=str[::-1]
#  print(rev_str)
# if str==rev_str:
#   print('the given string is palindrome')
# else:
#     print('not palindrome')


def reverse(s):
    return s[::-1]


def ispalindrome(s):
    rev = reverse(s)


if (s == rev):
    return true
else:
    return false

s = ""
ans = ispalindrome(s)

if ans == 1:
    print('yes')
else:
    print('no')
