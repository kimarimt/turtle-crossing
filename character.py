from turtle import Turtle


class Character(Turtle):
    start_position = (0, -225)

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape('turtle')
        self.color('green')
        self.goto(self.start_position)
        self.setheading(90)
        self.showturtle()
