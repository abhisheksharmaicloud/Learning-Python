#This file is for practicing the math and arthematics commands in Python

friends = 0
New_friends = friends+1

# augmented assignment
friends += 1 # friends = friends + 1 #Addition
print(friends)
friends -= 1 # friends = friends - 1 #Subtraction
print(friends)
friends *= 1 # friends = friends * 1 #Multiplication
print(friends)
friends /= 1 # friends = friends / 1 #Division
print(friends)
friends %= 1 # friends = friends % 1 #Modulus
print(friends)
friends **= 1 # friends = friends ** 1 #Exponentiation
print(friends)

#Math Functions

x = 3.14
y = -10
z = 2.9

mul = x * y
ads = abs(x * y)
maxi = max(x, y, z)
mini = min(x, y, z)
power = pow(x, 2)
rounding = round(x)

print(f"the values that are calculated are as follows: {mul}, {ads}, {maxi}, {mini}, {power}, {rounding}")

#now using math module

import math

print(round(math.pi,2)) #rounding the value of pi to 2 decimal places
print(round(math.e,2)) #rounding the value of e to 2 decimal places

x = float(input("Enter a number: "))
z = math.sqrt(x) #square root
y = math.ceil(z) #rounding up
print(f"The square root of {x} is {round(y,2)}")


#Exercise:
# Circumaference of a circle

radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference of the circle is {round(circumference,2)}")

#exercise:
# Area of a circle

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2 #another way to write this is area = math.pi * pow(radius,2)
print(f"The area of the circle is {round(area,2)}")

#exercise:
#hypotenuse of a Triangle

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c= math.sqrt(pow(a,2) + pow(b,2))   

print(f"The length of the hypotenuse is {round(c,2)}")

#This is the end of the Math file