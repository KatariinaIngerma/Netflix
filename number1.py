import matplotlib.pyplot as plot
import pandas as pd
import numpy as np
#import time
#from tkinter import *

#raam = Tk()
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
print(sisu)
print(pealkirjad)