import bl2sdk
from bl2sdk import *

import random


class Snake:
    def __init__(self, console):
        self.clock = 0.042  # ~24 fps
        self.counter = 0.0
        self.points = 0
        self.console = console
        self.console.set_game(self)
        self.dir = [1, 0]
        self.snake_x = self.console.max_width // 4  # start x axis
        self.snake_y = self.console.max_height // 2  # start y axis
        self.snake = [
            [self.snake_x, self.snake_y],
            [self.snake_x - 1, self.snake_y],
            [self.snake_x - 2, self.snake_y],
        ]
        self.food = [
            [random.randint(5, self.console.max_width - 6), random.randint(5, self.console.max_height - 6)]
        ]
        self.ate_food = False

    def update_pos(self):
        self.ate_food = False
        new_head = [self.snake[0][0] + self.dir[0], self.snake[0][1] + self.dir[1]]
        self.snake.insert(0, new_head)  # inserting the new head position

        # Check death
        if self.snake[0][0] in [1, self.console.max_width] or self.snake[0][1] in [1, self.console.max_height - 1]\
                or self.snake[0] in self.snake[1:]:
            # ToDo Draw End screen
            self.console.set_game(None)
            del self
            return

        # check snake food collision
        for f_xy in self.food:
            if self.snake[0][0] == f_xy[0] and self.snake[0][1] == f_xy[1]:
                # don't pop tail
                # remove food
                f_xy[0] = 0
                f_xy[1] = 0
                self.ate_food = True
                self.points += 100

        if not self.ate_food:
            self.snake.pop()

        # spawn new food if needed
        for xy in self.food:
            if xy[0] == 0 and xy[1] == 0:  # x == 0 and y == 0 means food was eaten
                xy[0] = random.randint(5, self.console.max_width - 6)  # give new x position
                xy[1] = random.randint(5, self.console.max_height - 6)  # give new y position

    def create_frame(self):
        # header list, SNAKE Points: # xyz
        header = list("SNAKE - Points: # {}".format(self.points))
        mid = len(header) // 2
        for x in range(self.console.max_width // 2 - mid, self.console.max_width // 2 - mid + len(header)):
            self.console.draw_pixel(x, 0, header[x - (self.console.max_width // 2 - mid)])

        self.console.draw_line_ver(0, ']')  # Walls
        self.console.draw_line_ver(self.console.max_width - 1, '[')  # Walls
        for x in range(160):
            self.console.draw_pixel(x, 1, '_')  # Walls
            self.console.draw_pixel(x, self.console.max_height - 1, 'T')  # Walls

        for xy in self.food:
            self.console.draw_pixel(xy[0], xy[1], '+')
        for i, xy in enumerate(self.snake):
            self.console.draw_pixel(xy[0], xy[1], "s" if i == 0 else "o")

    def on_input(self, key):
        xy = self.dir
        if key == "w":
            if xy[1] == 1:
                return
            xy[0] = 0
            xy[1] = -1
        if key == "s":
            if xy[1] == -1:
                return
            xy[0] = 0
            xy[1] = 1
        if key == "a":
            if xy[0] == 1:
                return
            xy[0] = -1
            xy[1] = 0
        if key == "d":
            if xy[0] == -1:  # if we go left, we cant go right
                return
            xy[0] = 1
            xy[1] = 0
        if key == "x":
            self.console.set_game(None)
            del self

    def on_tick(self, delta_time):
        self.counter += delta_time
        self.points += ((200 * delta_time) // 2)
        if self.counter > self.clock:
            self.counter = 0.0
            self.console.clear_frame()
            self.update_pos()
            self.create_frame()
            self.console.draw_frame()

    @staticmethod
    def get_controlls():
        return "w: up; s: down; a: left; d: right; x: quit"
