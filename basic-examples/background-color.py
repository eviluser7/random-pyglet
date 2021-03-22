# change the background color using a shape of the screen's width

import pyglet
from pyglet import shapes

window = pyglet.window.Window(1024, 600, caption="Set background color")
background = shapes.Rectangle(0, 0, window.width, window.height, color=(255, 255, 255)) # draw white rectangle of the size of the screen. find RGB values to get more colors!

@window.event
def on_draw():
    window.clear()
    background.draw()

pyglet.app.run()