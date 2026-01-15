import pygame

class Graphics:
    def __init__(self, window):
        self.window = window
        self.screen = window.screen        
        self.width = window.width
        self.height = window.height
        self.clock = window.clock

    def PutPixel(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
           self.screen.set_at((x, y), color)

    def BeginFrame(self, color=(0, 0, 0)):
        self.screen.fill(color)

    def EndFrame(self):
        pygame.display.flip()
        self.clock.tick(60)
