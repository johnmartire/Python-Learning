from turtle import Screen, Turtle
from paddle import Paddle
import random
import time
T=Turtle
paddle=Paddle

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG")
game_is_on = True



while game_is_on:
    screen.update()
    time.sleep(.1)



#Create the screen
#Create and move a paddle
#create another paddle
#create the ball and make it move
#Detect collision and wall and bounce
#detect collision with paddle 
#Detect when paddle misses
#keep score







screen.exitonclick()