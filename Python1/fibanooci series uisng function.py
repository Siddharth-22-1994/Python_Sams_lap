def fibanooci(x):
    n1=0
    n2=1
    count=0
    print(n1,n2,end=',')
    while count<x:
        y=n1+n2
        n1=n2
        n2=y
        count=count+1
        print(y,end=',')
n=int(input("n:"))
fibanooci(n)





#while not(len(name)>=min_length and name.isprintable() and name.isalph()):
 #   name=input("Enter your name")
#print("helle,{0}.format(name))

    
        
