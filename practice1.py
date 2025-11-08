num=int(input("Enter a number:"))
factors=[]

for i in range(1,num+1):
    if num % i==0:
        factors.append(i)


if len(factors)==2:
    print(f"Number {num} is prime number")
    print(f" its two factors are{factors}")

else:
    print(f"Number {num} is not prime number")
    print(f"All its factors are:{factors}")