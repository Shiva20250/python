n=int(input("Enter a number: "))


i=n
fact=1
while i>=1:
    fact=fact * i

    i= i-1

print(f"The factorial of {n} is {fact}")
