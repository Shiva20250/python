num=int(input("Enter a number: "))
last_digit=num % 10
# 158 -> 8


if last_digit % 3==0:
    print(f"Number= {num},Last_digit={last_digit} is divisible by 3")

else:
    print(f"Number= {num},Last_digit={last_digit} is not divisble by 3")