def computeGCD(a,b):
    if b==0:
        return a
    else:
        return computeGCD(b,a%b)

num1=int(input())
num2=int(input())
print(computeGCD(num1,num2))
