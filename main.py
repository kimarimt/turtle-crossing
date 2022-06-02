import turtle
from character import Character


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
START_POSITION = (0, -225)

screen = turtle.getscreen()
screen.title('Turtle Crossing')
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.clear()

screen.tracer(False)
turtle = Character()
screen.tracer(True)


if __name__ == '__main__':
    screen.exitonclick()
