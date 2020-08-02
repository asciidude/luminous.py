import pyglet
from pyglet.gl import *
from pyglet.window import *
from pyglet.media import *
from pyglet.clock import *
import math
import os

"""
TODO:
window.zoomscroll(True) not luminous.window because more than 1
key events
sound volume
"""

keys = key.KeyStateHandler()

# create the window
def createwin(name, width, height, resizable, callback, icon=None):
    iconbool = False
    win = window(width, height, name, resizable)
    win.push_handlers(keys)
    @win.event
    def on_draw():
        pyglet.clock.tick()
        win.clear()
        callback(win)
    
    if icon:
        iconbool = True
    if iconbool:
        image = pyglet.image.load(icon)
        win.set_icon(image)
            
    return win

def createpolygons(n, xpos, ypos):
    angle = 2*math.pi/n
    vertex = [100, 0, 0]
    for i in range(n - 1):
        x = vertex[i * 3] * math.cos(angle) - vertex[i * 3 + 1] * math.sin(angle)
        y = vertex[i * 3 + 1] * math.cos(angle) + vertex[i * 3] * math.sin(angle)
        vertex.extend([x, y, 0])

    for i in range(3 * n):
        if i % 3 == 0:
            vertex[i] -= xpos
        if i % 3 == 1:
            vertex[i] -= ypos
    
    return vertex

def colordata(n):
    return [0]*3*n

def callfunction(callback):
    return callback

class window(pyglet.window.Window):
    # initialize window, etc
    def __init__(self, width, height, name, resize=True):
        super().__init__(width, height, name, resizable=resize)
        self.width = width
        self.height = height
        self.set_minimum_size(400, 300)
        pyglet.gl.glClearColor(_r, _g, _b, _a)

    # create text
    def createtxt(text="Hello world!", font="Arial", size=50, x=0, y=0):
        label = pyglet.text.Label(
            text,
            font_name = font,
            font_size = size,
            x = x, y = y
        )
        return label

    # key events
    """
        ideas:
        #1 -
        make a dictionary of keys registered in pyglet
        look for key used in that dictionary
        when key is used it registers a keydown/up/hold event
        when event is registered it runs a callback function
        #2 -
        use pyglet.keys to load all keys and look for key that
        is used
    """
    def on_key_press(self, symbol, modifiers):
        pass # work on it later -.-

    # play sound
    def playsound(path="music.mp3", volume=1.0):
        player = Player()
        source = load(path)
        player.volume = volume
        player.queue(source)

    # zoom scroll function
    _zoomscroll = True
    def zoomscroll(boolValue=False):
        global _zoomscroll
        _zoomscroll = bool
        
    # set bg function
    def setbg(r=0, g=0, b=0, a=0):
        # get params and replace gl.glClearColor(r, g, b, a)
        global _r, _g, _b, _a
        _r = r
        _g = g
        _b = b
        _a = a
        
    # on resize function
    def on_resize(self, width, height):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glOrtho(width, -width, height, -height, -1, 1)
        glViewport(0, 0, width, height)
        self.width = width
        self.height = height
    
    # mouse motion function
    def mouse_move(callback):
        def on_mouse_motion(self, x, y, dx, dy):
            self.y = x
            self.y = y
            return callback

    # check if mouse scrolls
    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        zoom = 1.00
        if scroll_y > 0:
            zoom = 1.03
        elif scroll_y < 0:
            zoom = 0.97
        
        try:
            if _zoomscroll:
                glOrtho(-zoom, zoom, -zoom, zoom, -1, 1)
            else:
                glOrtho(1)
        except:
            pass
    
    def createsprite(path="/sprite.png", angle=180, x=50, y=50, w=0.5, h=0.5, opacity=255):
        image = pyglet.resource.image(path)
        image.anchor_x = image.width / 2
        image.anchor_y = image.width / 2
        sprite = pyglet.sprite.Sprite(image, x = x, y = y)
        sprite.image.anchor_x = sprite.image.width / 2
        sprite.image.anchor_y = sprite.image.height / 2
        sprite.scale_x = w
        sprite.scale_y = h
        sprite.rotation = angle
        return sprite
    
    def exit_callback(self, dt):
        self.close()
    
    def start(self=None):
        pyglet.app.run()