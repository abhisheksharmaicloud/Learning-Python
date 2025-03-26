# This file is for practicisng logical operators
# So lets get started
# Logical operators include and, or, not
# And: This operator is used to check if all the conditions are true
# Or: This operator is used to check if at least one of the conditions is true
# Not: This operator is used to check if the condition is false

temp = int(input("What is the temperature today: "))
mood = input("How do you feel about the weather today: ")
Cloud = input("is it cloudy outside: ")
Online = True

if temp <= 0 or temp >= 45:
    print("you are screwed")
elif temp > 0 and temp < 20:
    print("It's a bit cold today")
elif temp > 20 or temp < 30:
    print("Looks like a Beutiful weather")
else:
        print("It's a bit hot today")

if mood == 'happy' or mood == 'excited':
    print("I'm happy for you")
elif mood == 'sad' or mood == 'depressed':
    print("I'm sorry to hear that")
else:
    print("I'm not sure how to respond to that")

if Cloud == 'yes' or Cloud == 'Yes':
    print("It's going to rain today")
elif Cloud == 'no' or Cloud == 'No':
    print("It's not going to rain today")
else:
    print("I'm not sure what you mean by that")

if not Online:
    print("You are offile") 
else:
    print("You are Online")