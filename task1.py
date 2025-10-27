n=int(input("Enter a number: "))

#UPPER HALF
# ROWS

i=1
while(i<=n):
    # LEFT STAR
    j=1
    while(j <= n-i+1):
        print("*",end=" ")
        j+=1

    # SPACE
    sp=1
    while(sp <= 2*(i-1)):
        print(" ", end=" ")
        sp+=1
    # RIGHT STAR
    j=1
    while(j <= n-i+1):
        print("*",end=" ")
        j+=1

    # ROW INCREMENT
    i+=1
    # MOVE Cursor To Next Row
    print()



# Lower half
# Rows
i=n-1
while(i>=1):
# Left star
 j=1
while(j<=n-i+1):
    print("*",end=" ")
    j+=1
# space
sp=1
while(sp <=2*(i-1)):
    print(" ",end=" ")
    sp+=1

 # Right Star
j=1
while(j<=n-i+1):
    print("*",end=" ")
    j+=1

# Row decrement
i-=1
# Move Cursor To Next ROW
print()

    