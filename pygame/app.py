from graphics import Graphics
from player import Player
from enemy import Enemy
import random

class App:
    def __init__(self, gfx, kbd):
        self.gfx = gfx
        self.kbd = kbd
        self.rndX = random.randint(0, Graphics.wndWidth)
        self.rndY = random.randint(0, Graphics.wndHeight)
        self.player = Player(self.rndX, self.rndY)
        self.enemies = []

    def Go(self):
        self.gfx.BeginFrame()
        self.UpdateFrame()
        self.ComposeFrame()
        self.gfx.EndFrame()

    def UpdateFrame(self):
        self.player.Update(self.kbd)
        if random.random() < 0.02:
            self.rndX = random.randint(0, Graphics.wndWidth)
            self.rndY = random.randint(0, Graphics.wndHeight)
            self.rndV = random.uniform(-1, 1)
            self.enemies.append(Enemy(self.rndX, self.rndY, self.rndV, self.rndV))

        for enemy in self.enemies:
            enemy.Update()

    def ComposeFrame(self):
        self.player.Draw(self.gfx)
        for enemy in self.enemies:
            enemy.Draw(self.gfx)