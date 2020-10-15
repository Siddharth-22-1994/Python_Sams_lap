a = 'Iam from India.India is a normal country with various culture.Good country'
b = 'Iam from USA. Usa is an advanced country'

dataa = a.split()
datab = b.split()

for val in dataa:
    for val1 in datab:
        if val == val1:
            print(val, dataa.count(val))
