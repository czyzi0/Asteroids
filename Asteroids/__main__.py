import pygame as pg

from . import assets
from . import config
from .scenes import TitleScene


def main():
    pg.init()

    pg.display.set_caption('Asteroids')
    pg.display.set_icon(assets.get_image('icon.png'))

    screen = pg.display.set_mode((config.WIDTH, config.HEIGHT))
    clock = pg.time.Clock()

    active_scene = TitleScene()

    while active_scene:
        pressed_keys = pg.key.get_pressed()

        filtered_events = []
        for event in pg.event.get():
            quit_attempt = False
            if event.type == pg.QUIT:
                quit_attempt = True

            if quit_attempt:
                active_scene.terminate()
            else:
                filtered_events.append(event)

        active_scene.process_input(filtered_events, pressed_keys)
        active_scene.update()
        active_scene.display(screen)

        active_scene = active_scene.next_scene

        pg.display.flip()
        clock.tick(config.FPS)


if __name__ == '__main__':
    main()
