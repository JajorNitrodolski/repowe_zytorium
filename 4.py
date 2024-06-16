import numpy as np
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

całe = pd.Series(np.linspace(5,30,6), index=[5,10,15,"d","e","f"])
print(całe[15])
print(całe["e"])

kraje = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
        'Populacja': [11190846, 1303171035, 207847528, 38675467]}

ramka=pd.DataFrame(kraje)
print(ramka,end="\n")
print(ramka["Stolica"],end="\n")
print(ramka.iloc[2,1],end="\n")
print(ramka.loc[2,"Stolica"],end="\n")
print(ramka.at[2,"Stolica"],end="\n")
print(ramka.sample(7,replace=True))
print(ramka.head(2))
print(ramka.tail(2))
print(ramka.T)

print(całe[(całe>=10)&(całe<30)])
print(ramka[(ramka['Populacja']>15000000)&(ramka['Kontynent']=="Europa")])
print(ramka[(ramka['Populacja']>15000000)].agg({"Populacja":["min"]}))

print(ramka[(ramka.Populacja > 1000000)&(ramka.index.isin([0,2]))])

#szukaj = ['Belgia', 'Brasilia']
#print(ramka.isin(szukaj))

#ramka.loc[3]='dodane'
ramka.loc[4]=["Izrael","Jeruzalem","Azja",5000000]
#ramka.drop([3],inplace=True)

ramka["Ustrój"]=["mon","prez","prez","prez","prez"]
print(ramka.sort_values(by="Kraj",ascending=False))

#grupt=ramka.groupby("Kontynent")
#print(grupt.get_group("Azja"))
#grupa=ramka.groupby(['Kontynent']).agg({'Populacja':['sum']})
grupa=ramka.groupby(['Ustrój']).agg({'Kraj':['count']})
print(grupa)

grupa.plot(kind='bar', xlabel='Kontynent', ylabel='Mld', rot=0, legend=True, title='Populacja z podziałem na kontynenty')
#plt.show()
#daty = pd.date_range('20030426', periods=10)
#print(daty)

dzieci=pd.read_excel("imiona.xlsx")
#print(dzieci[dzieci.Liczba>1000])
#print(dzieci[dzieci.Imie=='MIKOŁAJ'])
#print(dzieci.Liczba.sum())
gdzieci=dzieci[(dzieci.Rok<2006)&(dzieci.Rok>1999)]
print(gdzieci.Liczba.sum())
print(dzieci.groupby('Plec').agg({'Liczba':['sum']}))
print(dzieci.sort_values(by="Liczba").groupby('Plec').last())
