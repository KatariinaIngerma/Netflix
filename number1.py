import matplotlib.pyplot as plot
import pandas as pd
import numpy as np
import time
from tkinter import *

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
raam = Tk()
raam.geometry("1000x1000")
Button(raam, text="Filmide ja sarjade jaotus", command= film_või_sari).pack(pady=20)
raam.mainloop()
