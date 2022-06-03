from turtle import Turtle


class GameHandler(Turtle):
    font = ('Courier', 20, 'normal')

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-180, 215)
        self.write(
            f'Level: {self.level}',
            align='center', font=self.font
        )

    def update_game(self, cars):
        self.level += 1
        self.clear()
        self.write(
            f'Level: {self.level}',
            align='center',
            font=(
                'Courier',
                20,
                'normal'))
        for car in cars:
            car.update_speed()

    def end_game(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=self.font)
