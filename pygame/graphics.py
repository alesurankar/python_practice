import pygame
from colors import Colors

class Graphics:
    wndWidth = 0
    wndHeight = 0

    def __init__(self, window, FPS):
        self.FPS = FPS
        self.screen = window.screen    
        self.clock = window.clock    
        Graphics.wndWidth = window.width
        Graphics.wndHeight = window.height

    def PutPixel(self, x, y, color):
        if 0 <= x < Graphics.wndWidth and 0 <= y < Graphics.wndHeight:
            if hasattr(color, "r"):
                self.screen.set_at((x, y), (color.r, color.g, color.b))
            else:
                self.screen.set_at((x, y), color)

    def DrawRect(self, x, y, width, height, color):
        for iy in range(y, y + height):
            for ix in range(x, x + width):
                self.PutPixel(ix, iy, color)


    def BeginFrame(self, color=Colors.DarkGray):
        self.screen.fill(color)

    def EndFrame(self):
        pygame.display.flip()
        self.clock.tick(self.FPS)
