l1 = [2, 3, 4, 5, 2, 3]
l1.sort()
for i in range(len(l1) - 1):
    if l1[i] == l1[i+1]:
        print(l1[i])
