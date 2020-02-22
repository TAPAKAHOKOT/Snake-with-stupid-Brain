from random import randint as rnd
from random import choice as chs
import turtle as tt


class Apple:
    def __init__(self, settings, snakes):
        self.settings = settings

        self.dwr = tt.Turtle()
        self.dwr.speed(0)
        self.dwr.hideturtle()

        self.width_size = len(self.settings.cells_st[0])
        self.height_size = len(self.settings.cells_st)

        self.x_pos = 0
        self.y_pos = 0

        while not self.x_pos and not self.y_pos:
            self.x_pos = rnd(0, self.width_size - 1)
            self.y_pos = rnd(0, self.height_size - 1)

            for snake in snakes:
                if (self.x_pos, self.y_pos) in zip(snake.x_pos, snake.y_pos):
                    self.x_pos = 0
                    self.y_pos = 0
                    break

    def draw(self):

        self.dwr.clear()

        self.dwr.up()
        self.dwr.goto(
            -self.settings.window_size[0] // 2 + 25 +
            self.settings.cell_size *
            (self.x_pos),

            self.settings.window_size[1] // 2 - 25 -
            self.settings.cell_size *
            (self.y_pos + 1)
        )
        self.dwr.down()

        self.dwr.begin_fill()
        self.dwr.setheading(0)

        for k in range(4):
            self.dwr.fd(self.settings.cell_size)
            self.dwr.left(90)

        self.dwr.end_fill()
