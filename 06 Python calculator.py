#This file is a simple calculator that can perform addition, subtraction, multiplication, and division.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(round((a + b),2))
elif operation == "-":
    print(round(a - b),2)
elif operation == "*":
    print(round(a * b),2)
elif operation == "/":
    print(round(a / b),2)
else:
    print("Invalid operation")

