setA = {5,10,1,2,3,6,20}
setB = {2,30,6,20,10,-8}

print(F"Set A = {setA}")
setA.update([60,-55])
print(F"Set A = {setA}")
print(F"Set B = {setB}")


union = setA.union(setB)
print(F"Set A Union Set B = {union}")


print(F"Set A Intersection Set B = {setA.intersection(setB)}")


print(F"Set A Difference Set B = {setA.difference(setB)}")
print(F"Set B Difference Set A = {setB.difference(setA)}")


print(F"Set A Symmetric Difference Set B = {setA.symmetric_difference(setB)}")