# hue waves radiate from the center of the matrix
from neopixel.serial_library import write, WIDTH, HEIGHT
from neopixel.color_library import color_names, hsv2rgb
from time import time, sleep
import numpy as np

##############################################
# SET UP
##############################################

# initialize led array
leds = np.zeros((WIDTH, HEIGHT, 3))

# variables for drawing logic
hue = 0.0
scale = 8.0 # the larger this is, the further apart the color waves are

# set a target framerate (max possible is around 60)
fps = 30
# variables for framerate logic
spf = 1 / fps
last_draw_time = time()


##############################################
# DRAW LOOP
##############################################

while True:

    #----------------------------------------
    # DRAWING LOGIC
    #----------------------------------------

    # for each pixel
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # get distance to center
            coord = (x - 3.5, y - 3.5) # subtract center
            dist = np.linalg.norm(coord)

            leds[x, y] = hsv2rgb(hue + dist / scale, 1, 1)

    # change hue so that colors move outwards over time
    hue -= 0.01

    # END DRAWING LOGIC

    # stay at target framerate
    sleep_duration = last_draw_time + spf - time()
    if sleep_duration > 0:
        sleep(sleep_duration)
    last_draw_time = time()

    # update the matrix
    write(leds)
