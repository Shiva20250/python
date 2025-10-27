# WAP TO CREATE EMPTY LIST
# ADD STUDENT NAME MARKS IN LIST IN NESTED FOR ->  STUDNET
'''[
    ["nAME", MARKS],
]
'''
# FOR LOOP AND DISPLAY EACH STUDENT

students =[]

print(students)

students.append(["Mihir Jadhav",85.55])
students.append(["Rohit Sharma",92.55])
students.append(["Pranjal Gupta",48.55])
print(students)

# store 10 fruits in list
# find index of apple in list
# remove orange, watermellon

Fruit=["Apple","Orange","Guava","Watermelon","Stawberry","Litchi","Mango","Apple","Grapes"]

Fruit.remove("Orange")
Fruit.remove("Watermelon")
print("Index of=",Fruit.index("Apple"))
print(Fruit)
print("Index of=",Fruit.index("Apple",Fruit.index("Apple")+1))
