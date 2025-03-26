# This file  is for One line shortcuts for the if else statement
# this is also know as ternary operator
# This is a one line code for the if else statement
# The fromat is:  "True" if CONDITION else "False"

num = int(input("Enter a number: "))
print("Positive" if num > 0 else "Negative") # Positive

#This one for checking if the number is even or odd
aa = ( int(input("Enter a Number: ")))
print("Even" if aa % 2 ==0 else "Odd") 

# This one is to check out of  two numbber which is greater?

bb = float(input("Enter a number: "))
cc = float(input("Enter a number: "))
print(bb if bb > cc else cc) 

# This one is to check out of  two numbber which is smallest?

bb = float(input("Enter a number: "))
cc = float(input("Enter a number: "))
print(bb if bb < cc else cc) 