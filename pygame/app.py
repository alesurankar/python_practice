class App:
    def __init__(self, gfx):
        self.gfx = gfx

    def Go(self):
        self.gfx.BeginFrame()
        self.UpdateFrame()
        self.ComposeFrame()
        self.gfx.EndFrame()

    def UpdateFrame(self):
        pass

    def ComposeFrame(self):
        self.gfx.PutPixel(20, 20, (255, 0, 0))