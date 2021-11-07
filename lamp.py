        #siis..
#film_või_sari():
import matplotlib.pyplot as plot
import pandas as pd
import numpy as np
from tkinter import *
from PIL import ImageTk, Image
data = pd.read_csv('KertuViewingActivity.csv')
pealkirjad = data.head(0)
sisu = data["Title"]
print(sisu)
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
print(pealkirjad)
print(sarjad, filmid)   