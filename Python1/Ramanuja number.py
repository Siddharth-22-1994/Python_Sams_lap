# The sum of (1cube and 12cube) should be equal to sum of (9cube and 10 cube)
def cube1(a, b):
    c = (a**3)+(b**3)
    return c


x = int(input())
y = int(input())
ans1 = cube1(x, y)


def cube2(d, e):
    f = (e**3)+(d**3)
    return f


w = int(input())
z = int(input())
ans2 = cube2(w, z)

if ans1 == ans2:
    print('The result of two pairs are', ans1, 'It is Ramanuja number')
else:
    print(ans1, 'is not ramanuja number')
