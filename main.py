import turtle
from turtle import Turtle
import random
import time

game_board = turtle.Screen()
game_board.bgcolor("#cbbeb5")
my_time = 20
scorenum = 0
game_over = False
catch_turtle = turtle.Turtle()
clock = Turtle()
score = Turtle()

def catching():
    catch_turtle.clear()
    catch_turtle.shape("turtle")
    catch_turtle.color("green")
    catch_turtle.shapesize(3, 3)
    catch_turtle.penup()
    catch_turtle.speed(0)
    if not game_over:
        catch_turtle.onclick(handclick)
        positionx = random.randint(-300, 300)
        positiony = random.randint(-300, 300)
        catch_turtle.setposition(positionx, positiony)
        game_board.ontimer(catching,620)
    else:
        catch_turtle.hideturtle()

def timer(my_time):
    global game_over
    clock.penup()
    clock.hideturtle()
    clock.setposition(0, 270)
    clock.clear()
    if my_time > 0:
        clock.clear()
        clock.hideturtle()
        clock.write(f"Time: {my_time}", align="center", font=("Arial", 20, "normal"))
        game_board.ontimer(lambda: timer(my_time-1),1000)
    else:
        game_over = True
        clock.clear()
        clock.write("Game is Over!", align="center", font=("Arial", 20, "normal"))
        endgame = Turtle()
        endgame.penup()
        endgame.hideturtle()
        endgame.setposition(0, 0)
        endgame.write(f"Final Score: {scorenum}", align="center", font=("Arial", 20, "normal"))

def scoring():
    score.color("dark blue")
    score.penup()
    score.hideturtle()
    score.setposition(0,300)
    global scorenum
    score.write(f"Score: {scorenum}", align="center", font=("Arial", 24, "normal"))

def handclick(x,y):
    global scorenum
    scorenum += 1
    score.clear()
    score.write(f"Score: {scorenum}", align= "center", font=("Arial",24,"normal"))

def gamestartup():
    scoring()
    timer(my_time)
    catching()



gamestartup()

turtle.mainloop()