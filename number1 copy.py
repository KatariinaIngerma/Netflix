import matplotlib.pyplot as plot
import pandas as pd
import numpy as np
from tkinter import *
from PIL import ImageTk, Image

def send():
    text.insert(END, "\n"+ send)
    #if sisend == "...midagi":
        #siis..
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
       command= film_või_sari, bg="red", fg="white").pack(pady=20) #pady paneb ridadele vahed ja pack paneb asja keskele

sisend = Entry(raam)
sisend.pack()
nupp = Button(raam, text="Saada", command=send, bg="red", fg="white").pack()

raam.mainloop()