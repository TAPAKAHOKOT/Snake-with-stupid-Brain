
import math
import numpy as np


def draw_field(drawer, cell_size, window_size):

    window_size = [window_size[0] - 50, window_size[1] - 50]

    going_down_y = 0
    for _ in range(math.ceil(window_size[1] / cell_size) + 1):

        drawer.up()
        drawer.goto(-window_size[0] // 2, window_size[1] // 2 - going_down_y)
        drawer.down()

        drawer.goto(window_size[0] // 2, window_size[1] // 2 - going_down_y)
        going_down_y += cell_size

    going_right_x = 0
    for _ in range(math.ceil(window_size[0] / cell_size) + 1):
        drawer.up()
        drawer.goto(-window_size[0] // 2 +
                    going_right_x, -window_size[1] // 2)
        drawer.down()

        drawer.goto(-window_size[0] // 2 + going_right_x, window_size[1] // 2)
        going_right_x += cell_size

    return np.array(
        [
            np.ones(math.ceil(window_size[0] / cell_size))
            for _ in range(math.ceil(window_size[1] / cell_size))
        ]
    )
