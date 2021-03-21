# using batches
# they work as groups for each object, so let's say
# you want to have a "world" batch. inside this batch
# you'd store whatever object you want to store as part
# of the world, like trees, grass, etc.
# drawing order in code makes changes in rendering order

import pyglet
from pyglet import shapes

batch1 = pyglet.graphics.Batch()
batch2 = pyglet.graphics.Batch()
batch3 = pyglet.graphics.Batch()

window = pyglet.window.Window(width=1024, height=600, caption="Using batches")
label = pyglet.text.Label(text="Change the inner code to change the squares' order",
                          font_name='Times New Roman', font_size=36,
                          x=window.width/2, y=550,
                          anchor_x='center', anchor_y='center')

rectangles = [
    # row 1
    shapes.Rectangle(x=300, y=180, width=100, height=100, color=(255, 0, 0), batch=batch1),   # red
    shapes.Rectangle(x=400, y=180, width=100, height=100, color=(255, 128, 0), batch=batch1), # orange
    shapes.Rectangle(x=500, y=180, width=100, height=100, color=(255, 255, 0), batch=batch1), # yellow

    # row 2
    shapes.Rectangle(x=300, y=260, width=100, height=100, color=(0, 255, 0), batch=batch2),   # green
    shapes.Rectangle(x=400, y=260, width=100, height=100, color=(0, 128, 255), batch=batch2), # blue
    shapes.Rectangle(x=500, y=260, width=100, height=100, color=(127, 0, 255), batch=batch2), # purple

    # row 3
    shapes.Rectangle(x=300, y=340, width=100, height=100, color=(128, 128, 128), batch=batch3), # gray 1
    shapes.Rectangle(x=400, y=340, width=100, height=100, color=(160, 160, 160), batch=batch3), # gray 2
    shapes.Rectangle(x=500, y=340, width=100, height=100, color=(192, 192, 192), batch=batch3) # gray 3
]

@window.event
def on_draw():
    window.clear()
    label.draw()

    # move these up or down to change the order
    batch1.draw()
    batch2.draw()
    batch3.draw()

pyglet.app.run()