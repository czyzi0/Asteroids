from asteroids import config
from asteroids.gui import BaseWidget


class Text(BaseWidget):

    def __init__(self, x, y, text, font):
        self.text = font.render(text, True, config.COLOR)

        if x == 'CENTER':
            x = (config.WIDTH - self.text.get_width()) / 2
        if y == 'CENTER':
            y = (config.HEIGHT - self.text.get_height()) / 2
        super().__init__(x, y)

    def display(self, screen):
        screen.blit(self.text, (self.pos.x, self.pos.y))
