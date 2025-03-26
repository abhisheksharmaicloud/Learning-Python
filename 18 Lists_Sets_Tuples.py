# This file is for learning and practising lists, sets and tuples
# Lists are ordered, changeable, and allow duplicate values
# Sets are unordered, unindexed, and do not allow duplicate values
# Tuples are ordered, unchangeable, and allow duplicate values


#collections
fruits = ["apple","banana","cherry","date","elderberry","fig","grape","honeydew","kiwi","lemon","mango","nectarine","orange","papaya","quince","raspberry","strawberry","tangerine","ugli","vanilla","watermelon"]
print(fruits)
print(fruits[0])

for fruit in fruits:
    print(fruit,end=",")
print("\n")
print(len(fruits))

#reassign the value using index
fruits[10] = "mango"
print(fruits[10])


fruits.remove("mango") #remove
fruits.insert(10,"mango") #insert
fruits.sort() #sort
fruits.reverse() #reverse
print(fruits)
print(fruits.index("mango")) #index
print(fruits.count("mango")) #count
fruits.clear() #clear

#help
#print(help(fruits))

#Sets
#the values are unordered and unindexed no duplicate values
fruits = {"apple","banana","cherry","date","elderberry","fig","grape","honeydew","kiwi","lemon","mango","nectarine","orange","papaya","quince","raspberry","strawberry","tangerine","ugli","vanilla","watermelon"}
print(fruits)

for fruit in fruits:
    print(fruit,end=",")
print("\n")
print(len(fruits))

print("mango" in fruits) #check if the value is in the set


fruits.remove("mango") #remove
fruits.add("mango") #insert
print(fruits)
fruits.clear() #clear


#tuples
#ordered, unchangeable, allow duplicate values and are faster

fruits = ("apple","banana","cherry","date","elderberry","fig","grape","honeydew","kiwi","lemon","mango","nectarine","orange","papaya","quince","raspberry","strawberry","tangerine","ugli","vanilla","watermelon")
print(fruits)

print(fruits.index("mango")) #index
print(fruits.count("mango")) #count
for fruit in fruits:
    print(fruit,end=",")
print("\n")
print(len(fruits))