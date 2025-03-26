#this file is a python program that converts the weight of a person from pounds to kilograms

weight = float(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit == 'L' or unit == 'l':
    converted = weight * 0.45
    print(f'You are {round(converted,2)} kilos')
elif unit == 'K' or unit == 'k':
    converted = weight / 0.45   
    print(f'You are {round(converted,2)} pounds')
else: 
    print(f'You entered {unit}, which is not a valid parameter. Please enter either L or K')

