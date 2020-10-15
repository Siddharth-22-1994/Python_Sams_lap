a=int(input())
rem=0
while a!=0:
  rem=(rem*10)+(a%10)
  a=int(a/10)
print(int(rem))
