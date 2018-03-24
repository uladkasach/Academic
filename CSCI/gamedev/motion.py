## import and define basics
from bge import logic
from bge import events

controller = logic.getCurrentController()
scene = logic.getCurrentScene()
snek = controller.owner



## define keypresses
key = logic.keyboard.events
keypress = dict({
    "left" : key[events.AKEY],
    "right" : key[events.DKEY],
    "forward" : key[events.WKEY],
    "back" : key[events.SKEY],
})
#kbright = key[events.RIGHTARROWKEY]
#kbup = key[events.UPARROWKEY]
#kbdown = key[events.DOWNARROWKEY]


## Linear Motion
velocity = 5.5;
motion = dict({
    "left" : 0,
    "forward" : 0,
    "up" : 0,
})
#if(keypress["left"] > 0): motion["left"] += velocity;
#if(keypress["right"] > 0): motion["left"] -= velocity;
if(keypress["forward"] > 0): motion["forward"] -= velocity;
if(keypress["back"] > 0): motion["forward"] = 0.0; # no backwards, just stops motion

snek.setLinearVelocity([motion["left"], motion["up"], motion["forward"]], True)

## Angular Motion
rotation_magnitude = 0.3;
rotation = 0;
if(keypress["left"] > 0): rotation += rotation_magnitude;
if(keypress["right"] > 0): rotation -= rotation_magnitude;
snek.applyRotation([0.0, rotation, 0.0], True)
