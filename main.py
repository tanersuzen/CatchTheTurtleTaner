import turtle
from turtle import Turtle
from random import random
import time

game_board = turtle.Screen()
game_board.bgcolor("#cbbeb5")

catch_turtle = Turtle()
catch_turtle.shape("turtle")
catch_turtle.color("green")
catch_turtle.shapesize(1.3)

my_time = 20

def counterclock():
    turtle.write(f"Time: {my_time}", align="center", font=("Arial", 20, "normal"))

for x in range(my_time,0,-1):
    counterclock()
    time.sleep(1)
    my_time = my_time -1
    turtle.clear()

def endgame():
    turtle.write("Game is Over",align="center",font=("Arial",20,"normal"))

if my_time == 0:
    endgame()



catch_turtle.screen.mainloop()
