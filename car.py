from random import randint
from turtle import Turtle


class Car(Turtle):
    speed = 5

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color('green')
        self.goto(-270, 0)
        self.showturtle()

    def drive(self):
        self.forward(5)

    def reset_position(self):
        ycor = randint(-220, 220)
        self.hideturtle()
        self.goto(-270, ycor)
        self.showturtle()
        
