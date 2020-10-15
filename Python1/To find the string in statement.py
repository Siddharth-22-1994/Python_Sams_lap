a = 'Human'
b = 'Human has various ways to live. But, Human depend mostly on SD. Best, Job for Human is Agriculture.N0 Human can line like animal.'

data = b.split()
data1 = a.split()

result = 0
for val in data:
    if val in data1:
        ans = data1.count(val)
        result = result+ans
print('The repeated string is', a, '.', 'It has been repeated for', result)
