import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import pandas as pd
import numpy as np
from tkinter import *
from PIL import ImageTk, Image
from icrawler.builtin import GoogleImageCrawler
import os
import time

def päevad():
    data = pd.read_csv('KertuViewingActivity.csv')
    data['Duration'] = pd.to_timedelta(data['Duration'])
    data["Start Time"]=pd.to_datetime(data['Start Time'], utc=True)
    data = data.set_index('Start Time')
    data.index=data.tz_convert('US/Eastern')
    data = data.reset_index()
    #kasutaja_sisend = str(sisend.get())
    for veerg in andmed:
        if kasutaja_sisend in veerg:
            #aeg = data[data['Title'].str.contains(kasutaja_sisend, regex=False)]
            kasutaja_sisend["weekday"]=kasutaja_sisend["Start Time"].dt.weekday
            kasutaja_sisend["hour"] = kasutaja_sisend["Start Time"].dt.hour
            kasutaja_sisend['weekday'] = pd.Categorical(office['weekday'], categories=[0,1,2,3,4,5,6], ordered=True)
            kasutaja_sisend_by_day = kasutaja_sisend['weekday'].value_counts()
            kasutaja_sisend_by_day = office_by_day.sort_index()
            matplotlib.rcParams.update({'font.size': 22})
            kasutaja_sisend_by_day.plot(kind='bar', figsize=(20,10), title='Office Episodes Watched by Day')
    

kasutaja_sisend=input("Sisesta: ")
päevad()
 
    

