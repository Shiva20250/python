def prime():
 n=int(input("Enter a Number:"))

 is_prime=None

 if(n<=1):
  is_prime=False
  print("Enter a number greater than 1")
  return
 
 count=0
 factors=[]
 for i in range(1,n+1):
  
  if(n%i==0):
   count=count+1
   factors.append(i)

 if count==2:
  print(f"Number {n} is prime")
  print(f"Its only factors are {factors[0]} and {factors[1]}")

 else:
  print(f"Number {n} is not prime number")
  print(f"All factors are {factors}")
  

prime()


 
 








 
 




