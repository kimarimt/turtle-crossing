from random import randint, randrange
from turtle import Turtle


class Car(Turtle):

    def __init__(self, color):
        super().__init__()
        self.mph = randrange(1, 5)
        self.hideturtle()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(color)
        self.speed(0)
        self.goto(-270, randint(-200, 200))
        self.showturtle()

    def drive(self):
        self.forward(self.mph)

    def reset_position(self):
        ycor = randint(-220, 220)
        self.hideturtle()
        self.goto(-270, ycor)
        self.showturtle()

    
    def hits(self, character):
        return self.distance(character.position()) < 10
