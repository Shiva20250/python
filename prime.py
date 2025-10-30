# WAP to check whether the number is prime number or not


n1=int(input("Enter a number: "))
is_prime=True
i=2
while i<=n1-1:
    if(n1%i==0):
       is_prime=False 
       break
    i=i+1
if is_prime==True:
    print("The number is prime")
else:
    print("The number is not prime")


# WAP to add only odd number in list from 1 to n and print list