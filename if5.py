m1=int(input("Enter the marks of subject 1: "))
m2=int(input("Enter the marks of subject 2: "))
m3=int(input("Enter the marks of subject 3: "))
m4=int(input("Enter the marks of subject 4: "))
m5=int(input("Enter the marks of subject 5: "))

sum=(m1+m2+m3+m4+m5)
avg=sum/5

print(f"Sum ={sum}, average = {avg}")

if avg>=90:
    print("A Grade")
elif avg>=70:
    print("B Grade")
elif avg>=50:
    print("C Grade")
elif avg>=35:
    print("D Grade")
else:
    print("FAIL")