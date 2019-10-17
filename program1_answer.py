# turn a single light on
from neopixel.serial_library import write, WIDTH, HEIGHT
from neopixel.color_library import color_names, hsv2rgb
from time import time, sleep
import numpy as np

##############################################
# SET UP
##############################################

# initialize led array
leds = np.zeros((WIDTH, HEIGHT, 3))

# variables for drawing logic go here

# set a target framerate (max possible is around 60)
fps = 10
# variables for framerate logic
spf = 1 / fps
last_draw_time = time()


##############################################
# DRAW LOOP
##############################################

while True:

    #----------------------------------------
    # DRAWING LOGIC GOES HERE
    #----------------------------------------
        
    # set the led at location (0, 0) to red
    leds[0, 0] = (255, 0, 0)

    # alternatively, set the led by hue (h)
    # leds[0, 0] = col.hsv2rgb(h=0, s=1, v=1)

    # END DRAWING LOGIC

    # stay at target framerate
    sleep_duration = last_draw_time + spf - time()
    if sleep_duration > 0:
        sleep(sleep_duration)
    last_draw_time = time()

    # update the matrix
    write(leds)
