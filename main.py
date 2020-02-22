from settings import *
from functions import *
from zmeya import Snake
from apple import Apple
from time import sleep
import keyboard as kb
import msvcrt as m
import os

from random import choice as chs
from random import randint as rnd

settings = Settings()

settings.cells_st = draw_field(
    settings.dwr, settings.cell_size, settings.window_size)
settings.cells_num = [len(settings.cells_st[0]), len(settings.cells_st[1])]

arr = [Snake(settings) for k in range(30)]

apples = [Apple(settings, arr)]


def snake_left():
    if settings.manual_control:
        for snake in arr:
            snake.change_direct("W")


def snake_up():
    if settings.manual_control:
        for snake in arr:
            snake.change_direct("N")


def snake_right():
    if settings.manual_control:
        for snake in arr:
            snake.change_direct("E")


def snake_down():
    if settings.manual_control:
        for snake in arr:
            snake.change_direct("S")


kb.add_hotkey('left', snake_left)
kb.add_hotkey('up', snake_up)
kb.add_hotkey('right', snake_right)
kb.add_hotkey('down', snake_down)

counter = 0
max_score = 0
while True:
    counter += 1

    for snake in arr:
        if snake.score > max_score:
            max_score = snake.score
        if snake.update(arr, snake):
            arr.remove(snake)
            break

        for apple in apples:
            if snake.check_apple_eating(apple):
                snake.inc_tail()

                apple.dwr.clear()

                apples.remove(apple)
                apples.append(Apple(settings, arr))

        snake.draw()
        snake.brain(apples, arr)

        if rnd(1, 15) == 3:
            apples.append(Apple(settings, arr))

        if rnd(1, 10) == 3 and not settings.manual_control:
            snake.change_direct(chs(["N", "E", "S", "W"]))

    for apple in apples:
        apple.draw()
    tt.update()

    if counter % 10 == 0:
        os.system("cls")
        print("\nSnake num: ", len(arr), "\nMax Score: ", max_score)
        counter = 0

    sleep(0.05)
    # m.getch()


tt.mainloop()
