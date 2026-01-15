from player import Player
from enemy import Enemy

class App:
    def __init__(self, gfx, kbd):
        self.gfx = gfx
        self.kbd = kbd
        self.player = Player(20, 20)
        self.enemy = Enemy(50, 50)

    def Go(self):
        self.gfx.BeginFrame()
        self.UpdateFrame()
        self.ComposeFrame()
        self.gfx.EndFrame()

    def UpdateFrame(self):
        self.player.Update(self.kbd)
        self.enemy.Update()

    def ComposeFrame(self):
        self.player.Draw(self.gfx)
        self.enemy.Draw(self.gfx)