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
    s=0
    k=0
    ü=0
    üks=0
    kaks=0
    listike=[]
    for row in loeb:
        pealkiri = row[4]
        aeg = row[1]
        if "Modern Family" in pealkiri:
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
#     plot.subplot(1, 2, 1)
    plot.bar(["2017","2018", "2019", "2020", "2021"], listike, color ="red")
    plot.show()
        
#         print(aasta)