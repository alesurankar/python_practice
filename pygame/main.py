from window import Window
from graphics import Graphics
from app import App

FPS = 60
wnd = Window(800, 600)
gfx = Graphics(wnd, FPS)
app = App(gfx, wnd.kbd)

while wnd.ProcessMessage():
    app.Go()

wnd.Quit()