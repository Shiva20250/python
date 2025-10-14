num=int(input("Enter a number: "))

remainder = num % 2
if  remainder == 0:
    print(f"Number ={num} is divisble by 2")
    print(f"Number ={num} is even")


else:
    print(f"Number={num} is  not divisble by 2")
    print(f"Number= {num} is Odd")