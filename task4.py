n=int(input("Enter a number: "))

i=n
while(i>=1):
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