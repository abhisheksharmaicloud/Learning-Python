# this file is for useful sting methods.
# I will also validtate the user input


name = input("Enter your Full name: ")
name1 = name.capitalize()
phone = (input("Enter your phone number: "))
find = input("Enter the character you want to find: ")
find1 = find.capitalize() 

# capitalize() method will capitalize the first letter of the string    
# upper() method will convert the string to uppercase
# lower() method will convert the string to lowercase
# isdigit() method will check if the string is digit or not
# isalpha() method will check if the string is alphabet or not
# count() method will count the number of occurance of a specific character in the string
# replace() method will replace the specific character with another character

# 1. len() method
print(f"Length of the name is: {len(name1)}")

# 2. Find method
# First occurance of a character
print(f"The first occurance of {find} is at index: {name.find(find1)}")
# last occurance of a character
print(f"The last occurance of the chactter {find} is at index: {name.rfind(find1)}")

# Replace method
print(f"The file needs to be saved as {name1.replace(' ', '_')}.txt")
print(f"the new phone number is: {phone.replace('-', '')}")


#Exercise to validate the user input. 
#Conditions: 1. Not more that 12 Characters, no spaces and no digits

aa = input("Enter your username: ")
bb = len(aa)

if  bb > 12:
    print("The usernamme is tooooo long")
elif not aa.find(" ") == -1:
    print("The username cannot have spaces")
elif not aa.isalpha():
    print("The username cannot have digits")
else:
    print(f"Welcome {aa}")
