# This is for learning and practvise file for indexing 

Credit_Card = "1234-5678-9101"

print(Credit_Card[0]) # First character
print(Credit_Card[0:5]) # From 0 to 5th character
print(Credit_Card[:5]) # From the start to 5th character
print(Credit_Card[5:]) # From 5th character to the end
print(Credit_Card[-1:]) # Last character
print(Credit_Card[::2]) # Last character to 4th character in reverse order in increment of 2


#practice
#fetch the last four digits of the credit card

cc = input("Enter your credit card number: ")
print(cc[-5:-1])

# Email Slicing
email = input("Enter your email: ")
index = email.index("@")

username = email[ : index]
domain = email[index + 1 : ]

print(f"Your username is {username} and domain is {domain}")
print(f"You encrypted email is {username[:2]}****{email[index:]}")