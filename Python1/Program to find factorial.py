a=int(str(input()))
fact=1
if a<0:
  print('Negative num does not have any factorial')
elif a==0:
  print('The facorial of 0 is 1')
else:
  for i in range (1,a+1):
       fact=fact*i
       print(fact)


  #Note: int(STR(input())), in this STR is a notable one.....
