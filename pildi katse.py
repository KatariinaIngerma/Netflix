from PIL import ImageTk, Image
import tkinter
from tkinter import *
from PIL import Image, ImageTk

raam = Tk()

image1 = Image.open("/Users/kertujogi/Desktop/progeprojekt")
test = ImageTk.PhotoImage(image1)
image1 = img.resize((50, 50), Image.ANTIALIAS)
label1 = tkinter.Label(image=test)
label1.image = test
raam.mainloop()

