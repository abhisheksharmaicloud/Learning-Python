#this file is for Exercise which will convert the temperature

t = int(input("What temperature would you like to convert: "))
u = input("what is the unit of the temperature you entered? (C)elsius or (F)ahrenheit: (K)elvin")
u1 = input("What unit would you like to fonvert it to: ? (C)elsius or (F)ahrenheit:(K)elvin")

if u == 'C' and u1 == 'F':
    converted = t * 9/5 + 32
    print(f'You are {round(converted,2)} Fahrenheit')
elif u == 'F' and u1 == 'C':
    converted = (t - 32) * 5/9
    print(f'You are {round(converted,2)} Celsius')
elif u == 'C' and u1 == 'K':
    converted = t + 273.15
    print(f'You are {round(converted,2)} Kelvin')
elif u == 'K' and u1 == 'C':
    converted = t - 273.15
    print(f'You are {round(converted,2)} Celsius')
elif u == 'F' and u1 == 'K':
    converted = (t - 32) * 5/9 + 273.15
    print(f'You are {round(converted,2)} Kelvin')
elif u == 'K' and u1 == 'F':
    converted = (t - 273.15) * 9/5 + 32
    print(f'You are {round(converted,2)} Fahrenheit')
else:
    print(f'You entered {u} and {u1}, which is not a valid parameter. Please enter either C, F or K')
