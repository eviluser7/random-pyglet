# drawing shapes
# shape drawn will depend on the sys.argv[]

import sys
import pyglet
from pyglet import shapes

shape_to_draw = sys.argv[1] # python drawing-shapes.py rectangle (example)

# rectangle values
rectangle_width = 64   # play with these values!
rectangle_height = 64

# circle values
circle_radius = 50

window = pyglet.window.Window(width=1024, height=600, caption="Drawing shapes")

rectangle = shapes.Rectangle(x=window.width/2-(rectangle_width/2), y=window.height/2-(rectangle_height/2),
                             width=rectangle_width, height=rectangle_height,
                             color=(255, 255, 255)) # draw a white square in the middle of the screen

circle = shapes.Circle(x=window.width/2, y=window.height/2, radius=circle_radius,
                       color=(255, 255, 255)) # draw a white circle in the middle of the screen

@window.event
def on_draw():
    window.clear()

    if shape_to_draw == "rectangle".lower():
        rectangle.draw()
    elif shape_to_draw == "circle".lower():
        circle.draw()
    elif shape_to_draw == "all".lower():
        rectangle.x = 500
        circle.x = 700

        # for this kind of stuff, batching is better
        rectangle.draw()
        circle.draw()
    else:
        # check if the sys.argv[1] is something that is not included in this branch
        print("Please specify what shape you wish to draw")
        print("rectangle / circle / all")

pyglet.app.run()