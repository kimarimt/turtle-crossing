import turtle


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
START_POSITION = (0, -225)

screen = turtle.getscreen()
screen.title('Turtle Crossing')
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.clear()

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()
turtle.shape('turtle')
turtle.color('green')
turtle.goto(START_POSITION)
turtle.setheading(90)
turtle.showturtle()


if __name__ == '__main__':
    screen.exitonclick()
