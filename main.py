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
    game_is_on = True
    screen.onkey(turtle.advance, 'w')
    screen.listen()

    while game_is_on:
        screen.update()

        if turtle.reaches_goal():
            screen.tracer(False)
            turtle.reset()
            screen.tracer(True)
        
