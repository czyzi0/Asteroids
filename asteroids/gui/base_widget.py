import pygame as pg

from asteroids import config


class BaseWidget:

    def __init__(self, x, y):
        self.pos = pg.math.Vector2(x, y)

    def display(self, screen):
        pass
