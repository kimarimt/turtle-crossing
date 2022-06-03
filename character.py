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

    def advance(self):
        self.forward(2.5)

    def reaches_goal(self):
        return self.ycor() > 270

    def reset_position(self):
        self.hideturtle()
        self.goto(self.start_position)
        self.showturtle()
