#chatbot
from tkinter import *
import time
raam = Tk()

def send():
    send = "Sina:" + e.get()
    text.insert(END, "\n"+ send)
    if e.get() == "tere" or e.get() == "jou":
        text.insert(END, "\n" + "Bot: tere")
    elif e.get() == "mis teed":
        text.insert(END, "\n" + "Bot: taun olen")
    else:
        text.insert(END, "\n" + "Bot: midagi")
text = Text(raam, bg="black", fg="white")
text.grid(row = 0, column=0, columnspan=2)

e = Entry(raam, width=70)
send = Button(raam, text="Saada", bg="deeppink", fg="white",
              width=20, command=send).grid(row=1, column=1)
e.grid(row=1, column=0)
raam.title("BOT")
raam.mainloop()
