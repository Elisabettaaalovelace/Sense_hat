from sense_hat import SenseHat, ACTION_RELEASED
import time
sense = SenseHat()
sense.low_light = True
w = [225,225,225]
b = [0,0,0]
r = [255,0,0]
l = [ 128,0,0]
w = [225,225,225]
r = [255,0,0]
l = [ 128,0,0]
G = [0, 255, 0]
R = [255, 0, 0]
W = [255,255,255]
O = [0,0,0]

def image3 ():
    logo =[
    [0,0,0,0,0,0,0,0],
    [0,1,0,0,1,0,1,0],
    [1,0,1,0,0,1,1,0],
    [0,1,0,0,1,0,0,0],
    [0,0,1,1,0,0,1,0],
    [1,0,1,0,1,0,0,1],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    ]
    return logo


def image4 ():
    logo = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
    return logo


def leftMenu(event):
  sense.clear()
  if event.action == ACTION_RELEASED:
    sense.set_pixels(image3)
    
def rightMenu(event):
  sense.clear()
  if event.action == ACTION_RELEASED:
    sense.set_pixels(image4)
  
sense.stick.direction_right = rightMenu
sense.stick.direction_left = leftMenu
