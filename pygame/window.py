import pygame
from inputMouse import Mouse
from inputKeyboard import Keyboard

class Window:
    def __init__(self, width=200, height=200):
        pygame.init()
        pygame.display.set_caption("My pygame Screen")
        self.screen = pygame.display.set_mode((width, height))
        self.width = width
        self.height = height
        self.clock = pygame.time.Clock()
        self.running = True
        self.mouse = Mouse()
        self.kbd = Keyboard()

    def ProcessMessage(self) -> bool:
        events = pygame.event.get()
        self.mouse.Update()
        self.kbd.Update()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
        return self.running
        
    def Quit(self):
        pygame.quit()