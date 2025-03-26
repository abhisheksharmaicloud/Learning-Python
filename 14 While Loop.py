# In this file i will learn and practise while loop in python
# While loop is used to iterate over a block of code as long as the test expression is true


#Example 1
name = input(" Enter your name please: ")

while name == "":
    print(" ENter a name you dumfuck")
    name = input(" Enter your name please: ")
print(f"Welcome {name}")


#Example 2

age = int(input("What is you age: ?"))

while age <0:
    print ("What are you? a demon?")
    age = int(input("What is you age: ?"))
print(f"You are {age} years old")

#Example 3
food = input("What is your favourite food: ?")

while not food == "pizza":
    print("you like shitty food")
    food = input("What is your another favourite food: ?")
print(f"now its like you like good food")

#example 4
num = int(input("enter a number between 1 and 10: "))

while num <1 or num>10:
    print("You are a dumbfuck")
    num = int(input("enter a number between 1 and 10: "))
print(f"you entered {num}")