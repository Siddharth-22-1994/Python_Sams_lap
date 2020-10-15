#Setattr in class method

# simply way

class employee:
    name=''
emp=employee()
setattr(emp,'name','Geeks')
print(emp.name)


class gfg:
    name = ' '

obj = gfg()
setattr(obj,'name',"john")
setattr(obj,'discription',"CS portal")
setattr(obj, 'age','23')

print(obj.name)
print(obj.discription)
print(obj.age)



#getattr in class method
# Simple way

class employee:
    name = 'Geeks'
    age = '25'
obj = employee()
print(getattr(obj,'name'))
print(getattr(obj,'age'))


class Gfg:
    name = 'Geeks'
    age = 23
    
obj = Gfg()
print(getattr(obj, 'name')
print(getattr(obj,'Discription','CS Portal')
print(getattr(obj,age)


# Gtrattr URL:https://www.geeksforgeeks.org/python-getattr-method/
# Setattr URL:https://www.geeksforgeeks.org/python-setattr-method/