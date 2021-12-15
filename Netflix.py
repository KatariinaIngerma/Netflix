import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import pandas as pd
import numpy as np
from tkinter import *
from PIL import ImageTk, Image
from icrawler.builtin import GoogleImageCrawler
import os
from os.path import exists
import datetime
import calendar
import matplotlib.image as mpimg
import csv

raam = Tk()
raam.geometry('300x250')
sisend = Entry(raam, width=40, font="Graphique 15")

def kasutaja_sisend():
    kustuta_pilt()
    data = pd.read_csv('KertuViewingActivity.csv')
    uus_sisend = str(sisend.get())
    google_Crawler = GoogleImageCrawler(storage = {'root_dir':r'/Users/kertujogi/Desktop/progeprojekt'})
    google_Crawler.crawl(keyword = uus_sisend, max_num = 1)
#     google_Crawler = GoogleImageCrawler(storage = {'root_dir': r'C:\Users\Külmkapp\OneDrive\Desktop\Netflix'})
    return uus_raam()

def uus_raam():
    uus_nimi()
    uusraam = Toplevel(raam)
    uusraam.title(str(sisend.get()))
    uusraam.geometry("800x600")
    uusraam.configure(bg="white")
    nimi = Label(uusraam, text = sisend.get().upper(), bg="white",font=("Graphique", 17)).pack(pady=20)
    aeg = Label(uusraam, text = send(), font=("Graphique", 15),bg="white").pack()
    graafik_1 = Button(uusraam, text="Nädalapäevad", command = graafik1, font=("Graphique", 15),bg="white", fg="red2").pack(pady=30)
    graafik_2 = Button(uusraam, text="Aastajad", command = graafik2, font=("Graphique", 15),bg="white", fg="red2").pack(pady=30)
    graafik_3 = Button(uusraam, text="Aastad",command = graafik3, font=("Graphique", 15),bg="white", fg="red2").pack(pady=30)
    graafik_4 = Button(uusraam, text="Kellaajad", command=graafik4, font=("Graphique", 15),bg="white", fg="red2").pack(pady=30)
    
def send():
    data = pd.read_csv('KertuViewingActivity.csv')
    data['Duration'] = pd.to_timedelta(data['Duration'])
    andmed = data["Title"]
    kasutaja_sisend = str(sisend.get())
    for veerg in andmed:
        if kasutaja_sisend in veerg:
            aeg = data[data['Title'].str.contains(kasutaja_sisend, regex=False)]
            aeg = aeg[(aeg['Duration'] > '0 days 00:01:00')]
            kokku = ("Oled vaadanud seda: "+  str(aeg['Duration'].sum()))
            return kokku
        
def uue_akna_graafikud():
    data = pd.read_csv('KertuViewingActivity.csv')
    for veerg in data["Start Time"]:
        data = data.set_index('Start Time')

def päevad():
    data = pd.read_csv('KertuViewingActivity.csv')
    for veerg in data["Start Time"]:
        data["Start Time"] = pd.to_datetime[veerg]
        data = data.set_index('Start Time')
        data.index = data.index.tz_localize('UTC').tz_convert('Eastern/European')
        data = data.reset.index()
        print(data.head(1))
        
def üldine_info_aken():
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
    plot.suptitle("Kokku oled vaadanud Netflixi: "+ str(kogu_aeg()), fontsize = 16)
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

def kas_pilt_on():
    if os.path.exists("000001.png"):
        uusraam = Toplevel(raam) #toplevel uus aken
        uusraam.title(str(sisend.get()))
        uusraam.geometry("1000x600")
        uusraam.configure(bg="white")
        nimi = Label(uusraam, text = sisend.get().upper(), bg="white",font=("Graphique", 17)).pack(pady=20)
        aeg = Label(uusraam, text = send(), font=("Graphique", 15),bg="white").pack()
        im = Image.open("000001.png")
        ph = ImageTk.PhotoImage(r"/Users/kertujogi/Desktop/progeprojekt", master = raam)

        label = Label(uusraam, image=ph)
        label.image=ph
    else:
        print("loll")    

def kogu_aeg():
    data = pd.read_csv('KertuViewingActivity.csv')
    kokku=pd.to_timedelta(data['Duration']).sum()
    return kokku

def graafik1():
    with open("KertuViewingActivity.csv") as f:
        loeb = csv.reader(f)
        kasutaja_sisend = sisend.get()
        E = 0
        T = 0
        K = 0
        N = 0
        R = 0
        L = 0
        P = 0
        listike=[]
        for row in loeb:
            pealkiri = row[4]
            aeg = row[1]
            if kasutaja_sisend in pealkiri:
                rida = aeg.split()
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
        plot.show()
    
def graafik2():
    with open("KertuViewingActivity.csv") as f:
        loeb = csv.reader(f)
        kasutaja_sisend = sisend.get()
        aastaajad=[]
        Suvi=0
        Sügis=0
        Talv=0
        Kevad=0
        for row in loeb:
            pealkiri = row[4]
            aeg = row[1]
            if kasutaja_sisend in pealkiri:
                üks_rida = aeg.split()
                uus1 = üks_rida[0]
                uus2 = uus1.split("-")
                kuu = uus2[1]
                if kuu == "01" or kuu == "02" or kuu == "12":
                    Talv += 1
                elif kuu == "03" or kuu == "04" or kuu == "05":
                    Kevad += 1
                elif kuu == "06" or kuu == "07" or kuu == "08":
                    Suvi += 1
                else:
                    Sügis += 1
    aastaajad.extend([Talv, Kevad, Suvi, Sügis])
    plot.bar(["Talv","Kevad", "Suvi", "Sügis"],aastaajad , color ="red")
    plot.title("Oled vaadanud Netflixi nende aastaaegadel")
    plot.show()

def graafik3():
    with open("KertuViewingActivity.csv") as f:
        loeb = csv.reader(f)
        kasutaja_sisend = sisend.get()
        s=0
        k=0
        ü=0
        üks=0
        kaks=0
        listike=[]
        for row in loeb:
            pealkiri = row[4]
            aeg = row[1]
            if kasutaja_sisend in pealkiri:
                osad = aeg.split()
                osad2 = osad[0]
                osad3 = osad2.split("-")
                aasta = osad3[0]
                if aasta == "2017":
                    s+=1
                if aasta == "2018":
                    k += 1
                if aasta == "2019":
                    ü += 1
                if aasta == "2020":
                    kaks += 1
                if aasta == "2021":
                    üks +=1
        listike.extend([s,ü,k,kaks,üks])
        plot.bar(["2017","2018", "2019", "2020", "2021"], listike, color ="red")
        plot.show()
        
def graafik4():#Kellajad
    with open("KertuViewingActivity.csv") as f:
        loeb = csv.reader(f)
        kasutaja_sisend = sisend.get()
        hommik = 0 #06-12
        päev = 0 #12-6
        õhtu = 0 #6-00
        öö = 0 #00-06
        listike = []
        for row in loeb:
             pealkiri = row[4]
             aeg = row[1]
             if kasutaja_sisend in pealkiri:
                osad = aeg.split(" ")
                osad2 = osad[1]
                kell = int(osad2[0:2])
                if kell >= 6 and kell < 12:
                    hommik += 1
                elif kell >=12 and kell < 18:
                    päev +=1
                elif kell >=18 and kell < 24:
                    õhtu += 1
                else:
                    öö += 1
        
        listike.extend([hommik, päev, õhtu, öö])
        y = np.array(listike)
        tähistused = ["Hommik","Päev", "Õhtu", "Öö"]
        värvid = ["crimson", "firebrick", "red", "maroon"]
        plot.pie(y, labels = tähistused, colors = värvid)
        plot.title("Oled vaadanud seda nendel aegadel")
        plot.show() 

raam.call('wm', 'iconphoto', raam._w, PhotoImage(file='n.png'))
raam.title("Netflix andmeanalüüs")
raam.configure(bg="white")
raam.geometry("1000x600")
pilt = PhotoImage(file="pilt.png")
silt = Label(image=pilt)
silt.pack()

sisendi_silt = Label(raam, text="Kirjuta siia sarja või filmi nimi:", bg ="white", fg="red", font="Graphique 15")
sisendi_silt.pack(pady=20)
sisend = Entry(raam, width=40, font="Graphique 15")
sisend.pack()
nupp = Button(raam, text="Näita", command=kasutaja_sisend, bg="white", fg="red2", font="Graphique 15").pack()
Üldised_andmed= Button(raam, text="Kõik andmed", command=üldine_info_aken, bg="white",  fg="red2", font="Graphique 15").pack(pady=20)
raam.mainloop()