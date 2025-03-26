#name = input("Enter your name: ")
#km = float(input("Please enter the Distance in KMs: "))
#miles = 1.609 * km

#print(f"Greetings {name.capitalize()} The distance you have enter is {km}Kms and when converted to Miles its is: {miles}")

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]

newsales = float(input("Enter the number you would like to add to week 2: "))
sales_w2.append(newsales)

Total_sales = sum(sales_w1+sales_w2)
print(f"The total sals for the two weeks is: {Total_sales}")

# Create a combined list (no extra brackets)
sales = sales_w1 + sales_w2

# Sort the combined list
sales.sort()

# Get the minimum and maximum values
worst_day = sales[0]
best_day = sales[-1]

print(f"The best day is: {best_day*1.5} and the worst day is: {worst_day*1.5}")