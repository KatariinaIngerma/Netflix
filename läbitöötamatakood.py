from tkinter import *
def task(event):
    print("Hello") 
def quit(event):                           
    print("Double click  to stop") 
    import sys; sys.exit()

ws=Tk()
ws.title("Python guides")
ws.geometry("200x200") 

button = Button(ws, text='Press')
button.pack(pady=10)
button.bind('<Button-1>', task)
button.bind('<Double-1>', quit) 
button.mainloop()