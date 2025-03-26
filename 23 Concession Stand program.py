#This files if for practising Dictionaries

menu = {"popcorns" : 1.25 , "pizzas" : 222.25, "coke" : 12.25, "fries" : 12.25, "soda" : 25.2}

cart = []
total = 0

print("________________Menu_________________")
for key, value in menu.items():
    print(f"{key:10}:${value:.02f}")


while True:
    food = input("Select in items from the menu. Q to quit").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end ="")
    print()

print(f"The total is ${total:.2f}")