# control a shape with the keys
# warning: this code may seem complex, but it's actually fairly simple.
# you'll need some python knowledge for this one, but take this as a template
# for moving a shape on the screen. bigger examples on the minigames/ directory

import pyglet
from pyglet.window import key
from pyglet import shapes

# variables
window = pyglet.window.Window(width=1024, height=600, caption="Control a shape")
label = pyglet.text.Label(text="Use WASD to move this little square around.",
                          font_name='Times New Roman', font_size=24,
                          color=(0, 255, 255, 255),
                          x=window.width/2, y=window.height/2,
                          anchor_x='center', anchor_y='center')

player_x = (window.width/2-32)
player_y = (window.height/2-32)
rectangle = shapes.Rectangle(player_x, player_y, 64, 64, color=(255, 255, 255))

# classes
class Player:
    def __init__(self):
        self.x = player_x
        self.y = player_y
        self.vx = 0
        self.vy = 0

    def draw(self):
        rectangle.draw()
    

    def change_position(self, vx, vy):
        self.vx = vx
        self.vy = vy
    
    def is_key_pressed(self):
        for _, v in keys.items():
            if v:
                return True

        return False

    def update(self, dt):
        # update position
        new_x = self.x + self.vx * dt
        new_y = self.y + self.vy * dt

        self.x = new_x
        self.y = new_y
        rectangle.x = self.x
        rectangle.y = self.y

        # check what key is being pressed
        
        # linear movement
        if keys[key.W]:
            self.change_position(0, 340)
        elif keys[key.A]:
            self.change_position(-340, 0)
        elif keys[key.S]:
            self.change_position(0, -340)
        elif keys[key.D]:
            self.change_position(340, 0)

        # diagonal movement
        if keys[key.W] and keys[key.A]:
            self.change_position(-340, 340)
        elif keys[key.W] and keys[key.D]:
            self.change_position(340, 340)
        
        if keys[key.S] and keys[key.A]:
            self.change_position(-340, -340)
        elif keys[key.S] and keys[key.D]:
            self.change_position(340, -340)
        
        # make player stay still
        if not self.is_key_pressed():
            self.change_position(0, 0)


# instance our player class
player = Player()

@window.event
def update(dt):
    player.update(dt)

@window.event
def on_draw():
    window.clear()
    player.draw()
    label.draw()

keys = key.KeyStateHandler()
window.push_handlers(keys)

pyglet.clock.schedule_interval(update, 1/60) # call the update function every 60 frames per second
pyglet.app.run()
