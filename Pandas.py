import pandas as pd
df = pd.read_csv('pokemon_data.csv')
#print(df.tail(5)) .tail is for printing last rows and .head is for fetching first rows
df_xl = pd.read_excel('pokemon_data.xlsx')
print(df_xl.tail(7))
#so read along with the file name helps you define the file format you want the python program to be read
df_txt = pd.read_csv('pokemon_data.txt', delimiter='/t') #So the delimiter is to define the sseprator that is used in the file and in the text file tab is used hence '/t'
print(df_txt.tail(2))