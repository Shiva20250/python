n=int(input("Enter a number: "))

is_prime=True


if(n <=1):
    is_prime=False
 

i=2


while(i <= n-1):
    if n % i ==0:
     is_prime=False
     break

    i=i+1

if is_prime ==True:
   print(f"Number ={n} is a prime number")

else:
   print(f"Number ={n} is not a prime number")


