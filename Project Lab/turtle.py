from turtle import Turtle, Screen
import random
from tkinter import messagebox

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet =screen.textinput(title="เริ่มต้นทายเต่า", prompt="เต่าตัวไหนจะชนะการเเข่งขัน?  \nred,orange,green,black,blue,purple\nพิมพ์สีของเต่า  ")
colors =["red","orange","green","black","blue","purple"]
y_positions =[-70,-40,-10, 20, 50, 80]
all_turtles = []

for turtle_index in range (0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= -230 ,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True  

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color =turtle.pencolor()
            if wining_color == user_bet:
                messagebox.showinfo("คุณชนะ",f"ผู้ชนะคือ เต่าสี {wining_color} !!")
            else:
                messagebox.showinfo("คุณแพ้",f"ผู้ชนะคือ เต่าสี {wining_color} !!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()