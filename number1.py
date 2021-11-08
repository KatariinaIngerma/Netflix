import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import pandas as pd
import numpy as np
from tkinter import *
from PIL import ImageTk, Image
from icrawler.builtin import GoogleImageCrawler
import os
import time


raam = Tk()
sisend = Entry(raam, width=40, font="Graphique 15")
def kasutaja_sisend():
    data = pd.read_csv('KertuViewingActivity.csv')
    uus_sisend = str(sisend.get())
    #google_Crawler = GoogleImageCrawler(storage = {'root_dir': r'C:\Users\katar\OneDrive\Desktop\Netflix'})
    #google_Crawler.crawl(keyword = uus_sisend, max_num = 1)
    return uus_raam()


def uus_raam():
    #muuda_faili_nime()
    uusraam = Toplevel(raam) #toplevel uus aken
    uusraam.title(str(sisend.get()))
    uusraam.geometry("1000x600")
    #uus_pilt = PhotoImage(file="000001.png")  #mingi jama
    #uus = ImageTk.PhotoImage(uus_pilt)
    #uus_silt = Label(image=uus)
    #uus_silt.pack()
    jama = Label(uusraam, text = send())
    
    jama.pack()
    film_või_sari()
def send():
    data = pd.read_csv('KertuViewingActivity.csv')
    data['Duration'] = pd.to_timedelta(data['Duration'])
    andmed = data["Title"]
    kasutaja_sisend = str(sisend.get())
    for veerg in andmed:
        if kasutaja_sisend in veerg:
            aeg = data[data['Title'].str.contains(kasutaja_sisend, regex=False)]
            aeg = aeg[(aeg['Duration'] > '0 days 00:01:00')]
            kokku = ("Oled vaadanud seda: ", aeg['Duration'].sum())
            return str(kokku)


#proovi see lisada nupu juurde!!
#proovi muuta nii et ei oleks ainult Friendside kohta
def aeg():
    data = pd.read_csv('KertuViewingActivity.csv')
    data['Duration'] = pd.to_timedelta(data['Duration'])
    sõbrad = data[data['Title'].str.contains('Friends', regex=False)]
    sõbrad = sõbrad[(sõbrad['Duration'] > '0 days 00:01:00')]
    kokku=sõbrad['Duration'].sum()
    return kokku


def muuda_faili_nime():
    uus_nimi = r'C:\Users\katar\OneDrive\Desktop\Netflix\000001.png'
    vana_nimi = r'C:\Users\katar\OneDrive\Desktop\Netflix\000001.jpg'
    if os.path.isfile(uus_nimi):
        print("ok")
    else:
        if os.path.isfile(vana_nimi):
            im1 = Image.open(r'C:\Users\katar\OneDrive\Desktop\Netflix\000001.jpg')
            im1.save(r'C:\Users\katar\OneDrive\Desktop\Netflix\000001.png')

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
def üldine_aken():
    plot1=film_või_sari()
    canvas = FigureCanvasTkAgg(plot1, master = raam)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2TkAgg(canvas, self)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    #uusraam = Toplevel(raam)
    #uusraam.geometry("1000x600")
    #uusraam.title(text="Üldised andmed")
    
   
raam.call('wm', 'iconphoto', raam._w, PhotoImage(file='n.png'))
raam.title("Netflix andmeanalüüs")
raam.configure(bg="white")
raam.geometry("1000x600")
pilt = PhotoImage(file="pilt.png")
silt = Label(image=pilt)
silt.pack()

#Button(raam, text="Filmide ja sarjade jaotus",command= film_või_sari,
      # bg="red2", fg="white", font="Graphique 15").pack(pady=20) #pady paneb ridadele vahed ja pack paneb asja keskele
sisendi_silt = Label(raam, text="Kirjuta siia sarja või filmi nimi:", bg ="white", fg="black", font="Graphique 15")
sisendi_silt.pack(pady=20)
sisend = Entry(raam, width=40, font="Graphique 15")
sisend.pack()
nupp = Button(raam, text="Näita", command=kasutaja_sisend, bg="black", fg="red2", font="Graphique 15").pack()
Üldised_andmed= Button(raam, text="Kõik andmed", command=üldine_aken, bg="black",  fg="red2", font="Graphique 15").pack(pady=20)
raam.mainloop()
