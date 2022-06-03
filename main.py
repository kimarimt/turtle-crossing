import turtle
import random
from character import Character
from car import Car
from game_handler import GameHandler


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
NUMBER_OF_CARS = 15
START_POSITION = (0, -225)
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

screen = turtle.getscreen()
screen.title('Turtle Crossing')
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.clear()


def get_cars():
    cars = []
    for _ in range(NUMBER_OF_CARS):
        color = random.choice(COLORS)
        car = Car(color)
        cars.append(car)

    return cars


screen.tracer(False)
character = Character()
cars = get_cars()
game_handler = GameHandler()
screen.tracer(True)


if __name__ == '__main__':
    game_is_on = True
    screen.onkey(character.advance, 'w')
    screen.listen()

    while game_is_on:
        screen.update()

        for car in cars:
            screen.tracer(False)
            car.drive()
            screen.tracer(True)

            if car.hits(character):
                game_is_on = False

            if car.xcor() > 270:
                screen.tracer(False)
                car.reset_position()
                screen.tracer(True)

        if character.reaches_goal():
            screen.tracer(False)
            character.reset_position()
            game_handler.update_game(cars)
            screen.tracer(True)

    screen.clear()
    game_handler.end_game()
    screen.exitonclick()
