import pathlib

import pygame as pg

from .. import config


# pylint: disable=invalid-name
_fonts_dict = {}
_images_dict = {}
_sounds_dict = {}


def get_font(name, size):
    font = _fonts_dict.get((name, size))
    if font is None:
        path = pathlib.Path(__file__).parent / 'fonts' / name
        font = pg.font.Font(str(path), size)
        _fonts_dict[(name, size)] = font
    return font


def get_image(name):
    image = _images_dict.get(name)
    if image is None:
        path = pathlib.Path(__file__).parent / 'images' / name
        image = pg.image.load(str(path))
        _images_dict[name] = image
    return image


def play_sound(name):
    sound = _sounds_dict.get(name)
    if sound is None:
        path = pathlib.Path(__file__).parent / 'audio' / name
        sound = pg.mixer.Sound(str(path))
        _sounds_dict[name] = sound
    if config.SOUNDS_ON:
        sound.play()
