import os

import pygame as pg

from asteroids import config


images_dict = {}
sounds_dict = {}
fonts_dict = {}


def get_font(name, size):
    font = fonts_dict.get((name, size))
    if font == None:
        path = os.path.join(os.path.dirname(__file__), 'fonts', name)
        font = pg.font.Font(path, size)
        fonts_dict[(name, size)] = font
    return font


def get_image(name):
    image = images_dict.get(name)
    if image == None:
        path = os.path.join(os.path.dirname(__file__), 'images', name)
        image = pg.image.load(path)
        images_dict[name] = image
    return image


def play_sound(name):
    sound = sounds_dict.get(name)
    if sound == None:
        path = os.path.join(os.path.dirname(__file__), 'audio', name)
        sound = pg.mixer.Sound(path)
        sounds_dict[name] = sound
    if config.SOUNDS_ON:
        sound.play()
