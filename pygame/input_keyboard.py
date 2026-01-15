import pygame

class Keyboard:
    def __init__(self):
        self._keys_held = []
        self._keys_down = set()
        self.quit = False

    def Update(self, events):
        self._keys_held = pygame.key.get_pressed()
        self._keys_down.clear()
        self.quit = False

        for event in events:
            if event.type == pygame.KEYDOWN:
                self._keys_down.add(event.key)
            elif event.type == pygame.QUIT:
                self.quit = True

    def KeyIsPressed(self, key_symbol: str):
        try:
            py_key = getattr(pygame, key_symbol)
        except AttributeError:
            return False
        return self._keys_held[py_key]