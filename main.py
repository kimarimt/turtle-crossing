import turtle
import random
from character import Character


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
START_POSITION = (0, -225)

screen = turtle.getscreen()
screen.title('Turtle Crossing')
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.clear()

screen.tracer(False)
character = Character()
screen.tracer(True)

ycor = random.randint(-220, 220)
car = turtle.Turtle()
car.hideturtle()
car.penup()
car.shape('square')
car.shapesize(stretch_wid=1, stretch_len=2)
car.color('green')
car.goto(-270, 0)
car.showturtle()

def drive():
    car.forward(5)

def reset():
    ycor = random.randint(-220, 220)
    car.hideturtle()
    car.goto(-270, ycor)
    car.showturtle()


if __name__ == '__main__':
    game_is_on = True
    screen.onkey(character.advance, 'w')
    screen.listen()

    while game_is_on:
        screen.update()
        drive()

        if character.reaches_goal():
            screen.tracer(False)
            character.reset()
            screen.tracer(True)

        if car.xcor() > 270:
            reset()
