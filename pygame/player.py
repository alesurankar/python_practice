from livingEntity import LivingEntity
from colors import Colors

class Player(LivingEntity):
    def __init__(self, x, y, kbd):
        super().__init__(x, y, 0, 0, Colors.Green)
        self.kbd = kbd
        self.speed = 1

    def Update(self):
        if self.kbd.KeyIsPressed("K_SPACE"):
            self.speed = 3
        else: self.speed = 1
        if self.kbd.KeyIsPressed("K_w"):
            self.y -= self.speed
        if self.kbd.KeyIsPressed("K_a"):
            self.x -= self.speed
        if self.kbd.KeyIsPressed("K_s"):
            self.y += self.speed
        if self.kbd.KeyIsPressed("K_d"):
            self.x += self.speed
        super().CheckBorders()

    def Draw(self, gfx):
        super().Draw(gfx)