import pygame

class Window:
    def __init__(self, width=200, height=200):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.width = width
        self.height = height
        pygame.display.set_caption("Screen")
        self.clock = pygame.time.Clock()
        self.running = True

    def ProcessMessage(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        return self.running
        
    def Quit(self):
        pygame.quit()