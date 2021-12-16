'''from tkinter import * 
from tkinter import messagebox
from os import *
window = Tk()
window.title("Welcome")
window.geometry("200x100")
lbl = Label(window,text="Password :")
lbl.grid(column=0,row=0)

def btn_clicked():
    messagebox.showinfo("Display","your type "+txt.get())

btn = Button(window,text="Click",command=btn_clicked)
btn.grid(column=1,row=1)
txt = Entry(window,width=10)
txt.grid(column=1,row=0)
window.mainloop()'''


'''from tkinter import *
window = Tk()
btnRed = Button(window,text="Red",fg="red")
btnRed.pack(side=LEFT)
btnGreen = Button(window,text="Green",fg="green")
btnGreen.pack(side=RIGHT)
btnBlue = Button(window,text="Blue",fg="blue")
btnBlue.pack(side=TOP)
btnBlack = Button(window,text="Black",fg="black")
btnBlack.pack(side=BOTTOM)
window.mainloop()'''


'''from tkinter import *
parent = Tk()
name = Label(parent,text="Name").grid(row=0,column=0)
e1 = Entry(parent).grid(row=0,column=1)
password = Label(parent,text="Password").grid(row=1,column=0)
e2 = Entry(parent).grid(row=1,column=1)
submit = Button(parent,text="Submit").grid(row=4,column=0)
parent.mainloop()'''


'''from tkinter import *
top = Tk()
top.geometry("400x250")
name = Label(top,text="Name").place(x=30,y=50)
email = Label(top,text="Email").place(x=30,y=90)
password = Label(top,text="Password").place(x=30,y=130)
e1=Entry(top).place(x=80,y=50)
e2=Entry(top).place(x=80,y=90)
e3=Entry(top).place(x=80,y=130)
top.mainloop()'''


import tkinter as tk
window = tk.Tk()
window.title("Calculator")
lbl1 = tk.Label(window,text="value A : ")
lbl1.grid(column=0,row=0)
lbl2 = tk.Label(window,text="value B : ")
lbl2.grid(column=0,row=1)
txt1 = tk.Entry(window,width=15)
txt1.grid(column=1,row=0)
txt2 = tk.Entry(window,width=15)
txt2.grid(column=1,row=1)
lblResult = tk.Label(window)
lblResult.grid(column=1,row=3)

def btn_clicked():
    n1 = int(txt1.get())
    n2 = int(txt2.get())
    result = n1 + n2
    lblResult.configure(text=str(result))
    print(result)

btn = tk.Button(window,text="Add",width=12,command=btn_clicked)
btn.grid(column=1,row=2)
window.mainloop()

