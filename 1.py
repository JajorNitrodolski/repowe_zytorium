import numpy as np
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

flags=pd.read_csv("flags.csv", sep=";")
zflags=flags[(flags.Zone=="NW")|(flags.Zone=="NE")]
wykres=zflags.groupby("Landmass").agg({"Area":["sum"]})
wykres.plot(kind="pie", subplots=True, xlabel="Continent", ylabel="Total area", title="Area of the continents (the top half)", fontsize=14, autopct="%.2f%%", legend=True)
plt.show()

zgroup=flags.groupby("Zone")
