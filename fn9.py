def calculateFactorial(number:int):

    # for negative number handling
    if number < 0:
        return -1

    if(number == 0 or number == 1):
        return 1
    
    return number * calculateFactorial(number-1)


num = int(input("Enter a number to calculate factorial: "))

ans = calculateFactorial(num)
# if(ans == -1):
#     print("Since you pass negative number\nTo calculate factorial, number should be positive")
if(ans == -1):
    print(f"""Since you pass a negative number i.e {num}
To calculate factorial, please enter positive number""")
else:
    print(F"The factorial of {num} = {ans}")