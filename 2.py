import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#plik = pd.ExcelFile('imiona.xlsx')
#df = pd.read_excel(plik, header=0)

# print(df[df.Liczba > 1000])
# print('')
# print(df[df.Imie == 'RADOSŁAW'])
# print('')
# print(df.Liczba.sum())
# print('')
# grupa = df[df.Rok < 2006]
# print(grupa.Liczba.sum())
# grupa = df[df.Rok < 2006].groupby('Rok').agg({'Liczba': ['sum']})
# print(grupa)
# print('')
#
# print(df.groupby('Plec').agg({'Liczba':['sum']}))

# print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).first())
#
# new_df = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
#
# for index, group in enumerate(new_df, start=1):
#     print(f"{index} {group[0]}")
#     print(f" {group[1].iloc[0]['Imie']}", end='')
#     print(f" {group[1].iloc[0]['Liczba']}")
# grupa = df.groupby(['Rok', 'Plec']).agg('Liczba').max()
# print(grupa)
#
# for i,g in enumerate(grupa, start=1):
#     print(i)
#     print(df[df['Liczba'] == g])
# grupa = df.groupby(['Rok', 'Plec']).agg({'Liczba':['max']})
# print(grupa[max])
# for i, g in enumerate(grupa[max], start=1):
#     print(df[df['Liczba'] == g])
# print('')
# print("Chłopiec")
# print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])
# print("Dziewczynka")
# print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])