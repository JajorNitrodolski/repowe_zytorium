import numpy as np
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

flags=pd.read_csv("flags.csv", sep=";")
gflags=flags[(flags.Landmass=="Asia")|(flags.Landmass=="Africa")]
wflags=gflags.groupby("Landmass").agg({"Country":["count"]})

wflags.plot(kind='bar', xlabel='Kontynent', ylabel='Liczba krajów', title="Wykres")
plt.show()

relflags=flags.groupby("Religion").agg({"Religion":["count"]})
relflags.plot(kind='pie', subplots=True, autopct='%.2f%%', fontsize=14, figsize=(6,6), colors=['red','green'], title="Religia na świecie")
plt.show()