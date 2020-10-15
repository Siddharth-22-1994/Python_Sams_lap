a = int(input())
if a % 4 == 0:
    print(a, "is a leap year")
elif a % 400 == 0:
    print(a, " is lean year")
else:
    print(a, " is not a leap year")
