class BaseScene:

    def __init__(self):
        self.next_scene = self

    def process_input(self, events, pressed_keys):
        pass

    def update(self):
        pass

    def display(self, screen):
        pass

    def terminate(self):
        self.next_scene = None
