n=int(input("Enter a number: "))

last_digit=n%10

if(last_digit%3 == 0):
    print("It is divible by 3")

else:
    print("Not divible by 3")