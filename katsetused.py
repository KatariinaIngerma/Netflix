import matplotlib.pyplot as plot
import pandas as pd
import numpy as np
import time
from tkinter import *
from PIL import ImageTk, Image

#proovi see lisada nupu juurde!!
#proovi muuta nii et ei oleks ainult Friendside kohta
def aeg():
    data = pd.read_csv('KertuViewingActivity.csv')
    data['Duration'] = pd.to_timedelta(data['Duration'])
    sõbrad = data[data['Title'].str.contains('Friends', regex=False)]
    sõbrad = sõbrad[(sõbrad['Duration'] > '0 days 00:01:00')]
    kokku=sõbrad['Duration'].sum()
    return kokku

def send():
    data = pd.read_csv('KertuViewingActivity.csv')
    data['Duration'] = pd.to_timedelta(data['Duration'])
    sisend = input(str("Mis seriaal?"))
    if sisend.lower() == "friends".lower():
        sõbrad = data[data['Title'].str.contains('Friends', regex=False)]
        sõbrad = sõbrad[(sõbrad['Duration'] > '0 days 00:01:00')]
        kokku = print("Oled vaadanud seda: ", sõbrad['Duration'].sum())
        return kokku
    if sisend.lower() == "modern family".lower():
        modernf = data[data['Title'].str.contains('Modern', regex=False)]
        modernf = modernf[(modernf['Duration'] > '0 days 00:01:00')]
        kokku = print("Oled vaadanud seda: ", modernf['Duration'].sum())
        return kokku
    if sisend.lower() == "The Big Bang Theory".lower():
        TheBigBang = data[data['Title'].str.contains('The Big Bang Theory', regex=False)]
        TheBigBang = TheBigBang[(TheBigBang['Duration'] > '0 days 00:01:00')]
        kokku = print("Oled vaadanud seda: ", TheBigBang['Duration'].sum())
        return kokku
    
    
def film_või_sari(): 
    data = pd.read_csv('KertuViewingActivity.csv')
    pealkirjad = data.head(0)
    sisu = data["Title"]
    sarjad = 0
    filmid = 0
    for veerg in data["Title"]:
        if "Season" in veerg:
            sarjad += 1
        else:
            filmid += 1
    y = np.array([sarjad, filmid])
    tähistused = ["Sarjad", "Filmid"]
    värvid = ["Black", "red"]
    plot.pie(y, labels = tähistused, colors = värvid)
    plot.show()


    
#if row (0) is not kertu delete row
#def vaatamise_aeg():
    
raam = Tk()
raam.configure(bg="white")
raam.geometry("1000x800")
pilt = PhotoImage(file="pilt.png")
silt = Label(image=pilt)
silt.pack()

Button(raam, text="Filmide ja sarjade jaotus",
       command= film_või_sari, bg="red", fg="black").pack(pady=20)
#pady paneb ridadele vahed ja pack paneb asja keskele

sisend = Entry(raam)
sisend.pack()
nupp = Button(raam, text="Saada", command=send, bg="red", fg="black").pack()

raam.mainloop()
