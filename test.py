from tkinter import *

import tkinter.messagebox
import tkinter.font

def fromrgb(rgb):
    return "#%02x%02x%02x" % rgb   

top = Tk()
top.geometry("500x300+450+300")
top.configure(background = fromrgb((81,118,168)))


helv36 = tkinter.font(family="Helvetica",size=50)

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

def exitdeh():
    tkMessageBox.showinfo("Program Inka", "Horeeeey bisa")

Welcome = Message( top, text = "Welcome!", bg = fromrgb((81,118,168)),fg = 'white', font = helv36, width = 500,)


Input = Button(top, text ="Masukkan Foto", command = top, relief = SUNKEN, bg = fromrgb((81,118,168)))
Exit = Button(top, text ="Keluar", command = exit)

Welcome.pack()
Input.pack()
Exit.pack()

top.mainloop()