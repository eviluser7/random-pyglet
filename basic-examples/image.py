# drawing a simple image

import pyglet

# define the window
window = pyglet.window.Window(width=960, height=1024, caption="Drawing an image")
image = pyglet.resource.image('resources/meow.jpg') # load the image

# things to draw
@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)

# enter the event loop
pyglet.app.run()