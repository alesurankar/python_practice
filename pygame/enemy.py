from graphics import Graphics
from colors import Colors

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 12
        self.height = 12
        self.speed = 0.4
        self.vx = 1
        self.vy = 1

    def Update(self):
        self.x += self.vx * self.speed
        self.y += self.vy * self.speed

    def Draw(self, gfx):
        gfx.DrawRect(int(self.x), int(self.y), self.width, self.height, Colors.Red)