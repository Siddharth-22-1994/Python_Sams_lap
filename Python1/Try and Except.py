# IO Error
# try:
#     f = open('notes.txt', 'r')
#     s = f.readline(3)
#     print(s)
# except Exception:
#     print('No file found')


# EOF Error
try:
    while True:
        data = input('prompt:')
        print('READ:', data)
except EOFError as e:
    print(e)

# Type Error
# try:
#     a = [2, 3, 4, 'i', 'o']
#     print(sum(a))
# except TypeError as e:
#     print(e)

# # Using Raise Keyword
# try:
#     a = int(input())
#     if a < 18:
#         raise Exception
# except Exception:
#     print('Not eligible to vote')


# Nested Try Block
# Eg:1

# try:
#     print('In 1st Try')
#     try:
#         print('In 2nd Try')
#     except Exception as e:
#         print(e)
#     finally:
#         print('Nested Try conmpleted')
# except Exception:
#     try:
#         print('Try inside Except')
#     except Exception:
#         print('Block error')
#     finally:
#         print('Main try Completed')

# Eg:2 (impXXXXX)
# try:
#     a = int(input())
#     if a <= 0:
#         print('Age cannot be negative')
#     elif a > 0 and a <= 17:
#         raise Exception
#     else:
#         print('Eligile to vote')
# except Exception:
#     try:
#         if a < 18:
#             raise Exception
#     except Exception:
#         print('Not eligible to vote')
# finally:
#     print('Code Completed')


# defanition
# types of error
# why to use
# where to use
# try and except syntax
