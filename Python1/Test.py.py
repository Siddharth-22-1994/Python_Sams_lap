n = int(input())
for i in range(n, 0, -1):
    for j in range(0, n-1):
        print(end="")
    for j in range(0, i):
        print("*", end="")
    print()
