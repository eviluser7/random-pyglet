# drawing a window

import pyglet

# define the window
window = pyglet.window.Window(width=1024, height=600, caption="Window drawing")

# define a text
label = pyglet.text.Label("I'm a window!",
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width/2, y=window.height/2,
                          anchor_x='center', anchor_y='center')

# things to draw
@window.event
def on_draw():
    window.clear()
    label.draw()

# enter the event loop
pyglet.app.run()