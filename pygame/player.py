from colors import Colors

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 12
        self.height = 12
        self.speed = 1

    def Update(self, kbd):
        if kbd.KeyIsPressed("K_SPACE"):
            self.speed = 3
        else: self.speed = 1
        if kbd.KeyIsPressed("K_w"):
            self.y -= self.speed
        if kbd.KeyIsPressed("K_a"):
            self.x -= self.speed
        if kbd.KeyIsPressed("K_s"):
            self.y += self.speed
        if kbd.KeyIsPressed("K_d"):
            self.x += self.speed

    def Draw(self, gfx):
        gfx.DrawRect(self.x, self.y, self.width, self.height, Colors.Green)