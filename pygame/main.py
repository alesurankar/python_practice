from window import Window
from graphics import Graphics
from app import App

wnd = Window(640, 480)
gfx = Graphics(wnd)
app = App(gfx)

while wnd.ProcessMessage():
    app.Go()

wnd.Quit()