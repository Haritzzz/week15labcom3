import tkinter as tk
from tkinter import *
import os

#-------------------------------def
def game_1(): #เกมใบ้คำ
    win.destroy()
    filename = 'menu0.py'
    os.system(filename)

def game_2(): #เกมบิงโก
    pass

def game_3(): #เกมซูโดกุ
    pass

def game_4(): #เกมงู
    pass

def game_5(): #เกมหมากฮอส
    pass

def game_6(): #เกมวิ่งแข่ง
    pass

#-------------------------------label
win = Tk()
win.title("MINIGAMES")
win.geometry("1200x1200")
#win.tk.call('wm','iconphoto',win._w,PhotoImage(file='unnamed1.png'))
win.configure(bg="#FE8D6F")

L_0 = Label(win,text="MINIGAMES",font=("Comic Sans MS",64),bg="#FE8D6F",fg="white")
L_0.place(x=320,y=50)

def on_hover(button, colorOnHover, colorOnLeave):
	button.bind("<Enter>", func=lambda e: button.config(background="#A0DDE0",foreground=colorOnHover))
	button.bind("<Leave>", func=lambda e: button.config(background="#A0DDE0",foreground=colorOnLeave))

class RoundedButton(tk.Canvas):
    def __init__(self, parent, width, height, cornerradius, padding, color, bg, command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0, 
            relief="flat", highlightthickness=0, bg=bg)
        self.command = command

        if cornerradius > 0.5*width:
            print("Error: cornerradius is greater than width.")
            return None

        if cornerradius > 0.5*height:
            print("Error: cornerradius is greater than height.")
            return None

        rad = 2*cornerradius
        def shape():
            self.create_polygon((padding,height-cornerradius-padding,padding,cornerradius+padding,padding+cornerradius,padding,width-padding-cornerradius,padding,width-padding,cornerradius+padding,width-padding,height-cornerradius-padding,width-padding-cornerradius,height-padding,padding+cornerradius,height-padding), fill=color, outline=color)
            self.create_arc((padding,padding+rad,padding+rad,padding), start=90, extent=90, fill=color, outline=color)
            self.create_arc((width-padding-rad,padding,width-padding,padding+rad), start=0, extent=90, fill=color, outline=color)
            self.create_arc((width-padding,height-rad-padding,width-padding-rad,height-padding), start=270, extent=90, fill=color, outline=color)
            self.create_arc((padding,height-padding-rad,padding+rad,height-padding), start=180, extent=90, fill=color, outline=color)


        id = shape()
        (x0,y0,x1,y1)  = self.bbox("all")
        width = (x1-x0)
        height = (y1-y0)
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()

b_1 = Button(win,text="WORD GUESS",command=game_1,font=("Comic Sans MS",24),bg="#A0DDE0",fg="black",activebackground="#789CCE",activeforeground="white")
#b_1 = RoundedButton(win, 250, 150, 50, 2, '#A0DDE0', '#FE8D6F', command=game_1)
b_1.place(x=200,y=200,height=150,width=250)
#l_b_1 = Label(text="WORD GUESS",font=("Comic Sans MS",24),bg="#A0DDE0")
#l_b_1.place(x=215,y=250,height=50,width=225)
on_hover(b_1,"white","black")

#b_2 = Button(win,text="BINGO",command=game_2,font=("Comic Sans MS",24),bg="#A0DDE0",fg="black",activebackground="#789CCE",activeforeground="white") 
b_2 = RoundedButton(win, 250, 150, 50, 2, '#A0DDE0', '#FE8D6F', command=game_2)
b_2.place(x=200,y=400,height=150,width=250)
l_b_2 = Label(text="BINGO",font=("Comic Sans MS",24),bg="#A0DDE0")
l_b_2.place(x=215,y=450,height=50,width=225)
on_hover(l_b_2,"white","black")

#b_3 = Button(win,text="SUDOKU",command=game_3,font=("Comic Sans MS",24),bg="#A0DDE0",fg="black",activebackground="#789CCE",activeforeground="white") 
b_3 = RoundedButton(win, 250, 150, 50, 2, '#A0DDE0', '#FE8D6F', command=game_3)
b_3.place(x=200,y=600,height=150,width=250)
l_b_3 = Label(text="SUDOKU",font=("Comic Sans MS",24),bg="#A0DDE0")
l_b_3.place(x=215,y=650,height=50,width=225)
on_hover(l_b_3,"white","black")

#b_4 = Button(win,text="SNAKE",command=game_4,font=("Comic Sans MS",24),bg="#A0DDE0",fg="black",activebackground="#789CCE",activeforeground="white") 
b_4 = RoundedButton(win, 250, 150, 50, 2, '#A0DDE0', '#FE8D6F', command=game_4)
b_4.place(x=750,y=200,height=150,width=250)
l_b_4 = Label(text="SUDOKU",font=("Comic Sans MS",24),bg="#A0DDE0")
l_b_4.place(x=765,y=250,height=50,width=225)
on_hover(l_b_4,"white","black")

#b_5 = Button(win,text="CHECKERS",command=game_5,font=("Comic Sans MS",24),bg="#A0DDE0",fg="black",activebackground="#789CCE",activeforeground="white")
b_5 = RoundedButton(win, 250, 150, 50, 2, '#A0DDE0', '#FE8D6F', command=game_5)
b_5.place(x=750,y=400,height=150,width=250)
l_b_5 = Label(text="CHECKERS",font=("Comic Sans MS",24),bg="#A0DDE0")
l_b_5.place(x=765,y=450,height=50,width=225)
on_hover(l_b_5,"white","black")

#b_6 = Button(win,text="RACE GAME",command=game_6,font=("Comic Sans MS",24),bg="#A0DDE0",fg="black",activebackground="#789CCE",activeforeground="white")
b_6 = RoundedButton(win, 250, 150, 50, 2, '#A0DDE0', '#FE8D6F', command=game_6)
b_6.place(x=750,y=600,height=150,width=250)
l_b_6 = Label(text="RACE GAME",font=("Comic Sans MS",24),bg="#A0DDE0")
l_b_6.place(x=765,y=650,height=50,width=225)
on_hover(l_b_6,"white","black")

win.mainloop()