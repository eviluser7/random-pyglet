# looping sounds

import pyglet

window = pyglet.window.Window(width=1024, height=600, caption="Loop a sound")
label = pyglet.text.Label(text="It's worth mentioning that looping sounds can be used to play a repeating music.",
                          font_name='Times New Roman',
                          font_size=20,
                          x=window.width/2, y=window.height/2,
                          anchor_x='center', anchor_y='center')

# load the sound as media
music = pyglet.resource.media('resources/song1.wav', streaming=False)

# set the sound as a media player, queue the original file
# into the player, set the looping parameter as true, and play it
song = pyglet.media.Player()
song.queue(music)
song.loop = True

@window.event
def on_draw():
    window.clear()
    label.draw()

song.play()

pyglet.app.run()