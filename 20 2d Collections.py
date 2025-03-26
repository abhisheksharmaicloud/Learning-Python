# This if file is for learning and practising 2d Collections

fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "potato", "onion"]
meats = ["beef", "chicken", "fish"]

groceries = [fruits, vegetables, meats]

print(groceries)

#now lets change the files
fruits[0] = "blueberry"

print(groceries[2][2])

# order way to make 2d lists
groceries = [["apple", "banana", "cherry"], ["carrot", "potato", "onion"], ["beef", "chicken", "fish"]]

for collection in groceries:
    for item in collection:
        print(item, end=",")

# exersice

num_pad =((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()