n=int(input())
list=[]
rem=0

while n!=0:
    rem=int(n%2)
    list.append(rem)
    n=int(n/2)
length=len(list)
x=length-1

while x>=0:
    print(list[x])
    x=x-1
