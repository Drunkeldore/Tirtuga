from turtle import *
import random

#
MINIMUM_BRANCH_LENGTH = 20
MOVEMENT = 150
ANGLE = 45
X_ZERO = 0
Y_ZERO = -375
LENGTH_SHORTEN_BY = .67


if __name__ == "__main__":
   #Turt config

    tree = Turtle()
    tree.width(5)
    tree.hideturtle()
    tree.penup()
    tree.setpos(X_ZERO, Y_ZERO)
    tree.pendown()
    tree.setheading(90)
    tree.color("white")

    

    #SCREEN
    tree.screen.colormode(255)
    tree.screen.bgcolor("black")

    def branch(length):
        tree.forward(length)
        left_pos_array = []
        right_pos_array = []
        if length > MINIMUM_BRANCH_LENGTH:

            left_pos_array.append(tree.position())
            tree.setheading(tree.heading() - ANGLE)
            branch(length * LENGTH_SHORTEN_BY)
            tree.setpos(left_pos_array[-1])

            right_pos_array.append(tree.position())
            tree.setheading(tree.heading() + ANGLE)
            branch(length * LENGTH_SHORTEN_BY)
            tree.setpos(right_pos_array[-1])


 
    branch(MOVEMENT)

    # Test to show different parts of pos array
    # print(f"Last turtle position {pos_array[-1]}\n"
    #         f"Second to last turtle position {pos_array[-2]}")
    tree.screen.mainloop()