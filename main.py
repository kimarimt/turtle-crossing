import turtle
from character import Character
from car import Car


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
START_POSITION = (0, -225)

screen = turtle.getscreen()
screen.title('Turtle Crossing')
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.clear()

screen.tracer(False)
character = Character()
car = Car()
screen.tracer(True)


if __name__ == '__main__':
    game_is_on = True
    screen.onkey(character.advance, 'w')
    screen.listen()

    while game_is_on:
        screen.update()
        car.drive()

        if character.reaches_goal():
            screen.tracer(False)
            character.reset_position()
            screen.tracer(True)

        if car.xcor() > 270:
            car.reset_position()
