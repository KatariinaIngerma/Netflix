import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import pandas as pd
import numpy as np
from tkinter import *
from PIL import ImageTk, Image
from icrawler.builtin import GoogleImageCrawler
import os
import datetime
import calendar
import matplotlib.image as mpimg

raam = Tk()
sisend = Entry(raam, width=40, font="Graphique 15")
def kasutaja_sisend():
    kustuta_pilt()
    data = pd.read_csv('KertuViewingActivity.csv')
    uus_sisend = str(sisend.get())
    google_Crawler = GoogleImageCrawler(storage = {'root_dir': r'C:\Users\katar\OneDrive\Desktop\Netflix'})
#     google_Crawler = GoogleImageCrawler(storage = {'root_dir': r'C:\Users\Külmkapp\OneDrive\Desktop\Netflix'})
    google_Crawler.crawl(keyword = uus_sisend, max_num = 1)
    uus_nimi()
    uusraam = Toplevel(raam) #toplevel uus aken
    uusraam.title(str(sisend.get()))
    uusraam.geometry("1000x600")
    uusraam.configure(bg="white")
    nimi = Label(uusraam, text = sisend.get().upper(), bg="white",font=("Graphique", 17)).pack(pady=20)
    aeg = Label(uusraam, text = send(), font=("Graphique", 15),bg="white").pack()
#     image = Image.open('000001.png')
#     image = ImageTk.PhotoImage(image)
#     img = PhotoImage(file=image).pack()
#     img = ImageTk.PhotoImage(Image.open("000001.png"))
#     img = PhotoImage(file="000001.png")
# 
#     label = Label(uusraam, image=img)
#     label.pack()
# #     uusraam.mainloop()
#     pilt = PhotoImage(file="C:\Users\katar\OneDrive\Desktop\Netflix\000001.jpg")
#     silt = Label(image=pilt)
    img=mpimg.imread("000001.png")
    imgplot = plot.imshow(img)
    silt = Label(uusraam, image=imgplot).pack()

def uus_raam():
    uus_nimi()
    uusraam = Toplevel(raam) #toplevel uus aken
    uusraam.title(str(sisend.get()))
    uusraam.geometry("1000x600")
    uusraam.configure(bg="white")
    
#     uus = ImageTk.PhotoImage(uus_pilt)
#     uus_silt = Label(image=uus)
#     uus_silt.pack()
    nimi = Label(uusraam, text = sisend.get().upper(), bg="white",font=("Graphique", 17)).pack(pady=20)
    aeg = Label(uusraam, text = send(), font=("Graphique", 15),bg="white").pack()
#     pilt = PhotoImage(file = "000001.png") 
#     silt = Label(image=pilt).pack()
    image = Image.open('000001.jpg')
    image = image.resize((20, 20))
    image = ImageTk.PhotoImage(image)
    img = PhotoImage(file=image).pack()
    
def send():
    data = pd.read_csv('KertuViewingActivity.csv')
    data['Duration'] = pd.to_timedelta(data['Duration'])
    andmed = data["Title"]
    kasutaja_sisend = str(sisend.get())
    for veerg in andmed:
        if kasutaja_sisend in veerg:
            aeg = data[data['Title'].str.contains(kasutaja_sisend, regex=False)]
            aeg = aeg[(aeg['Duration'] > '0 days 00:01:00')]
#             aeg = aeg.replace("Days", "päeva")
            kokku = ("Oled vaadanud seda: " + str(aeg['Duration'].sum()))
            return kokku
#         else:
#             kokku1 = "Sa pole seda vaadanud :(" #sellega ei toota avga
#         return kokku1
#         
def päevad():
    data = pd.read_csv('KertuViewingActivity.csv')
    for veerg in data["Start Time"]:
        data["Start Time"] = pd.to_datetime[veerg]
        data = data.set_index('Start Time')
        data.index = data.index.tz_localize('UTC').tz_convert('Eastern/European')
        data = data.reset.index()
        print(data.head(1))
        
def subplot():
    E = 0
    T = 0
    K = 0
    N = 0
    R = 0
    L = 0
    P = 0
    data = pd.read_csv('KertuViewingActivity.csv')
    aeg = data["Start Time"]
    kasutaja_sisend = str(sisend.get())
    listike=[]
    for veerg in aeg:
        rida = veerg.split()
        uus1 = rida[0]
        uus2 = uus1.split("-")
        uus3 = uus2[::-1]
        string = " ".join(uus3)
        päev = datetime.datetime.strptime(string,'%d %m %Y').weekday()
        päeva_nimi = calendar.day_name[päev]
        if päeva_nimi == "Monday":
            E += 1
        elif päeva_nimi == "Tuesday":
            T += 1
        elif päeva_nimi == "Wednesday":
            K += 1
        elif päeva_nimi == "Thursday":
            N += 1
        elif päeva_nimi == "Friday":
            R += 1
        elif päeva_nimi == "Saturday":
            L += 1
        elif päeva_nimi == "Sunday":
            P += 1
    listike.extend([E,T,K,N,R,L,P])

    plot.subplot(1, 2, 1)
    plot.bar(["E","T", "K", "N", "R", "L", "P"], listike, color ="red")
    plot.title("Oled vaadanud Netflixi nende päevadel")
    data = pd.read_csv('KertuViewingActivity.csv')
    pealkirjad = data.head(0)
    sisu = data["Title"]
    sarjad = 0
    filmid = 0
    for veerg in sisu:
        if "Season" in veerg:
            sarjad += 1
        else:
            filmid += 1
    y = np.array([sarjad, filmid])
    tähistused = ["Sarjad", "Filmid"]
    värvid = ["red", "black"]
    plot.subplot(1, 2, 2)
    plot.pie(y, labels = tähistused, colors = värvid)
    plot.title("Filmide ja sarjade jaotus")
    plot.show()

def uus_nimi():
    try: 
        vana_nimi = "000001.jpg"
        base = os.path.splitext(vana_nimi)[0]
        os.rename(vana_nimi, base + ".png")
    except:
        try:
            vana_nimi = "000001.jpeg"
            base = os.path.splitext(vana_nimi)[0]
            os.rename(vana_nimi, base + ".png")
        except:
            print("okei")
        
def kustuta_pilt():
    if os.path.exists("000001.png"):
        os.remove("000001.png")

def film_või_sari(): 
    data = pd.read_csv('KertuViewingActivity.csv')
    pealkirjad = data.head(0)
    sisu = data["Title"]
    sarjad = 0
    filmid = 0
    for veerg in sisu:
        if "Season" in veerg:
            sarjad += 1
        else:
            filmid += 1
    y = np.array([sarjad, filmid])
    tähistused = ["Sarjad", "Filmid"]
    värvid = ["red", "black"]
    plot.title("Filmide ja sarjade jaotus")
    plot.pie(y, labels = tähistused, colors = värvid)
    

def kogu_aeg():
    data = pd.read_csv('KertuViewingActivity.csv')
    kokku=pd.to_timedelta(data['Duration']).sum()
    return kokku
   
def üldine_aken():
    subplot()
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