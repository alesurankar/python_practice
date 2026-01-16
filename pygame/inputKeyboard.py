import pygame

class Keyboard:
    def __init__(self):
        self.keysHeld = []

    def Update(self):
        self.keysHeld = pygame.key.get_pressed()

    def KeyIsPressed(self, symbol: str):
        key = getattr(pygame, symbol)
        return self.keysHeld[key]