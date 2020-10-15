a = int(input())
rem = 0
while a != 0:
    i = a % 10
    rem = rem+i
    a = a/10
print(int(rem))
