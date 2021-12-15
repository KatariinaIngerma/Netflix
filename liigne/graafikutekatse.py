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

with open("KertuViewingActivity.csv") as f:
        loeb = csv.reader(f)
        #kasutaja_sisend = sisend.get()
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
            print(aeg)
            for kasutaja_sisend in pealkiri:
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

# with open("KertuViewingActivity.csv") as f:
#     loeb = csv.reader(f)
#     E = 0
#     T = 0
#     K = 0
#     N = 0
#     R = 0
#     L = 0
#     P = 0
#     #kasutaja_sisend = str(sisend.get())
#     listike=[]
#     for row in loeb:
#         pealkiri=row[4]
#         aeg=row[1]
#         print(aeg)
#         for kasutaja_sisend in pealkiri:
#             rida = aeg.split()
#             uus1 = rida[0]
#             uus2 = uus1.split("-")
#             uus3 = uus2[::-1]
#             string = " ".join(uus3)
#             päev = datetime.datetime.strptime(string,'%d %m %Y').weekday()
#             päeva_nimi = calendar.day_name[päev]
#             if päeva_nimi == "Monday":
#                 E += 1
#             elif päeva_nimi == "Tuesday":
#                 T += 1
#             elif päeva_nimi == "Wednesday":
#                 K += 1
#             elif päeva_nimi == "Thursday":
#                 N += 1
#             elif päeva_nimi == "Friday":
#                 R += 1
#             elif päeva_nimi == "Saturday":
#                 L += 1
#             elif päeva_nimi == "Sunday":
#                 P += 1
#     listike.extend([E,T,K,N,R,L,P])
#     plot.subplot(1, 2, 1)
#     plot.bar(["E","T", "K", "N", "R", "L", "P"], listike, color ="red")
#     plot.title("Oled vaadanud Netflixi nende päevadel")
#     plot.show()


#     #kasutaja_sisend = sisend.get()
#     E = 0
#     T = 0
#     K = 0
#     N = 0
#     R = 0
#     L = 0
#     P = 0
#     listike=[]
#     for row in loeb:
#         pealkiri = row[4]
#         aeg = row[1]
#         if "Friends" in pealkiri:
#             rida = aeg.split()
#             uus1 = rida[0]
#             uus2 = uus1.split("-")
#             #print(uus2)
#             uus3 = uus2[0]+uus2[1]+uus2[2]
#             string = " ".join(uus3)
#             päev = datetime.datetime.strptime(string,'%Y %m %d').weekday()
#             päeva_nimi = calendar.day_name[päev]
#             
#     print(uus3)