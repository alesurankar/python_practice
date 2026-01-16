import pygame

class Keyboard:
    def __init__(self):
        self.keysHeld = []
        self.keysDown = set()

    def Update(self, events):
        self.keysHeld = pygame.key.get_pressed()
        self.keysDown.clear()

        for event in events:
            if event.type == pygame.KEYDOWN:
                self.keysDown.add(event.key)

    def KeyIsPressed(self, symbol: str):
        key = getattr(pygame, symbol)
        return self.keysHeld[key]