num=int(input())
length=len(str(num))
sum=0
temp=num
while temp!=0:
    t=temp%10
    sum=sum+(t**length)
    temp=int(temp/10)
if sum==num:
    print(num, 'is an amstrong number')
else:
    print(num, 'is not an amstrong number')