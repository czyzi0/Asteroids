import pygame as pg

from asteroids import assets
from asteroids import config
from asteroids.entities import Ship
from asteroids.scenes import BaseScene


class GameScene(BaseScene):

    def __init__(self):
        super().__init__()
        self.ship = Ship(x=0.5*config.WIDTH, y=0.5*config.HEIGHT)
        self.missles = []

    def process_input(self, events, pressed_keys):
        for event in events:
            # quit
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                assets.play_sound('beat.wav')
                from asteroids.scenes import TitleScene
                self.next_scene = TitleScene()
            # shooting
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and self.ship:
                assets.play_sound('shot.wav')
                self.missles.append(self.ship.shoot())
        # move ship
        if self.ship:
            self.ship.process_input(
                pressed_keys[pg.K_LEFT], pressed_keys[pg.K_RIGHT], pressed_keys[pg.K_UP])

    def update(self):
        if self.ship:
            self.ship.update()
        for missle in self.missles:
            missle.update()
        self.missles = [missle for missle in self.missles if not missle.to_remove]

    def display(self, screen):
        screen.fill(config.BACKGROUND)
        if self.ship:
            self.ship.display(screen)
        for missle in self.missles:
            missle.display(screen)
