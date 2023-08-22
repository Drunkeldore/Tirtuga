from turtle import *

MOVEMENT = 300
INITIAL_ANGLE = 90

class Turt(Turtle):
    def __init__(self):
        super().__init__() # We had to set this super init to inherit everything from Turtle() instead of setting up a base turtle. This interferes with movement and position if you don't.
        self.penup()
        self.speed(5)
        self.hideturtle()
        self.shape("turtle")
        self.shapesize(2,2)
        self.goto(0, -350)
        self.showturtle()
        self.pendown()
        self. seth(INITIAL_ANGLE)
        self.forward(MOVEMENT)

    def branch(self, angle, b_length):
        self.seth(INITIAL_ANGLE + angle)
        self.forward(b_length)