import turtle as tt
tt.tracer(0, 0)


class Settings:
    def __init__(self):
        self.dwr = tt.Turtle()
        self.dwr.speed(0)
        self.dwr.hideturtle()

        self.window_size = [800, 800]

        tt.setup(self.window_size[0], self.window_size[1])

        self.cell_size = 10

        self.cells_st = None
        self.cells_num = [0, 0]

        self.dead_cells = []

        self.manual_control = True

        self.colors = [
            "Light Pink",
            "Pale Violet Red",
            "Maroon",
            "Medium Violet Red",
            "Orange Red",
            "Red",
            "Orange",
            "Dark Orange",
            "Green Yellow",
            "Lime Green",
            "Yellow Green",
            "Forest Green",
            "Olive Drab",
            "Royal Blue",
            "Blue",
            "Dodger Blue",
            "Deep Sky Blue"
        ]
