# Print a greeting message
print('hello')

# Get the user's name and print a personalized greeting
x = input("What is your name? ")
print("Hello", x)

# Print a number
print(123)

# Get the user's age and print it
y = input("What is your age? ")
print("You are", y, "years old")

# Get a number from the user and compare it with 10
x = int(input("Enter a number: "))
if x < 10:
    print('x is less than 10')
elif x == 10:
    print('x is equal to 10')
else:
    print('x is greater than 10')

# This is the if-else command

count = 0
while count < 3:
    print("This is a while loop")
    print("This is the second line of the loop")
    count += 1

#Integers
age = 21
players = 2
quantity = 5
print("you are ", age, " years old")
print(f"You are {age} years old")
print(f"There are {players} players")
print(f"There are {quantity} Bottles")

#Floats
GPA = 1.6
Distance = 3.5
Price = 10.99
print(f"Your GPA is {GPA}")
print(f"The distance is {Distance} miles")
print(f"The price is {Price} Euros")

#Strings
First_name = "Abhishek"
Email = "hi@abisk.de"

print(f"Your name is {First_name}")
print(f"Your email is {Email}")
print("We are now done with Integers Floats and Strings. That is Amazing")

#Boolean
online = True
For_sale = True
Running = False

print(f"Is the product online? {online}")
print(f"Is the product for sale? {For_sale}")
print(f"Is the product running? {Running}") 

if online:
    print("The product is online")
else:
    print("The product is offline")

# Tips with Vaariable
aa = 1
bb = 2
cc = 3

print(aa, bb, cc)

aa,bb,cc = 2,4,5
print(aa, bb, cc)
#