import pygame as pg

from asteroids import config
from asteroids.entities import BaseEntity, Missle


class Ship(BaseEntity):

    V_MAX = 240 / config.FPS
    V_RES = 3 / config.FPS
    ROT_RES = 324 / config.FPS
    SHIELD_DUR = 5 * config.FPS

    def __init__(self, x, y, r=15):
        super().__init__(x=x, y=y, vx=0, vy=0)
        self.r = r
        self.vertices = [
            pg.math.Vector2(1.1*r, 0),
            pg.math.Vector2(-r, -r),
            pg.math.Vector2(-0.5*r, 0),
            pg.math.Vector2(-r, r)
        ]
        self.shield = self.SHIELD_DUR

    def process_input(self, left, right, up):
        # rotate
        if right:
            for vert in self.vertices:
                vert.rotate_ip(self.ROT_RES)
        if left:
            for vert in self.vertices:
                vert.rotate_ip(-self.ROT_RES)
        # speed up
        if up:
            self.vel += self.V_RES * self.vertices[0].normalize()
            # constraint velocity
            if self.vel.length() > self.V_MAX:
                self.vel.scale_to_length(self.V_MAX)

    def update(self):
        super().move(self.r)
        if self.shield:
            self.shield -= 1

    def display(self, screen):
        translated_vertices = [self.pos + vert for vert in self.vertices]
        if self.shield % 4 < 2:
            pg.draw.polygon(screen, config.COLOR, translated_vertices, config.LINE_WIDTH)

    def shoot(self):
        missle_pos = self.pos + self.vertices[0]
        return Missle(missle_pos.x, missle_pos.y, self.vertices[0].normalize())
