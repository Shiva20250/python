s1=int(input("Enter a side 1: "))
s2=int(input("Enter a side 2: "))
s3=int(input("Enter a side 3: "))

if s1 == s2 and s2 == s3:
    print("Equilateral triangle")


elif s1 == s2 or  s2 == s3 or s1 == s3:
    print("Isococles triangle")

else:
    print("Scalene triangle")