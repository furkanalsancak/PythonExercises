from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("500x300")
def helloCallBack():
   msg=messagebox.showinfo( "Hello Python", "Hello World")
B = Button(top, text ="Hello", command = helloCallBack)
B.place(x=250,y=150)
top.mainloop()