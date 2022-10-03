from tkinter import CENTER
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from bars import Bars
import time
import random

##### creates the screen
screen = Screen()
screen.setup(width = 800, height= 600)
screen.bgcolor('black')
screen.title("Breakout Game")
# screen.tracer(0) # turn off the animation

##### Paddle
paddle = Paddle((0,-200)) 
ball = Ball()
bar = Bars()


screen.exitonclick()