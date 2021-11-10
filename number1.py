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
    kustuta_pilt()
    data = pd.read_csv('KertuViewingActivity.csv')
    uus_sisend = str(sisend.get())
    google_Crawler = GoogleImageCrawler(storage = {'root_dir': r'C:\Users\katar\OneDrive\Desktop\Netflix'})
    #google_Crawler = GoogleImageCrawler(storage = {'root_dir': r'C:\Users\Külmkapp\OneDrive\Desktop\Netflix'})
    google_Crawler.crawl(keyword = uus_sisend, max_num = 1)
    return uus_raam()

def uus_raam():
    uus_nimi()
    uusraam = Toplevel(raam) #toplevel uus aken
    uusraam.title(str(sisend.get()))
    uusraam.geometry("1000x600")
    #uus_pilt = PhotoImage(file = "000001.png")  #mingi jama pilt ei tule kuidagi :dddd
#     img = Image.open('000001.png')
#     photo = ImageTk.PhotoImage(img)
#     silt = Label(image=photo)
#     silt.pack()
    
#     uus = ImageTk.PhotoImage(uus_pilt)
#     uus_silt = Label(image=uus)
#     uus_silt.pack()
    jama = Label(uusraam, text = send())
    jama.pack()
    
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
            return kokku
        if kasutaja_sisend not in veerg:
            kokku = "Sa pole seda vaadanud :("
            return kokku
        

def aeg():
    data = pd.read_csv('KertuViewingActivity.csv')
    data['Duration'] = pd.to_timedelta(data['Duration'])
    aeg = data[data['Title'].str.contains(sisend, regex=False)]
    aeg = aeg[(aeg['Duration'] > '0 days 00:01:00')]
    kokku=aeg['Duration'].sum()
    return kokku

def uus_nimi():
    try: 
        vana_nimi = "000001.jpg"
        base = os.path.splitext(vana_nimi)[0]
        os.rename(vana_nimi, base + ".png")
    except:
        vana_nimi = "000001.jpeg"
        base = os.path.splitext(vana_nimi)[0]
        os.rename(vana_nimi, base + ".png")
        
def kustuta_pilt():
    if os.path.exists("000001.png"):
        os.remove("000001.png")

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
    
def kogu_aeg():
    data = pd.read_csv('KertuViewingActivity.csv')
    kokku=pd.to_timedelta(data['Duration']).sum()
    print(kokku)
    return kokku
kogu_aeg()    
    
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

# Button(raam, text="Filmide ja sarjade jaotus",command= film_või_sari,
#        bg="red2", fg="white", font="Graphique 15").pack(pady=20) #pady paneb ridadele vahed ja pack paneb asja keskele
sisendi_silt = Label(raam, text="Kirjuta siia sarja või filmi nimi:", bg ="white", fg="red", font="Graphique 15")
sisendi_silt.pack(pady=20)
sisend = Entry(raam, width=40, font="Graphique 15")
sisend.pack()
nupp = Button(raam, text="Näita", command=kasutaja_sisend, bg="white", fg="red2", font="Graphique 15").pack()
Üldised_andmed= Button(raam, text="Kõik andmed", command=üldine_aken, bg="white",  fg="red2", font="Graphique 15").pack(pady=20)
raam.mainloop()
