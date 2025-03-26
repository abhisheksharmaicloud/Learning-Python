#This is for practicing the User Inputs in Python

# here is am practising how to take user inputs as strings and flat and print in Python
adjective1 = input("Enter an Adjective: ")
adjective2 = input("Enter another Adjective: ")
age = int(input("Enter your age: "))    

print(f"I am {adjective1}")
print(f"and my name is {adjective2}")
print(f"I am {age} years old")

#here i will trying claculate the area
length = float(input("Enter the length of the rectangle: "))    
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

area = length * width * height

print(f"The volume of the rectangle is {area}cm^3")

item = input("Enter the name of the item: ")
price = float(input("Enter the price of the item: "))
Quqantity = int(input("Enter the quantity of the item: "))
total = price * Quqantity

print(f"The total price of {Quqantity} {item} is {round(total,2)} Euros")

#This is the end of the User Inputs file