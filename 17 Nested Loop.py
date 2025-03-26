# This file is forr learning and practising nested loop
# Nested loop is a loop inside a loop


for x in range(3):
    for y in range(1,10):
         print(y,end=",")
    print("\n")

#printing a rectangle

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol,end="")
    print("\n")

#making a count down timer
import time

my_time = int(input("Enter the time in seconds: "))

for x  in reversed(range(0,my_time)):
    s = x%60
    m = int(x/60)%60
    h = int(x/3600)
    print(f"{h:02d}:{m:02d}:{s:02d}")
    time.sleep(1)
print("Time's up!")
