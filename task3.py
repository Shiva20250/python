n=int(input("Enter a number: "))
i=1
while(i<=n):
    sp=1
    
    while(sp<=n-i):
     print(" ",end=" ")
     sp+=1
    j=1
    while(j<=i):
        print("*",end=" ")
        j+=1

    print()
    i+=1
