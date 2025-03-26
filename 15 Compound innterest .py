#this file is to learn and practise how to calculate compound interest in python

p = 0
r = 0
t = 0

while p <= 0:
    p = float(input("Enter the principal amount: "))    #taking input from user for principal amount
    if p <= 0:
        print("Please enter a number above 0")    #if user enters a negative number, this message will be displayed
print(f"The principal amount is: {p}")

while r <= 0:
    r = float(input("Enter the interest rate: "))    #taking input from user for principal amount
    if r <= 0:
        print("Please enter a number above 0")    #if user enters a negative number, this message will be displayed
print(f"The interest rate is: {r}")

while t <= 0:
    t = float(input("Enter the time in years: "))    #taking input from user for principal amount
    if t <= 0:
        print("Please enter a number above 0")    #if user enters a negative number, this message will be displayed
print(f"The time in years is: {t}")

a = p * (1 + r/100) ** (t)    #formula to calculate compound interest
print(a)    #printing the compound 


#Another way of writing the code

p = 0
r = 0
t = 0

while True:
    p = float(input("Enter the principal amount: "))    #taking input from user for principal amount
    if p < 0:
        print("Please enter a number above 0")    #if user enters a negative number, this message will be displayed
    else:
        break

while True:
    r = float(input("Enter the interest rate: "))    #taking input from user for principal amount
    if r < 0:
        print("Please enter a number above 0")    #if user enters a negative number, this message will be displayed
    else:
        break

while True:
    t = float(input("Enter the time in years: "))    #taking input from user for principal amount
    if t < 0:
        print("Please enter a number above 0")    #if user enters a negative number, this message will be displayed
    else:
        break

a = p * (1 + r/100) ** (t)    #formula to calculate compound interest
print(a)    #printing the compound 