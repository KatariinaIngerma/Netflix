import matplotlib.pyplot as plot
import pandas as pd
import numpy as np
from tkinter import *
from PIL import ImageTk, Image

def kasutaja_sisend():
    data = pd.read_csv('KertuViewingActivity.csv')
    uus_sisend = str(sisend.get())
    #for veerg in data["Title"]:
       # if uus_sisend in veerg:
           # data["Duration"]
        
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
raam.call('wm', 'iconphoto', raam._w, PhotoImage(file='n.png'))
raam.title("Netflix andmeanalüüs")
raam.configure(bg="white")
raam.geometry("1000x600")
pilt = PhotoImage(file="pilt.png")
silt = Label(image=pilt)
silt.pack()
Button(raam, text="Filmide ja sarjade jaotus",
       command= film_või_sari, bg="red", fg="white", font="Graphique 15").pack(pady=20) #pady paneb ridadele vahed ja pack paneb asja keskele
sisendi_silt = Label(raam, text="Kirjuta siia sarja või filmi nimi:", font="Graphique 15" )
sisendi_silt.pack()
sisend = Entry(raam, width=40, font="Graphique 15")

sisend.pack()
nupp = Button(raam, text="Saada", command=kasutaja_sisend, bg="red", fg="white", font="Graphique 15").pack()

raam.mainloop()
