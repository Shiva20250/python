def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


num = int(input("Enter the number to print series of prime numbers: "))

if num > 1:
    print(f"The series of prime numbers from 1 to {num}:")
    for i in range(2, num + 1):
        if is_prime(i):
            print(i, end=" ")
else:
    print("Number should be greater than 1 to print series of prime numbers.")
