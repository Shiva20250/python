#  wap TO ACCEPT A NUMBER AND PRINT SERIES OF PRIME NUMBER TILL THAT NUMBER USIGN FUNCTION
def is_prime(number):
    i=2
    while(i<=number //2):
        if(number % i ==0):
            return False
        
        i+=1
        return True
    
    num=int(input("Enter the number to print series of prime number:"))

    if (num>1):
        print(f"The series of prime 1 to {num}")

    else:
        print("Number should be greater than 1 to print series of prime number")


    if(is_prime(i)):
        print(f"{i} ",end="")

    
    is_prime(True)

    

    
    
    