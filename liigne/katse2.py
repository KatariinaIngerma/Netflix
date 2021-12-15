import matplotlib.pyplot as plot
import pandas as pd
import numpy as np
import time
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

data = pd.read_csv('KertuViewingActivity.csv')
data['Duration'] = pd.to_timedelta(data['Duration'])
# Kertuinfo = data[data['Profile Name'].str.contains('Kertu', regex=False)]
# #print(Kertuinfo)

# kui siin muta "Friends" mingi muu seriaali märksõnaga, siis ütleb selle kohta aja
#kuidas sõltumatult teha?
sõbrad = data[data['Title'].str.contains('Friends', regex=False)]
sõbrad = sõbrad[(sõbrad['Duration'] > '0 days 00:01:00')]
kokku=sõbrad['Duration'].sum()
print(kokku)

#searchbar äkki toimima??
def Otsing(sisu):
    väärtus=sisu.widget.get()
    print (väärtus)
    
    if väärtus == "":
        data=list
    else:
        data=[]
        for element in list:
            if väärtus.lower() in element.lower():
                data.append(element)
    Uuenda(data)

def Uuenda(data):
    listbox.delete(0,"end")
    for element in data:
        listbox.insert("end", element)

list = ("Friends", "Modern Family", "The Big Bang Theory", "Squid Game",
        "Money Heist", "Mission", "Formula 1" )