num=int(input())
count=0
for i in range(2,num):
    if(num%i==0):
        break
if(count==0 and num!=1):
    print("The num is prime")
else:
    print("The num is not-prime")
