from luminous import *
from pyglet.window import key

window.zoomscroll(True)
window.setbg(0.9, 0.7, 0.6, 1.0)

s = window.createsprite(
    path="assets/testSprite.png", 
    angle=180, 
    x=0, y=0, 
    w=0.5, h=0.5, 
    opacity=255
)

l = window.createtxt(
    text="Hello, world!", 
    font="Arial", 
    size=50, 
    x=0, y=0
)

def gameloop(window):
    s.draw()
    l.draw()

def on_key_press():
    # WORK IN PROGRESS
    if keys[key.ENTER]:
        s.x += 5

window.playsound(
    path="assets/music.mp3", 
    volume=1.0
)

window = createwin(
    name="Luminous Testing",
    width=120,
    height=120,
    resizable=True,
    callback=gameloop,
    icon="assets/icon.png"
)

window.start() # start window

# TODO list in luminous.py
# Key list: https://pyglet.readthedocs.io/en/latest/programming_guide/keyboard.html