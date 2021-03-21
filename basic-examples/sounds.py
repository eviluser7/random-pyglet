# playing sound

import pyglet
from pyglet.window import key

window = pyglet.window.Window(width=1024, height=600, caption="Playing sound")
label = pyglet.text.Label(text="Press space to play a sound",
                          font_name='Times New Roman',
                          font_size=24,
                          x=180, y=570,
                          anchor_x='center', anchor_y='center')
sound = pyglet.resource.media('resources/sound.wav', streaming=False)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.SPACE:
        sound.play()

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()