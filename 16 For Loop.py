#This file is for learning and practising for loop
#For loop is used to iterate over a sequence (list, tuple, string) or other iterable objects    


for x in range(1,11):
    print(x)

for x in reversed(range(1,11)):
    print(x)

for x in range(1,11,2):
    print(x)


card = "1234-5678-1234-5678"

for x in card:
    print(x)

for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)

for x in range(1,21):
    if x == 13:
        break
    else:
        print(x)