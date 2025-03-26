# This file is for learning and practising lists, sets and tuples as exersices

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food item: (press q to quit) ")
    if food.lower() == "q":
        break
    else: 
        price = float(input(f"Enter the price of {food}: "))
        foods.append(food)
        prices.append(price)
   
print("------- Your Cart -------")
for food in foods:
    print(f"{food} will cost $ {price}")  

for price in prices:
    total += price

print(f"You total will be ${total}")