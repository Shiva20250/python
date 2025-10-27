#wap to print odd number from 1 to n

n=int(input("Enter a number: "))

i=1
while i<=n:
    print(i)
    i=i+2

print("----------------------------------------")
n=int(input("Enter a number: "))
for i in range(1,n,2):
    print(i)
