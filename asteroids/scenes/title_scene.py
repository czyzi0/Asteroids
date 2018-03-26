import random

import pygame as pg

from asteroids import assets
from asteroids import config
from asteroids.entities import Asteroid
from asteroids.gui import Text
from asteroids.scenes import BaseScene


class TitleScene(BaseScene):

    def __init__(self):
        super().__init__()
        # Widgets
        self.title_text = Text('CENTER', 50, 'ASTEROIDS', assets.get_font('vector_battle.ttf', 80))
        self.menu_text = Text(
            'CENTER', config.HEIGHT - 200, 'press ENTER to start', assets.get_font('vector_battle.ttf', 20))
        # Entities
        self.asteroids = [
            Asteroid(
                x=random.randint(0, config.WIDTH),
                y=random.randint(0, config.HEIGHT),
                r=random.randint(20, 50)
            )
            for _ in range(15)
        ]

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                assets.play_sound('beat.wav')
                from asteroids.scenes import GameScene
                self.next_scene = GameScene()

    def update(self):
        for asteroid in self.asteroids:
            asteroid.update()

    def display(self, screen):
        screen.fill(config.BACKGROUND)
        # Entites
        for asteroid in self.asteroids:
            asteroid.display(screen)
        # Widgets
        self.title_text.display(screen)
        self.menu_text.display(screen)
