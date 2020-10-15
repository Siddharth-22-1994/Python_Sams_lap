string=input()
length=len(string)
for i in range(0,length):
    for j in range(0,i+1):
        print (string[j],end="")
    print()

     
