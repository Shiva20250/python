n=int(input("Enter a number:"))
i=1
fact=1
while i<=n:
    fact=fact*i
    i=i+1
print(f"The factorial of {n} is{fact}")