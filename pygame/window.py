import pygame
from input_keyboard import Keyboard

class Window:
    def __init__(self, width=200, height=200):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.width = width
        self.height = height
        pygame.display.set_caption("Screen")
        self.clock = pygame.time.Clock()
        self.running = True
        self.kbd = Keyboard()

    def ProcessMessage(self) -> bool:
        events = pygame.event.get()
        self.kbd.Update(events)
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
        return self.running
        
    def Quit(self):
        pygame.quit()