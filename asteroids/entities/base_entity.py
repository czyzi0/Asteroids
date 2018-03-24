import pygame as pg

from asteroids import config


class BaseEntity:

    def __init__(self, x, y, vx, vy):
        self.pos = pg.math.Vector2(x, y)
        self.vel = pg.math.Vector2(vx, vy)

    def update(self):
        pass

    def display(self, screen):
        pass

    def move(self, size):
        self.pos += self.vel
        if self.pos.x < -size:
            self.pos.x = config.WIDTH + size
        if self.pos.y < -size:
            self.pos.y = config.HEIGHT + size
        if self.pos.x > config.WIDTH + size:
            self.pos.x = -size
        if self.pos.y > config.HEIGHT + size:
            self.pos.y = -size
