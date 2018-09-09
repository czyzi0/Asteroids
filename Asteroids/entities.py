import math
import random

import pygame as pg

from . import config


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
