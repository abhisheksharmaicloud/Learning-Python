# This File is for Practising the Loop commands in Python
# Soo Lets get started.


#if loop

age = int(input("Enter your age: "))

#is an abult or not?
if age <= 0:
    print("You are not born yet")
elif age < 18:
    print("You are a minor")
elif age == 18:
    print("You are 18 years old")
else:
    print("You are an adult")

#is the age limit
if age>=18:
      print("You can signup")
else:
    print("You are not allowed to signup")  

#Exercise
#Check if the user is allowed to drive

Driving_age = int(input("Enter the your age: "))
Country = input("Enter the country you are from: ") 
limit = int(input("Enter the driving age limit in your country: "))

if Driving_age >= limit:
    print(f"You are allowed to drive in {Country}")
else:
    print(f"You are not allowed to drive {Country}")

#Exercise 2

hungry = input("Are you hungry? (yes/no) ")

if hungry == "yes":
    print("i will order something for you now")
elif hungry == "":
    print("The fuck man! Are you hungry or not?")
else:
    print("I will order something for you later then!")

