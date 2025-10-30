# WAP to accept 2 number and 1 operator [+,-,*,/] based on operator perform calculation

n1=int(input("Enter a first  number: "))
n2=int(input("Enter a second number: "))
operator=input("Enter a operator :")


if operator =="+":
    result=n1+n2
    print(f"The result of addition is: {result}")

elif operator =="-":
    result=n1-n2
    print(f"The result of substraction is: {result}")

elif operator =="*":
    result=n1*n2
    print(f"The result of multiplication is : {result}")

elif operator =="/":
    result=n1//n2
    print(f"The result of Division is: {result}")
else:
    print("Invalid Choice")
# WAP to check whether the number is prime number or not
 











