n=int(input("Enter a number"))
is_prime=True

if(n<=1):
    is_prime=False


i=2
while(i<=n-1):
    if n%i==0:
        is_prime=False
        break

    i=i+1

if is_prime==True:
    print(f"The {n} is prime number ")

else:
    print(f"The number is {n} not a prime number")
    





