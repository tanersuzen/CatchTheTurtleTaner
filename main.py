import turtle
from turtle import Turtle
import random
from random import randint
import time

game_board = turtle.Screen()
game_board.bgcolor("#cbbeb5")
my_time = 20

catch_turtle = Turtle()
catch_turtle.shape("turtle")
catch_turtle.color("green")
catch_turtle.shapesize(1.3)
catch_turtle.penup()
catch_turtle.speed(0)

clock = Turtle()
clock.penup()
clock.hideturtle()
clock.setposition(0, 270)

def mainfunc():
    my_time = 20
    for x in range(my_time, 0, -1):
        clock.write(f"Time: {my_time}", align="center", font=("Arial", 20, "normal"))
        time.sleep(0.5)
        my_time = my_time - 1
        for el in range(0,1):
            positionx = random.randint(-300, 300)
            positiony = random.randint(-300, 300)
            catch_turtle.setposition(positionx, positiony)
            time.sleep(0.25)
        clock.clear()
    if my_time == 0:
        endgame = Turtle()
        endgame.penup()
        endgame.hideturtle()
        endgame.setposition(0, 0)
        endgame.write("Game is Over", align="center", font=("Arial", 20, "normal"))

mainfunc()

game_board.mainloop()