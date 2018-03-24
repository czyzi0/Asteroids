import random

import pygame as pg

from asteroids import assets
from asteroids import config
from asteroids.entities import Ship, Asteroid
from asteroids.gui import Text
from asteroids.scenes import BaseScene


class GameScene(BaseScene):

    def __init__(self):
        super().__init__()
        # Logic
        self.paused = False
        self.points = 0
        self.lives = config.START_LIVES - 1
        # Entities
        self.ship = Ship(x=0.5*config.WIDTH, y=0.5*config.HEIGHT)
        self.missles = []
        self.asteroids = [
            Asteroid(
                x=random.randint(0, config.WIDTH),
                y=random.randint(0, config.HEIGHT),
                r=random.randint(40, 50)
            )
            for _ in range(config.START_ASTEROIDS)
        ]
        # Widgets
        self.points_text = Text(5, 5, str(self.points), assets.get_font('vector_battle.ttf', 20))
        self.lives_text = Text(5, 30, 'x' + str(self.lives), assets.get_font('vector_battle.ttf', 20))
        self.paused_text = Text('CENTER', 150, 'PAUSED', assets.get_font('vector_battle.ttf', 20))
        self.lost_text = Text('CENTER', 'CENTER', 'press ENTER', assets.get_font('vector_battle.ttf', 20))

    def process_input(self, events, pressed_keys):
        for event in events:
            # quit
            if (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
                or
                event.type == pg.KEYDOWN and event.key == pg.K_RETURN and self.lives < 0
            ):
                assets.play_sound('beat.wav')
                from asteroids.scenes import TitleScene
                self.next_scene = TitleScene()
            # pause
            if event.type == pg.KEYDOWN and event.key == pg.K_p and self.lives >= 0:
                assets.play_sound('beat.wav')
                self.paused = not self.paused
            # shooting
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and self.ship:
                assets.play_sound('shot.wav')
                self.missles.append(self.ship.shoot())
        # move ship
        if self.ship:
            self.ship.process_input(
                pressed_keys[pg.K_LEFT], pressed_keys[pg.K_RIGHT], pressed_keys[pg.K_UP])

    def update(self):
        if not self.paused:
            # Entities
            if self.ship:
                self.ship.update()
            for missle in self.missles:
                missle.update()
            for asteroid in self.asteroids:
                asteroid.update()
            # Add new asteroid from time to time
            self.new_asteroid()
            # Collisions
            self.resolve_missle_asteroid_collisions()
            self.resolve_ship_asteroids_collisions()
            # Delete old objects
            self.missles = [missle for missle in self.missles if not missle.to_remove]

    def display(self, screen):
        screen.fill(config.BACKGROUND)
        # Entities
        if self.ship:
            self.ship.display(screen)
        for missle in self.missles:
            missle.display(screen)
        for asteroid in self.asteroids:
            asteroid.display(screen)
        # Widgets
        self.points_text.display(screen)
        self.lives_text.display(screen)
        if self.paused:
            self.paused_text.display(screen)
        if self.lives < 0:
            self.lost_text.display(screen)

    def new_asteroid(self):
        if (
            random.uniform(0, 1) < 1 / (config.FPS * config.NEW_ASTEROID_PERIOD)
            and
            len(self.asteroids) < 30
        ):
            r = random.randint(40, 50)
            x = -r if random.uniform(0, 1) < 0.5 else config.WIDTH + r
            y = -r if random.uniform(0, 1) < 0.5 else config.HEIGHT + r
            self.asteroids.append(Asteroid(x=x, y=y, r=r))

    def resolve_missle_asteroid_collisions(self):
        for i in range(len(self.missles)-1, -1, -1):
            for j in range(len(self.asteroids)-1, -1, -1):
                dist_vec = self.missles[i].pos - self.asteroids[j].pos
                crash_dist_squared = self.asteroids[j].r ** 2
                if dist_vec.length_squared() <= crash_dist_squared:
                    self.missles.pop(i)
                    self.break_asteroid(j)
                    break

    def resolve_ship_asteroids_collisions(self):
        if self.ship and not self.ship.shield:
            for i in range(len(self.asteroids)-1, -1, -1):
                dist_vec = self.ship.pos - self.asteroids[i].pos
                crash_dist_squared = (self.ship.r + self.asteroids[i].r)**2
                if dist_vec.length_squared() <= crash_dist_squared:
                    assets.play_sound('bang_large.wav')
                    self.lives -= 1
                    self.break_asteroid(i)
                    if self.lives < 0:
                        self.ship = None
                    else:
                        self.ship = Ship(x=0.5*config.WIDTH, y=0.5*config.HEIGHT)
                        self.lives_text = Text(5, 30, 'x' + str(self.lives), assets.get_font('vector_battle.ttf', 20))
                    break

    def break_asteroid(self, index):
        if self.asteroids[index].r >= 20:
            assets.play_sound('bang_medium.wav')
            self.points += 50
            x = self.asteroids[index].pos.x
            y = self.asteroids[index].pos.y
            r = 0.5 * self.asteroids[index].r
            self.asteroids.append(Asteroid(x=x, y=y, r=r))
            self.asteroids.append(Asteroid(x=x, y=y, r=r))
        else:
            assets.play_sound('bang_small.wav')
            self.points += 100
        self.asteroids.pop(index)
        self.points_text = Text(5, 5, str(self.points), assets.get_font('vector_battle.ttf', 20))
