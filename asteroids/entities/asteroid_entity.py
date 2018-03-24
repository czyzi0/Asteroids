import math
import random

import pygame as pg

from asteroids import config
from asteroids.entities import BaseEntity


class Asteroid(BaseEntity):

    V_MAX = 126 / config.FPS
    V_ANG_MAX = 103 / config.FPS
    VERTS_N_MIN = 8
    VERTS_N_MAX = 14
    ROUGHNESS = 0.3

    def __init__(self, x, y, r):
        super().__init__(
            x=x, y=y,
            vx=random.uniform(-self.V_MAX, self.V_MAX),
            vy=random.uniform(-self.V_MAX, self.V_MAX)
        )
        self.vel_ang = random.uniform(-self.V_ANG_MAX, self.V_ANG_MAX)
        self.r = r
        self.vertices = []
        verts_n = random.randint(self.VERTS_N_MIN, self.VERTS_N_MAX)
        for i in range(verts_n):
            mod_r = self.r * random.uniform(1 - self.ROUGHNESS, 1 + self.ROUGHNESS)
            self.vertices.append(pg.math.Vector2(
                mod_r * math.cos(i * 2 * math.pi / verts_n),
                mod_r * math.sin(i * 2 * math.pi / verts_n)
            ))

    def update(self):
        super().move(self.r)
        for vert in self.vertices:
            vert.rotate_ip(self.vel_ang)

    def display(self, screen):
        translated_vertices = [self.pos + vert for vert in self.vertices]
        pg.draw.polygon(screen, config.COLOR, translated_vertices, config.LINE_WIDTH)
