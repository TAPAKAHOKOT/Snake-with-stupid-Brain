from random import randint as rnd
from random import choice as chs
import turtle as tt
import numpy as np


class Snake:
    def __init__(self, settings):
        self.settings = settings

        self.score = 0

        self.dwr = tt.Turtle()
        self.dwr.speed(0)
        self.dwr.hideturtle()

        self.width_size = len(self.settings.cells_st[0])
        self.height_size = len(self.settings.cells_st)

        self.x_pos = [rnd(0, self.width_size - 1)]
        self.y_pos = [rnd(0, self.height_size - 1)]

        rn_speed = rnd(-1, 1)
        self.speed = [rn_speed, chs([-1, 1]) if rn_speed == 0 else 0]

        self.settings.dead_cells.append([self.x_pos[0], self.y_pos[0]])
        self.to_move = ["W", "N", "E", "S"]

        self.last_side = "N"

        self.color = chs(self.settings.colors)
        self.head_color = chs(self.settings.colors)

    def draw(self):

        self.dwr.clear()

        for k in range(len(self.x_pos)):

            self.dwr.up()
            self.dwr.goto(
                -self.settings.window_size[0] // 2 + 25 +
                self.settings.cell_size *
                (self.x_pos[k]),

                self.settings.window_size[1] // 2 - 25 -
                self.settings.cell_size *
                (self.y_pos[k] + 1)
            )
            self.dwr.down()

            if k == 0:
                self.dwr.fillcolor(self.head_color)

            self.dwr.begin_fill()
            self.dwr.setheading(0)

            for k in range(4):
                self.dwr.fd(self.settings.cell_size)
                self.dwr.left(90)

            self.dwr.end_fill()

            self.dwr.fillcolor(self.color)

    def update(self, snakes, this_snake):
        # try:
        #     self.settings.dead_cells.remove(
        #         [self.x_pos[-1], self.y_pos[-1]])
        # except:
        #     pass

        for k in range(1, len(self.x_pos)):
            self.x_pos[-k] = self.x_pos[-k - 1]
            self.y_pos[-k] = self.y_pos[-k - 1]

        self.x_pos[0] += self.speed[0]
        self.y_pos[0] += self.speed[1]

        # self.settings.dead_cells.append([self.x_pos[0], self.y_pos[0]])

        return self.check_lose(snakes, this_snake)
        # return False

    def inc_tail(self):
        self.x_pos.append(self.x_pos[-1])
        self.y_pos.append(self.y_pos[-1])

        self.score += 1
        # print("Score is >>> ", self.score)

    def change_direct(self, side):
        if side == "N" and self.speed != [0, 1]:
            self.speed = [0, -1]
        elif side == "S" and self.speed != [0, -1]:
            self.speed = [0, 1]
        elif side == "E" and self.speed != [-1, 0]:
            self.speed = [1, 0]
        elif side == "W" and self.speed != [1, 0]:
            self.speed = [-1, 0]

    def check_lose(self, snakes, this_snake):
        if self.settings.cells_num[0] - 1 < self.x_pos[0] or\
                0 > self.x_pos[0] or\
                self.settings.cells_num[1] - 1 < self.y_pos[0] or\
                0 > self.y_pos[0]:
            self.dwr.clear()

            # for k in range(len(self.x_pos)):
            #     self.settings.dead_cells.append([self.x_pos[k], self.y_pos[k]])

            return True

        for snake in snakes:
            if snake != this_snake:
                if (self.x_pos[0], self.y_pos[0]) in zip(snake.x_pos, snake.y_pos):
                    if len(snakes) > 1:
                        self.dwr.clear()
                    return True
            else:
                if (self.x_pos[0], self.y_pos[0]) in zip(snake.x_pos[1:], snake.y_pos[1:]):
                    if len(snakes) > 1:
                        self.dwr.clear()
                    return True
        return False

    def check_apple_eating(self, apple):

        if [self.x_pos[0], self.y_pos[0]] == [apple.x_pos, apple.y_pos]:
            return True
        return False

    def brain(self, apples, snakes):
        apple_pos = []
        for apple in apples:
            apple_pos.append([apple.x_pos, apple.y_pos])

        # self.arr_app = np.random.rand(7, 7) - 0.5
        self.arr_app = [
            [0, 1, 1, 1, 1, 1, 0],
            [1, 1, 2, 3, 2, 1, 1],
            [1, 2, 6, 8, 6, 2, 1],
            [1, 3, 8, 0, 8, 3, 1],
            [1, 2, 6, 8, 6, 2, 1],
            [1, 1, 2, 3, 2, 1, 1],
            [0, 1, 1, 1, 1, 1, 0]
        ]

        self.arr_block = [
            [-2, -2, -2, -2, -2, -2, -2],
            [-2, -2, -3, -4, -3, -2, -2],
            [-2, -3, -10, -20, -10, -3, -2],
            [-2, -4, -20, 0, -20, -4, -2],
            [-2, -3, -10, -20, -10, -3, -2],
            [-2, -2, -3, -4, -3, -2, -2],
            [-2, -2, -2, -2, -2, -2, -2]
        ]
        # self.arr_block = np.random.rand(7, 7) - 0.5

        weights_sum = [0, 0, 0, 0]

        for i in range(7):
            for k in range(7):
                if [self.x_pos[0] + k - 3, self.y_pos[0] + i - 3] in apple_pos:
                    if k < 3:
                        weights_sum[0] += self.arr_app[i][k]

                    if k > 3:
                        weights_sum[2] += self.arr_app[i][k]

                    if i < 3:
                        weights_sum[1] += self.arr_app[i][k]

                    if i > 3:
                        weights_sum[3] += self.arr_app[i][k]

                for snake in snakes:
                    if (self.x_pos[0] + k - 3, self.y_pos[0] + i - 3)\
                            in zip(snake.x_pos, snake.y_pos):
                        if k < 3:
                            weights_sum[0] += self.arr_block[i][k]

                        if k > 3:
                            weights_sum[2] += self.arr_block[i][k]

                        if i < 3:
                            weights_sum[1] += self.arr_block[i][k]

                        if i > 3:
                            weights_sum[3] += self.arr_block[i][k]

                if (self.x_pos[0] + k - 3, self.y_pos[0] + i - 3)\
                        in zip(self.x_pos[1:], self.y_pos[1:]):
                    if k < 3:
                        weights_sum[0] += self.arr_block[i][k]

                    if k > 3:
                        weights_sum[2] += self.arr_block[i][k]

                    if i < 3:
                        weights_sum[1] += self.arr_block[i][k]

                    if i > 3:
                        weights_sum[3] += self.arr_block[i][k]

                if (self.x_pos[0] + k - 3) < 0:
                    weights_sum[0] += self.arr_block[i][k]
                    self.last_side = "W"
                if (self.x_pos[0] + k - 3) > (self.width_size - 1):
                    self.last_side = "E"
                    weights_sum[2] += self.arr_block[i][k]
                if (self.y_pos[0] + i - 3) < 0:
                    weights_sum[1] += self.arr_block[i][k]
                    self.last_side = "N"
                if (self.y_pos[0] + i - 3) > (self.height_size - 1):
                    weights_sum[3] += self.arr_block[i][k]
                    self.last_side = "S"

        # print(weights_sum)
        inds = []

        # print("ls = ", self.last_side)
        if weights_sum.count(max(weights_sum)) > 1:
            for k in range(4):
                if weights_sum[k] == max(weights_sum):
                    inds.append(k)

            if self.last_side == "W" and 2 in inds:
                side = "E"
            elif self.last_side == "E" and 0 in inds:
                side = "W"
            elif self.last_side == "N" and 1 in inds:
                side = "S"
            elif self.last_side == "S" and 3 in inds:
                side = "N"
            else:
                side = self.to_move[chs(inds)]
        else:
            side = self.to_move[weights_sum.index(max(weights_sum))]

        if side == "N" and self.speed == [0, 1]:
            weights_sum[weights_sum.index(max(weights_sum))] -= 100
            side = self.to_move[weights_sum.index(max(weights_sum))]
        elif side == "S" and self.speed == [0, -1]:
            weights_sum[weights_sum.index(max(weights_sum))] -= 100
            side = self.to_move[weights_sum.index(max(weights_sum))]
        elif side == "E" and self.speed == [-1, 0]:
            weights_sum[weights_sum.index(max(weights_sum))] -= 100
            side = self.to_move[weights_sum.index(max(weights_sum))]
        elif side == "W" and self.speed == [1, 0]:
            weights_sum[weights_sum.index(max(weights_sum))] -= 100
            side = self.to_move[weights_sum.index(max(weights_sum))]

        # print(side)

        self.change_direct(side)

        #
        # for i in range(7):
        #     for k in range(7):
        #         if apple_pos == [self.x_pos[0] + k - 3, self.y_pos[0] + i - 3]:
        #             print([self.x_pos[0] + k - 3, self.y_pos[0] + i - 3])
        #             print(arr_app[i, k], arr_block[i, k])
        #
        # print("\n")
