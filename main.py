from turtle import *
import random

#
MINIMUM_BRANCH_LENGTH = 5
MOVEMENT = 150

if __name__ == "__main__":
   #Turt config

    tree = Turtle()
    tree.width(5)
    tree.hideturtle()
    tree.penup()
    tree.setpos(0, -375)
    tree.pendown()
    tree.setheading(90)
    tree.color('green')
    #tree.forward(50)
    

    #SCREEN
    tree.screen.colormode(255)
    pos_array = []

    def branch(length):
        if length < MINIMUM_BRANCH_LENGTH:
            return
        tree.forward(length)
        tree.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        branch(length * .67)
        pos_array.append(tree.position())

    branch(MOVEMENT)
    print(pos_array)
    tree.screen.mainloop()