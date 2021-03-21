# handling keyboard input

import pyglet
from pyglet.window import key

# define variables
window = pyglet.window.Window(width=1024, height=600, caption="Handling input")
text = "Go ahead and press a key"
label = pyglet.text.Label(text=text,
                          font_name='Times New Roman',
                          font_size=24,
                          x=180, y=570,
                          anchor_x='center', anchor_y='center')  # this will change

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.W:
        label.text = "Pressed the W key"
    elif symbol == key.A:
        label.text = "Pressed the A key"
    elif symbol == key.S:
        label.text = "Pressed the S key"
    elif symbol == key.D:
        label.text = "Pressed the D key"
    else:
        label.text = "Pressed some other key"

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()