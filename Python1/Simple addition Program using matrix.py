m1 = [[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]]

m2 = [[2, 2, 2],
      [2, 2, 2],
      [2, 2, 2]]

sum = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

for i in range(len(m1)):
    for j in range(len(m2)):
        sum[i][j] = m1[i][j]+m2[i][j]

for num in sum:
    print(num)
