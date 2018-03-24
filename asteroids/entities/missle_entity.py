import pygame as pg

from asteroids import config
from asteroids.entities import BaseEntity


class Missle(BaseEntity):

    V_MAX = 350 / config.FPS
    RANGE = 1.5 * config.FPS
    RADIUS = 2

    def __init__(self, x, y, v_dir):
        super().__init__(x=x, y=y, vx=self.V_MAX*v_dir.x, vy=self.V_MAX*v_dir.y)
        self.vertices = [self.RADIUS * v_dir, -self.RADIUS * v_dir]
        self.range = self.RANGE
        self.to_remove = False

    def update(self):
        super().move(self.RADIUS)
        self.range -= 1
        if self.range < 0:
            self.to_remove = True

    def display(self, screen):
        translated_vertices = [self.pos + vert for vert in self.vertices]
        pg.draw.line(screen, config.COLOR, *translated_vertices, config.LINE_WIDTH)
