'''#Import required libraries
from tkinter import *
#Create an instance of tkinter frame
win= Tk()
#Define the geometry of the window
win.geometry("750x250")
#Define functions
def on_enter(e):
   button.config(background='OrangeRed3', foreground= "white")

def on_leave(e):
   button.config(background= 'SystemButtonFace', foreground= 'black')
#Create a Button
button= Button(win, text= "Click Me", font= ('Helvetica 13 bold'))
button.pack(pady= 20)

#Bind the Enter and Leave Events to the Button
button.bind('<Enter>', on_enter)
button.bind('<Leave>', on_leave)
win.mainloop()'''

'''import tkinter as tk
root =tk.Tk()
btn = tk.Button(text="Button",activebackground="red").pack()
root.mainloop()'''

'''# import required module
from tkinter import *


# function to change properties of button on hover
def changeOnHover(button, colorOnHover, colorOnLeave):

	# adjusting backgroung of the widget
	# background on entering widget
	button.bind("<Enter>", func=lambda e: button.config(
		background=colorOnHover))

	# background color on leving widget
	button.bind("<Leave>", func=lambda e: button.config(
		background=colorOnLeave))


# Driver Code
root = Tk()

# create button
# assign button text along
# with background color
myButton = Button(root,
				text="On Hover - Background Change",
				bg="yellow")
myButton.pack()

# call function with background
# colors as argument
changeOnHover(myButton, "red", "yellow")

root.mainloop()'''

from tkinter import *
import tkinter as tk

root = Tk()
root.geometry("1000x1000")
root.configure(bg="#FE8D6F")

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

def test():
    print("Hello")

button1 = (RoundedButton(root, 200, 100, 50, 2, '#A0DDE0', '#FE8D6F', command=test))
l_button1 = Label(text="hello",font=("Comic Sans MS",24),bg="#A0DDE0",fg="black")
l_button1.place(x=200,y=200)
button1.place(x=200,y=200)

button2 = RoundedButton(root, 200, 100, 50, 2, 'red', 'white', command=test)
button2.place(relx=.6, rely=.6)

root.mainloop()